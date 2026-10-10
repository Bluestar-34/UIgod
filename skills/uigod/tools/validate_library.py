"""Check shared work metadata and final deliverables without guessing filenames."""
from pathlib import Path
import json,sys,hashlib
from datetime import datetime
from library_data import compile_catalog,read,EDITORIAL_FIELDS

root=Path(__file__).resolve().parents[3]
errors=[]
catalog=json.loads((root/'catalog.json').read_text(encoding='utf-8'))
taxonomy=read(root/'taxonomy.json')
editorial=read(root/'editorial.json')['entries']
try:
    if catalog!=compile_catalog(root):errors.append('catalog.json is stale; run build_catalog.py')
except (ValueError,KeyError) as exc:errors.append(str(exc))
ids=[e['id'] for e in catalog['entries']]
if len(ids)!=len(set(ids)):errors.append('Duplicate catalog IDs')
curation=json.loads((root/'curation.json').read_text(encoding='utf-8'))
if curation.get('default_view')!='all':errors.append('Default view must be all')
if not set(curation.get('featured_ids',[])).issubset(ids):errors.append('Unknown featured ID')
if len(curation['featured_ids'])!=len(set(curation['featured_ids'])):errors.append('Duplicate featured ID')
if curation.get('selected_by')!='maintainer':errors.append('Public curation must belong to maintainer')
for eid,fields in editorial.items():
    if set(fields)-EDITORIAL_FIELDS:errors.append(eid+': forbidden editorial fields')
    if eid not in ids:errors.append(eid+': orphan editorial record; source removal needs review')
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
    eid=item['id']
    for field in ['content_type','media','visual_tags','tech_tags','added_at','updated_at','naming_status','availability','sources','deliverables']:
        if field not in item:errors.append(eid+': missing '+field)
    if item.get('content_type') not in taxonomy['content_types']:errors.append(eid+': invalid content type')
    if not set(item.get('media',[])).issubset(taxonomy['media']):errors.append(eid+': invalid media')
    if not set(item.get('visual_tags',[])).issubset(taxonomy['visual_tags']):errors.append(eid+': unknown visual tag')
    if item.get('naming_status') not in taxonomy['naming_status']:errors.append(eid+': invalid naming status')
    if item.get('availability') not in taxonomy['availability']:errors.append(eid+': invalid availability')
    for key in ['added_at','updated_at']:
        try:
            value=datetime.fromisoformat(item[key])
            if value.tzinfo is None:raise ValueError('Timezone required')
        except (KeyError,ValueError):errors.append(eid+': invalid timestamp '+key)
    if item.get('hidden') and not item.get('hidden_reason'):errors.append(eid+': hidden without reason')
    if item.get('hidden') and eid in curation['featured_ids']:errors.append(eid+': hidden entry cannot be featured')
    if item.get('related_style_id') and item['related_style_id'] not in {e['id'] for e in catalog['entries'] if e.get('kind')=='style-package'}:errors.append(eid+': invalid related style')
    if not item.get('display_name') or '@' in item['display_name']:errors.append(eid+': invalid display title')
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
    required=['style.json','SKILL.md','DESIGN.md','references/source-observations.md']
    if item.get('status') in ['sample-verified','production-verified']:required.append('examples/index.html')
    for rel in required:
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
