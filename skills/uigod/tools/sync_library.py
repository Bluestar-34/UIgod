"""Sync the full repository entry and managed styles, preserving destination-only files."""
from pathlib import Path
import shutil,json,hashlib,uuid
root=Path(__file__).resolve().parents[3]
config_path=root/'sync.local.json'
if not config_path.exists():raise SystemExit('Create ignored sync.local.json using sync.example.json before local sync.')
config=json.loads(config_path.read_text(encoding='utf-8'))
if not all(Path(p).expanduser().is_absolute() for p in config['destinations']):raise SystemExit('Sync destinations must be absolute paths')
destinations=[Path(p).expanduser().resolve() for p in config['destinations']]
for dest in destinations:
    if dest==root or dest.is_relative_to(root) or root.is_relative_to(dest):raise SystemExit('Sync destination overlaps source repository')
    dest.mkdir(parents=True,exist_ok=True)
    for name in ['index.html','SKILL.md','README.md','MOC.md','catalog.json','curation.json','collections','skills','assets','docs','AGENTS.md','CONTRIBUTING.md','editorial.json','taxonomy.json','preferences.example.json','preferences.local.json','sync.example.json']:
        src=root/name
        if src.is_dir():shutil.copytree(src,dest/name,dirs_exist_ok=True,ignore=shutil.ignore_patterns('__pycache__'))
        elif src.exists():shutil.copy2(src,dest/name)
    # Archive only explicitly retired generated files, outside installed skill folders.
    video=(dest/'skills/style-manager/styles/neuroblue-halftone-motion').resolve()
    archive=(Path.home()/'.codex/backups'/('uigod-retired-'+uuid.uuid4().hex[:8])).resolve()
    retired=['preview-desktop.png', 'preview-mobile.png', 'examples/contact-sheet.jpg', 'examples/preview-desktop.png', 'examples/preview-mobile.png', 'examples/frame-2.8s.png', 'examples/frame-4.3s.png', 'examples/frame-6.5s.png', 'examples/frame-7.7s.png', 'examples/frame-9.5s.png', 'references/code-patterns/README.md']
    for rel in retired:
        target=(video/rel).resolve()
        archived=(archive/rel).resolve()
        assert target.is_relative_to(video) and archived.is_relative_to(archive)
        if target.is_file():
            archived.parent.mkdir(parents=True,exist_ok=True)
            shutil.move(str(target),str(archived))
    print('SYNC:',dest)
manifest=Path(config['collection_manifest']) if config.get('collection_manifest') else None
if manifest and manifest.exists():
    data=json.loads(manifest.read_text(encoding='utf-8-sig'))
    for entry in data.get('skills',[]):
        if entry.get('name','').lower()=='uigod':
            entry['source']=str(root)
            entry['installed_locations']=[str(root),*[str(p) for p in destinations]]
            collection=destinations[0]
            entry['files']=[{'path':p.relative_to(collection).as_posix(),'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'bytes':p.stat().st_size} for p in sorted(collection.rglob('*')) if p.is_file() and '__pycache__' not in p.parts]
    manifest.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
