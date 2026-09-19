#!/usr/bin/env bash
set -euo pipefail
study=/tmp/minidregg-cycle-20260919/waterfall-study
lean_bin=/Users/ember/.elan/toolchains/leanprover--lean4---v4.30.0/bin/lean
mkdir /tmp/minidregg-cycle-20260919/lean-seat-2 || exit 75
trap 'rmdir /tmp/minidregg-cycle-20260919/lean-seat-2' EXIT
cd /Users/ember/dev/minidregg
mini_lean_path=$(lake env printenv LEAN_PATH)
export LEAN_PATH="$study/upstream/.lake/build/lib/lean:$mini_lean_path"
export LEAN_NUM_THREADS=1
"$lean_bin" "$study/$1.lean" > "$study/logs/$1.log" 2>&1
cat "$study/logs/$1.log"
