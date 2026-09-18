from pathlib import Path
import json, hashlib, difflib
root=Path('/Users/ember/dev/breadstuffs')
stage=Path('/tmp/dregg-direct-auth-width-20260918')
reps=json.loads((stage/'replacements.json').read_text())
texts={r['path']:(root/r['path']).read_text() for r in reps}
before=dict(texts)
for r in reps:
    assert texts[r['path']].count(r['old'])==1, 'owned region changed: '+r['path']
    texts[r['path']]=texts[r['path']].replace(r['old'],r['new'],1)
assert 'digest_low' not in texts['dregg-lean-ffi/src/lean_direct.rs']
for suffix in ['signature','proof','bearer','captp','custom','stealth','token']:
    old='dregg_d_auth_'+suffix
    assert old+'(' not in texts['dregg-lean-ffi/src/lean_direct.rs']
    assert '@[export '+old+']' not in texts['metatheory/Dregg2/Exec/FFIDirect.lean']
    assert '@[export '+old+'_w]' in texts['metatheory/Dregg2/Exec/FFIDirect.lean']
# Validate every original region before any writes; preserve concurrent edits outside those regions.
report={}
for path,value in texts.items():
    assert (root/path).read_text()==before[path], 'concurrent source edit: '+path
for path,value in texts.items():
    (stage/(Path(path).name+'.at-apply-before')).write_text(before[path])
    (root/path).write_text(value)
    (stage/(Path(path).name+'.applied.diff')).write_text(''.join(difflib.unified_diff(before[path].splitlines(True),value.splitlines(True),fromfile=path+'.before',tofile=path)))
    report[path]={'before_sha256':hashlib.sha256(before[path].encode()).hexdigest(),'after_sha256':hashlib.sha256(value.encode()).hexdigest()}
(stage/'applied-manifest.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
