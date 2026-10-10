"""Deterministic catalog compilation. Upstream snapshots and editorial work stay separate."""
from pathlib import Path
from datetime import datetime, timezone
import json, copy

ROOT=Path(__file__).resolve().parents[3]
CONTENT_MAP={'motion':'视觉演示','explainer':'知识讲解','game':'游戏体验','games':'游戏体验'}
EDITORIAL_FIELDS={'display_name','summary','content_type','visual_tags','tech_tags','added_at','updated_at','date_basis','naming_status','availability','hidden','hidden_reason','related_style_id'}

def read(path):
    return json.loads(Path(path).read_text(encoding='utf-8'))

def write(path,data):
    Path(path).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

def compile_catalog(root=ROOT):
    root=Path(root)
    editorial=read(root/'editorial.json')['entries']
    entries=[]
    for path in sorted((root/'skills/style-manager/styles').glob('*/style.json')):
        entry=read(path);entry['kind']='style-package'
        entries.append(entry)
    collections=[]
    for folder in sorted((root/'collections').iterdir()):
        if not (folder/'IMPORT.json').is_file():continue
        manifest=read(folder/'IMPORT.json');records=read(folder/'data/videos.json')
        collection_id=folder.name
        collections.append({'id':collection_id,'path':folder.relative_to(root).as_posix(),'upstream':manifest['upstream'],'commit':manifest['commit'],'count':len(records),'license':(folder/'LICENSE').relative_to(root).as_posix()})
        for v in records:
            slug=v['slug'];eid='opus-external-'+slug
            content=CONTENT_MAP.get(v['category'],'待分类')
            partial=bool(v.get('prompt_partial'));prompt=v.get('prompt') or ''
            entry={'id':eid,'name':content if content!='待分类' else '视频参考','aliases':[slug,'@'+v['author']],
              'media':['video','interactive'] if v['category']=='interactive' else ['video'],
              'content_type':content,'visual_tags':['三维'] if v['category']=='3d' else [],'tech_tags':v.get('tech_tags',[]),
              'path':folder.relative_to(root).as_posix(),'kind':'external-reference','status':'imported-unverified',
              'collection':collection_id,'author':v['author'],'author_url':v['author_url'],'category':v['category'],
              'poster_url':v.get('poster_url',''),'preview_url':v.get('skillry_url') or v['post_url'],'original_url':v['post_url'],
              'prompt_file':'prompts/'+slug+'.md','prompt_text':prompt,'prompt_partial':partial,'naming_status':'pending',
              'summary':'外部视频参考，尚未逐条分析。'+('原提示词不完整。' if partial else '可查看原提示词与来源。'),
              'sources':[{'role':'creative-origin','url':v['post_url'],'provided_by':manifest['upstream'],'verification':'upstream-record-not-individually-reviewed','use_for':['reference','prompt-provenance']}],
              'deliverables':{'prompt':'prompts/'+slug+'.md','source_notes':'IMPORT.json'},'upstream_commit':manifest['commit'],
              'rights':{'metadata_license':'MIT','media_license':'not-specified','prompt_license':'not-specified'}}
            entries.append(entry)
    for entry in entries:
        eid=entry['id']
        if eid not in editorial:raise ValueError('Missing editorial ledger entry: '+eid)
        unknown=set(editorial[eid])-EDITORIAL_FIELDS
        if unknown:raise ValueError('Editorial fields cannot override source data: '+str(unknown))
        entry.update(copy.deepcopy(editorial[eid]))
        entry.setdefault('display_name',entry['name'])
        entry.setdefault('content_type','待分类');entry.setdefault('visual_tags',[]);entry.setdefault('tech_tags',[])
        entry.setdefault('availability','unknown');entry.setdefault('hidden',False)
        entry['tags']=list(dict.fromkeys([entry['content_type'],*entry['visual_tags'],*entry['tech_tags'],*entry.get('tags',[])]))
    return {'version':4,'collections':collections,'entries':entries}

def register_new(root=ROOT):
    """Add missing ledger IDs only; never rewrite existing human edits or dates."""
    root=Path(root);document=read(root/'editorial.json');ledger=document['entries']
    now=datetime.now(timezone.utc).isoformat()
    for path in sorted((root/'skills/style-manager/styles').glob('*/style.json')):
        ledger.setdefault(read(path)['id'],{'added_at':now,'updated_at':now})
    for path in sorted((root/'collections').glob('*/data/videos.json')):
        for v in read(path):ledger.setdefault('opus-external-'+v['slug'],{'added_at':now,'updated_at':now})
    write(root/'editorial.json',document)

def check_source_removals(previous,records):
    removed={v['slug'] for v in previous}-{v['slug'] for v in records}
    if removed:raise ValueError('Upstream removed records; maintainer review required: '+', '.join(sorted(removed)))

def build(root=ROOT):
    result=compile_catalog(root);write(Path(root)/'catalog.json',result);return result
