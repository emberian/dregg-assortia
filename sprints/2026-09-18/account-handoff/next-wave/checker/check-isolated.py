#!/usr/bin/env python3
"""One source-owned, two-thread Lean check with only /tmp outputs."""
from pathlib import Path
import hashlib
import json
import os
import re
import subprocess
import sys
import time

project = Path('/Users/ember/dev/minidregg')
scratch = Path('/tmp/dregg-delegation-core-effect')
library = scratch / 'olean'
source_root = Path(sys.argv[1]).resolve()
module = sys.argv[2]
if not source_root.is_relative_to(Path('/tmp').resolve()):
    raise SystemExit('source must be a scratch copy under /tmp')
if not re.fullmatch(r'[A-Za-z0-9_]+(?:/[A-Za-z0-9_]+)*', module):
    raise SystemExit('expected a relative module path')
source = source_root / (module + '.lean')
output = library / (module + '.olean')
output.parent.mkdir(parents=True, exist_ok=True)
for artifact in output.parent.glob(output.stem + '.*'):
    if artifact.is_symlink():
        raise SystemExit(f'refusing symlink output or sidecar: {artifact}')
for directory in output.parents:
    if directory == scratch:
        break
    if directory.is_symlink():
        raise SystemExit(f'refusing symlink output directory: {directory}')
environment = dict(os.environ, LEAN_NUM_THREADS='2')
environment['LEAN_PATH'] = str(library) + ':' + subprocess.check_output(
    ['lake', 'env', 'printenv', 'LEAN_PATH'], cwd=project, text=True).strip()
lean = subprocess.check_output(['lake', 'env', 'which', 'lean'],
                              cwd=project, text=True).strip()
log = scratch / (module.replace('/', '-') + '.log')
command = [lean, '-o', str(output), module + '.lean']
started = time.time()
with log.open('w') as stream:
    result = subprocess.run(command, cwd=source_root, env=environment,
                            stdout=stream, stderr=subprocess.STDOUT)
record = {
    'source': str(source), 'module': module,
    'sha256': hashlib.sha256(source.read_bytes()).hexdigest(),
    'cwd': str(source_root), 'command': command,
    'exit': result.returncode, 'seconds': round(time.time() - started, 3),
    'log': str(log), 'output': str(output),
}
with (scratch / 'checks.jsonl').open('a') as stream:
    stream.write(json.dumps(record) + '\n')
print(json.dumps(record), flush=True)
print(log.read_text(), end='', flush=True)
raise SystemExit(result.returncode)
