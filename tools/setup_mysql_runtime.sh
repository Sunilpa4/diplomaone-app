#!/usr/bin/env bash
# Recreate the local MySQLi test runtime after a sandbox reset.
# Requires sudo. Does NOT start a daemon or open a TCP port.
set -euo pipefail
sudo apt-get update -qq
sudo DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends mariadb-server mariadb-client-core php8.4-mysql
ROOT=/home/user/php_root
mkdir -p "$ROOT/usr/lib/php/20240924" "$ROOT/conf.d"
cp /usr/lib/php/20240924/mysqlnd.so /usr/lib/php/20240924/mysqli.so "$ROOT/usr/lib/php/20240924/"
printf 'extension=%s/usr/lib/php/20240924/mysqlnd.so\nextension=%s/usr/lib/php/20240924/mysqli.so\n' "$ROOT" "$ROOT" > "$ROOT/conf.d/20-mysql.ini"
BASE=/tmp/di04007011_mysql
mkdir -p "$BASE"
if [ ! -d "$BASE/data/mysql" ]; then
  mariadb-install-db --no-defaults --datadir="$BASE/data" --auth-root-authentication-method=normal --skip-test-db
fi
cat <<'EOF'
Start this command with the process tool (not bash), then build/test Unit 5:
/usr/sbin/mariadbd --no-defaults --datadir=/tmp/di04007011_mysql/data --socket=/tmp/di04007011_mysql/mysql.sock --pid-file=/tmp/di04007011_mysql/mysql.pid --skip-networking --skip-log-bin --innodb-buffer-pool-size=32M --innodb-log-file-size=8M --aria-pagecache-buffer-size=8M --key-buffer-size=8M --console
No network listener is created. Databases and users are private, disposable test data.
EOF
