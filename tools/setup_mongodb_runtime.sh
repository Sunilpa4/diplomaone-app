#!/usr/bin/env bash
# Reproducible private teaching runtime, tested on Debian 13 x86_64.
# Package binaries/system services do not persist in workspace snapshots.
# Uses the vendor's signed APT repository; does not start a background daemon.
set -euo pipefail
. /etc/os-release
if [[ "$ID" != debian || "$VERSION_ID" != 13 || "$(uname -m)" != x86_64 ]]; then
  echo 'This recipe targets Debian 13 x86_64 only. Use the official guide for your OS.' >&2
  exit 1
fi
key=$(mktemp)
trap 'rm -f "$key"' EXIT
curl --fail --silent --show-error --location https://pgp.mongodb.com/server-9.asc \
  | gpg --batch --yes --dearmor > "$key"
sudo install -m 0644 "$key" /usr/share/keyrings/mongodb-server-9.gpg
printf '%s\n' 'deb [arch=amd64 signed-by=/usr/share/keyrings/mongodb-server-9.gpg] https://repo.mongodb.org/apt/debian trixie/mongodb-org/9.0 main' \
  | sudo tee /etc/apt/sources.list.d/mongodb-org-9.0.list >/dev/null
sudo apt-get update -qq
sudo apt-get install -y --no-install-recommends mongodb-org-server=9.0.4 mongodb-mongosh=2.14.0
mongod --version | head -n 2
mongosh --version
mkdir -p /home/user/.cache/diplomaone-mongodb-u2/data
cat <<'EOF'
Start the private standalone server through the process manager (do not fork):
mongod --dbpath /home/user/.cache/diplomaone-mongodb-u2/data --bind_ip 127.0.0.1 --port 27027 --nounixsocket --auth --wiredTigerCacheSizeGB 0.25 --logpath /home/user/.cache/diplomaone-mongodb-u2/mongod.log
Connect locally: mongosh 'mongodb://127.0.0.1:27027/?directConnection=true'
No public bind, no real personal data, and no replica-set/sharding setup.
After starting it: python3 tools/mongodb_content.py --bootstrap
This creates the private first user via the localhost exception; credentials stay outside the project.
EOF
