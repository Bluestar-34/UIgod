"""Sync the full repository entry and managed styles, preserving destination-only files."""
from pathlib import Path
import shutil,json,hashlib
root=Path(__file__).resolve().parents[3]
collection=Path(r'F:\Obsi-neuroBlue\08_创作\创作Skills\uigod')
claude=Path(r'C:\Users\asus\.claude\skills\uigod')
for dest in [collection,claude]:
    dest.mkdir(parents=True,exist_ok=True)
    for name in ['index.html','SKILL.md','README.md','MOC.md','catalog.json','skills']:
        src=root/name
        if src.is_dir():shutil.copytree(src,dest/name,dirs_exist_ok=True,ignore=shutil.ignore_patterns('__pycache__'))
        elif src.exists():shutil.copy2(src,dest/name)
    print('SYNC:',dest)
manifest=collection.parent/'来源清单.json'
if manifest.exists():
    data=json.loads(manifest.read_text(encoding='utf-8-sig'))
    for entry in data.get('skills',[]):
        if entry.get('name','').lower()=='uigod':
            entry['source']=str(root)
            entry['installed_locations']=[str(root),str(claude)]
            entry['files']=[{'path':p.relative_to(collection).as_posix(),'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'bytes':p.stat().st_size} for p in sorted(collection.rglob('*')) if p.is_file() and '__pycache__' not in p.parts]
    manifest.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
