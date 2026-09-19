#!/usr/bin/env bash
set -euo pipefail
study=/tmp/minidregg-cycle-20260919/waterfall-study
mkdir /tmp/minidregg-cycle-20260919/lean-seat-2 || exit 75
trap 'rmdir /tmp/minidregg-cycle-20260919/lean-seat-2' EXIT
cd /Users/ember/dev/minidregg
export LEAN_NUM_THREADS=1
lake env lean -o .lake/build/lib/lean/Compiler/TypedAuthorizationRequestCodec.olean -i .lake/build/lib/lean/Compiler/TypedAuthorizationRequestCodec.ilean -c .lake/build/ir/Compiler/TypedAuthorizationRequestCodec.c Compiler/TypedAuthorizationRequestCodec.lean > "$study/logs/CanonicalCodec.log" 2>&1
cat "$study/logs/CanonicalCodec.log"
