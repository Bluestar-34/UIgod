"""Import every upstream prompt and record, preserving creator attribution.
Usage: python skills/uigod/tools/import_opus_videos.py [local-upstream-checkout]
No remote media is copied; preview and original links remain attached to each record.
"""
from pathlib import Path
import sys,json,subprocess,shutil,tempfile,hashlib
from datetime import datetime
from zoneinfo import ZoneInfo
from library_data import read, write, check_source_removals

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
dest=ROOT/'collections/awesome-opus5-5-videos'
previous=read(dest/'data/videos.json') if (dest/'data/videos.json').exists() else []
check_source_removals(previous,records)
previous_map={v['slug']:v for v in previous}
previous_prompts={v['slug']:(dest/'prompts'/(v['slug']+'.md')).read_bytes() for v in previous if (dest/'prompts'/(v['slug']+'.md')).is_file()}
assert all((source/'prompts'/(v['slug']+'.md')).is_file() for v in records),'Missing upstream prompt file'
dest.mkdir(parents=True,exist_ok=True)
for name in ['README.md','LICENSE','data','prompts']:
    src=source/name
    if src.is_dir():shutil.copytree(src,dest/name,dirs_exist_ok=True)
    else:shutil.copy2(src,dest/name)
prompts=list((source/'prompts').glob('*.md'))
for record in records:assert (dest/'prompts'/(record['slug']+'.md')).is_file(),record['slug']
manifest={'upstream':UPSTREAM,'commit':commit,'imported_at':datetime.now(ZoneInfo('Asia/Shanghai')).isoformat(),'record_count':len(records),'prompt_file_count':len(prompts),'media_policy':'保留上游海报、预览与原帖链接，不镜像远程音视频；素材归原作者。','files':[{'path':p.relative_to(source).as_posix(),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for name in ['README.md','LICENSE','data','prompts'] for p in ([source/name] if (source/name).is_file() else sorted((source/name).rglob('*'))) if p.is_file()]}
(dest/'IMPORT.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
from library_data import register_new, build
register_new(ROOT)
editorial=read(ROOT/'editorial.json')
for record in records:
    if record['slug'] in previous_map and (record!=previous_map[record['slug']] or previous_prompts.get(record['slug'])!=(source/'prompts'/(record['slug']+'.md')).read_bytes()):
        editorial['entries']['opus-external-'+record['slug']]['updated_at']=manifest['imported_at']
write(ROOT/'editorial.json',editorial)
build(ROOT)
print(f'Imported {len(records)} records and {len(prompts)} prompt files; commit {commit[:12]}')
if owned:owned.cleanup()
