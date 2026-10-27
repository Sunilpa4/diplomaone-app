#!/usr/bin/env bash
# Re-creates the build environment for the DiplomaOne Flutter app in a fresh sandbox.
# Everything big goes to /opt (NOT saved in the workspace snapshot).
#   bash tools/setup_build_env.sh          # web only
#   bash tools/setup_build_env.sh android  # + Java 17 + Android SDK
# Afterwards:  source tools/build_env.sh
set -e
FLUTTER_VER=3.47.8
CMDLINE_VER=16111833

# 1) swap – the 2 GB sandbox freezes during builds without it
if ! grep -q /swapfile /proc/swaps 2>/dev/null; then
  [ -f /swapfile ] || sudo fallocate -l 3G /swapfile
  sudo chmod 600 /swapfile && sudo /sbin/mkswap /swapfile >/dev/null && sudo /sbin/swapon /swapfile
  echo "swap on"
fi

sudo mkdir -p /opt/flutter_sdk /opt/android-sdk /opt/jdk17 /opt/gradle-home
sudo chown -R "$(id -u)" /opt/flutter_sdk /opt/android-sdk /opt/jdk17 /opt/gradle-home

# 2) Flutter
if [ ! -x /opt/flutter_sdk/flutter/bin/flutter ]; then
  cd /opt/flutter_sdk
  curl -sSL -o f.tar.xz "https://storage.googleapis.com/flutter_infra_release/releases/stable/linux/flutter_linux_${FLUTTER_VER}-stable.tar.xz"
  tar xf f.tar.xz && rm f.tar.xz
  git config --global --add safe.directory '*'
  echo "flutter extracted"
fi
export PATH=/opt/flutter_sdk/flutter/bin:$PATH PUB_CACHE=/opt/flutter_sdk/pub-cache
flutter --disable-analytics >/dev/null 2>&1 || true
flutter config --no-analytics --enable-web >/dev/null 2>&1 || true

if [ "$1" = "android" ]; then
  # 3) Java 17 (Temurin)
  if [ ! -x /opt/jdk17/bin/java ]; then
    curl -sSL -o /tmp/jdk.tgz "https://api.adoptium.net/v3/binary/latest/17/ga/linux/x64/jdk/hotspot/normal/eclipse"
    tar xzf /tmp/jdk.tgz -C /opt/jdk17 --strip-components=1 && rm /tmp/jdk.tgz
    echo "jdk17 installed"
  fi
  export JAVA_HOME=/opt/jdk17 PATH=/opt/jdk17/bin:$PATH
  # 4) Android command-line tools + licences
  if [ ! -x /opt/android-sdk/cmdline-tools/latest/bin/sdkmanager ]; then
    curl -sSL -o /tmp/clt.zip "https://dl.google.com/android/repository/commandlinetools-linux-${CMDLINE_VER}_latest.zip"
    mkdir -p /opt/android-sdk/cmdline-tools && unzip -q /tmp/clt.zip -d /opt/android-sdk/cmdline-tools
    mv /opt/android-sdk/cmdline-tools/cmdline-tools /opt/android-sdk/cmdline-tools/latest && rm /tmp/clt.zip
    echo "cmdline-tools installed"
  fi
  export ANDROID_HOME=/opt/android-sdk ANDROID_SDK_ROOT=/opt/android-sdk
  yes | /opt/android-sdk/cmdline-tools/latest/bin/sdkmanager --licenses >/dev/null 2>&1 || true
  /opt/android-sdk/cmdline-tools/latest/bin/sdkmanager "platform-tools" >/dev/null
  flutter config --enable-android --android-sdk /opt/android-sdk --jdk-dir /opt/jdk17 >/dev/null
fi
flutter --version | head -1
echo SETUP_DONE
