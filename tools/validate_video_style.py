"""Validate the video-specific UIgod contract; never replaces visual review."""
import json,sys
from pathlib import Path
p=Path(sys.argv[1]);errors=[]
for name in ['SKILL.md','DESIGN.md','style.json','preview.html','references/source-observations.md','references/frames/index.json','references/code-patterns','examples/index.html']:
    if not (p/name).exists():errors.append('missing '+name)
if not errors:
    data=json.loads((p/'style.json').read_text(encoding='utf-8'))
    if 'video' not in data.get('media',[]):errors.append('media must contain video')
    if data.get('status') not in ['draft','sample-verified','production-verified']:errors.append('invalid status')
    for frame in json.loads((p/'references/frames/index.json').read_text(encoding='utf-8'))['frames']:
        if not (p/'references/frames'/frame['file']).is_file():errors.append('missing frame '+frame['file'])
    if data.get('status')!='draft':
        vp=p/'examples/verification.json'
        if not vp.is_file():errors.append('verified status without verification.json')
        else:
            v=json.loads(vp.read_text(encoding='utf-8'))
            if not v.get('visual_review') or not v.get('decode_pass') or not (p/'examples/transfer.mp4').exists():errors.append('verification incomplete')
    design=(p/'DESIGN.md').read_text(encoding='utf-8')
    for title in ['Signature Moves','Colors','Typography','Layout','Motion & Interaction','Sound & Rhythm','Variables','Prompt Guide','Known Gaps']:
        if '## '+title not in design:errors.append('missing section '+title)
for error in errors:print('FAIL:',error)
if not errors:print('PASS:',p)
sys.exit(bool(errors))
