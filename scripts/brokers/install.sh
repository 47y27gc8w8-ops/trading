#!/usr/bin/env bash
# Install / remove the paper-broker systemd units.   sudo bash scripts/brokers/install.sh [--uninstall]
set -euo pipefail
here="$(cd "$(dirname "$0")" && pwd)"
ids=$(grep -oP '^  - id: \K\S+' "$here/../../config/brokers.yaml")
[ "$(id -u)" -eq 0 ] || { echo "run with sudo"; exit 1; }
if [ "${1:-}" = "--uninstall" ]; then
  for i in $ids; do systemctl disable --now "broker@$i.service" || true; done
  systemctl disable --now broker-report.timer || true
  rm -f /etc/systemd/system/broker@.service /etc/systemd/system/broker-report.{service,timer}
  systemctl daemon-reload; echo "removed"; exit 0
fi
install -m 644 "$here/broker@.service" "$here/broker-report.service" "$here/broker-report.timer" /etc/systemd/system/
systemctl daemon-reload
for i in $ids; do systemctl enable --now "broker@$i.service"; done
systemctl enable --now broker-report.timer
sleep 3
systemctl --no-pager --plain list-units 'broker@*' 
systemctl --no-pager list-timers broker-report.timer
