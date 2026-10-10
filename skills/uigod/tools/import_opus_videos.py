"""Import every upstream prompt and record, preserving creator attribution.
Usage: python skills/uigod/tools/import_opus_videos.py [local-upstream-checkout]
No remote media is copied; preview and original links remain attached to each record.
"""
from pathlib import Path
import sys,json,subprocess,shutil,tempfile,hashlib
from datetime import datetime
from zoneinfo import ZoneInfo

ROOT=Path(__file__).resolve().parents[3]
UPSTREAM='https://github.com/yihui-dev/awesome-opus5-5-videos'
owned=None
if len(sys.argv)>1:source=Path(sys.argv[1]).resolve()
else:
    owned=tempfile.TemporaryDirectory(prefix='uigod-opus-import-')
    source=Path(owned.name)/'upstream'
    subprocess.run(['git','clone','--depth','1',UPSTREAM+'.git',str(source)],check=True)
commit=subprocess.check_output(['git','rev-parse','HEAD'],cwd=source,text=True).strip()
records=json.loads((source/'data/videos.json').read_text(encoding='utf-8'))
assert len({v['slug'] for v in records})==len(records),'Duplicate upstream slugs'
dest=ROOT/'collections/awesome-opus5-5-videos';dest.mkdir(parents=True,exist_ok=True)
for name in ['README.md','LICENSE','data','prompts']:
    src=source/name
    if src.is_dir():shutil.copytree(src,dest/name,dirs_exist_ok=True)
    else:shutil.copy2(src,dest/name)
prompts=list((source/'prompts').glob('*.md'))
for record in records:assert (dest/'prompts'/(record['slug']+'.md')).is_file(),record['slug']
manifest={'upstream':UPSTREAM,'commit':commit,'imported_at':datetime.now(ZoneInfo('Asia/Shanghai')).isoformat(),'record_count':len(records),'prompt_file_count':len(prompts),'media_policy':'保留上游海报、预览与原帖链接，不镜像远程音视频；素材归原作者。','files':[{'path':p.relative_to(source).as_posix(),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for name in ['README.md','LICENSE','data','prompts'] for p in ([source/name] if (source/name).is_file() else sorted((source/name).rglob('*'))) if p.is_file()]}
(dest/'IMPORT.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
catalog_path=ROOT/'catalog.json';cat=json.loads(catalog_path.read_text(encoding='utf-8'))
existing={e['id']:e for e in cat['entries']}
categories={'motion':'动态设计','explainer':'知识讲解','3d':'三维场景','game':'游戏与交互','interactive':'游戏与交互','games':'游戏与交互'}
for v in records:
    slug=v['slug'];id='opus-external-'+slug
    partial=bool(v.get('prompt_partial'));prompt=v.get('prompt') or ''
    label=categories.get(v['category'],v['category'])
    existing[id]={'id':id,'name':label,'aliases':[slug,'@'+v['author']],'media':['video'],'tags':[label,v['category'],*v.get('tech_tags',[])],'path':'collections/awesome-opus5-5-videos','kind':'external-reference','status':'imported-unverified','collection':'awesome-opus5-5-videos','author':v['author'],'author_url':v['author_url'],'category':v['category'],'poster_url':v.get('poster_url',''),'preview_url':v.get('skillry_url') or v['post_url'],'original_url':v['post_url'],'prompt_file':'prompts/'+slug+'.md','prompt_text':prompt,'prompt_partial':partial,'summary':('原提示词不完整。' if partial else '')+(prompt[:110].replace('\n',' ') if prompt else '上游未提供完整提示词，保留原帖供查看。'),'sources':[{'role':'creative-origin','url':v['post_url'],'provided_by':UPSTREAM,'verification':'upstream-record-not-individually-reviewed','use_for':['reference','prompt-provenance']}],'deliverables':{'prompt':'prompts/'+slug+'.md','source_notes':'IMPORT.json'},'upstream_commit':commit}
cat['entries']=list(existing.values());cat['version']=3
cat['collections']=[{'id':'awesome-opus5-5-videos','path':'collections/awesome-opus5-5-videos','upstream':UPSTREAM,'commit':commit,'count':len(records),'license':'collections/awesome-opus5-5-videos/LICENSE'}]
catalog_path.write_text(json.dumps(cat,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
curation=ROOT/'curation.json'
if not curation.exists():curation.write_text(json.dumps({'default_view':'all','selected_by':'user','featured_ids':['neuroblue-halftone-motion'],'notes':'精选只由用户明确挑选；上游 highlighted 不等于用户精选。'},ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(f'Imported {len(records)} records and {len(prompts)} prompt files; commit {commit[:12]}')
if owned:owned.cleanup()
