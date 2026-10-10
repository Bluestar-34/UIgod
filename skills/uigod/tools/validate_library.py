"""Check shared work metadata and final deliverables without guessing filenames."""
from pathlib import Path
import json,sys,hashlib

root=Path(__file__).resolve().parents[3]
errors=[]
catalog=json.loads((root/'catalog.json').read_text(encoding='utf-8'))
ids=[e['id'] for e in catalog['entries']]
if len(ids)!=len(set(ids)):errors.append('Duplicate catalog IDs')
curation=json.loads((root/'curation.json').read_text(encoding='utf-8'))
if curation.get('default_view')!='all':errors.append('Default view must be all')
if not set(curation.get('featured_ids',[])).issubset(ids):errors.append('Unknown featured ID')
upstream={}
for collection in catalog.get('collections',[]):
    folder=root/collection['path']
    manifest=json.loads((folder/'IMPORT.json').read_text(encoding='utf-8'))
    records=json.loads((folder/'data/videos.json').read_text(encoding='utf-8'))
    if len(records)!=manifest['record_count'] or len(records)!=collection['count']:errors.append('Collection count differs')
    if len(list((folder/'prompts').glob('*.md')))!=manifest['prompt_file_count']:errors.append('Prompt count differs')
    for file in manifest['files']:
        target=(folder/file['path']).resolve()
        if not target.is_relative_to(folder.resolve()) or not target.is_file() or hashlib.sha256(target.read_bytes()).hexdigest()!=file['sha256']:errors.append('Snapshot mismatch: '+file['path'])
    upstream.update({'opus-external-'+r['slug']:r for r in records})
for item in catalog['entries']:
    pack=(root/item['path']).resolve()
    if not pack.is_relative_to(root):
        errors.append(item['id']+': path outside library');continue
    if item.get('kind')=='external-reference':
        original=upstream.get(item['id'])
        if not original:errors.append(item['id']+': missing upstream record');continue
        for key,source in [('author','author'),('author_url','author_url'),('original_url','post_url'),('poster_url','poster_url'),('prompt_text','prompt'),('prompt_partial','prompt_partial')]:
            if item.get(key)!=original.get(source):errors.append(item['id']+': changed original '+key)
        target=(pack/item['prompt_file']).resolve()
        if not target.is_relative_to(pack) or not target.is_file():errors.append(item['id']+': missing prompt file')
        if item.get('status')!='imported-unverified':errors.append(item['id']+': invalid external status')
        continue
    for rel in ['style.json','SKILL.md','DESIGN.md','preview.html','references/source-observations.md','examples/index.html']:
        if not (pack/rel).is_file():errors.append(item['id']+': missing '+rel)
    if not (pack/'style.json').exists():continue
    meta=json.loads((pack/'style.json').read_text(encoding='utf-8'))
    for key in ['id','name','media','aliases','status','sources','deliverables']:
        if key not in meta:errors.append(item['id']+': missing metadata '+key)
    for key in ['cover','preview','example','prompt','source_notes']:
        if key not in meta.get('deliverables',{}):errors.append(item['id']+': missing deliverable pointer '+key)
    for key,rel in meta.get('deliverables',{}).items():
        target=(pack/rel.split('#')[0]).resolve()
        if not target.is_relative_to(pack) or not target.is_file():errors.append(item['id']+': invalid deliverable '+key)
    if len(list(pack.rglob('*.srt')))>1:errors.append(item['id']+': more than one final SRT')
    if item.get('sources')!=meta.get('sources') or item.get('deliverables')!=meta.get('deliverables'):
        errors.append(item['id']+': catalog and style.json differ')
for error in errors:print('FAIL:',error)
if not errors:print('PASS:',len(catalog['entries']),'entries; local deliverables, upstream snapshot hashes and curation consistent')
sys.exit(bool(errors))
