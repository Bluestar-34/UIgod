"""Sync the full repository entry and managed styles, preserving destination-only files."""
from pathlib import Path
import shutil,json,hashlib,uuid
root=Path(__file__).resolve().parents[3]
collection=Path(r'F:\Obsi-neuroBlue\08_创作\创作Skills\uigod')
claude=Path(r'C:\Users\asus\.claude\skills\uigod')
for dest in [collection,claude]:
    dest.mkdir(parents=True,exist_ok=True)
    for name in ['index.html','SKILL.md','README.md','MOC.md','catalog.json','curation.json','collections','skills']:
        src=root/name
        if src.is_dir():shutil.copytree(src,dest/name,dirs_exist_ok=True,ignore=shutil.ignore_patterns('__pycache__'))
        elif src.exists():shutil.copy2(src,dest/name)
    # Archive only explicitly retired generated files, outside installed skill folders.
    video=(dest/'skills/style-manager/styles/neuroblue-halftone-motion').resolve()
    archive=(Path(r'C:\Users\asus\.codex\backups')/('uigod-retired-'+uuid.uuid4().hex[:8])).resolve()
    retired=['preview-desktop.png', 'preview-mobile.png', 'examples/contact-sheet.jpg', 'examples/preview-desktop.png', 'examples/preview-mobile.png', 'examples/frame-2.8s.png', 'examples/frame-4.3s.png', 'examples/frame-6.5s.png', 'examples/frame-7.7s.png', 'examples/frame-9.5s.png', 'references/code-patterns/README.md']
    for rel in retired:
        target=(video/rel).resolve()
        archived=(archive/rel).resolve()
        assert target.is_relative_to(video) and archived.is_relative_to(archive)
        if target.is_file():
            archived.parent.mkdir(parents=True,exist_ok=True)
            shutil.move(str(target),str(archived))
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
