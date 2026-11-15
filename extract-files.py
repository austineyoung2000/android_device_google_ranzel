#!/bin/bash
set -euo pipefail
root="$(cd -- "$(dirname -- "$0")" && pwd)"
if (($# == 0)); then
    echo "Usage: $0 {blazer|mustang|frankel|rango} [upstream options...]" >&2
    exit 2
fi
device="$1"
shift
case "$device" in
    blazer|mustang|frankel) dir="$root/$device" ;;
    rango) dir="$root/rango/rango" ;;
    *) echo "Unknown device: $device" >&2; exit 2 ;;
esac
cd "$dir"
exec ./extract-files.py "$@"
