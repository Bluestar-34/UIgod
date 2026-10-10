"""Build the offline gallery from catalog.json. No server or frontend dependencies."""
from pathlib import Path
import json
from library_data import compile_catalog

ROOT=Path(__file__).resolve().parents[3]
catalog=compile_catalog(ROOT)
entries=catalog['entries']
curation=json.loads((ROOT/'curation.json').read_text(encoding='utf-8'))
featured=set(curation['featured_ids'])
names={
 'hiitmaster-brutal-interval-timer':('机械红黑','高对比数字、硬朗边界与运动计时界面。'),
 'lonely-blue-field-notes':('深夜技术手记','深色编辑版式、衬线标题与信号色。'),
 'namesake-soft-civic-guides':('温暖公共指南','柔和中性色、衬线标题与清晰的信息层级。'),
 'nicchan-pixel-desktop-portfolio':('像素桌面','复古桌面、像素图形与窗口式界面。'),
 'neuroblue-halftone-motion':('网点海报动态','灰度思维母版。巨型黑体、网点主体与语义动效。')}
for i, original in enumerate(entries):
    e=original
    e=dict(e)
    e['featured']=e['id'] in featured
    e['featured_rank']=curation['featured_ids'].index(e['id']) if e['featured'] else 999999
    if e.get('kind')=='external-reference':
        e['display_name']=e.get('display_name',e['name'])
        e['cover']=e.get('poster_url','')
        e['preview']=e['preview_url']
        e['preview_kind']='external'
        e['source_url']=e['original_url']
        e['design']=e['path']+'/'+e['prompt_file']
        e['prompt']=e.get('prompt_text') or '上游未提供完整提示词。请查看原帖：'+e['original_url']
        entries[i]=e
        continue
    if e.get('display_name') and e.get('summary'):pass
    elif e['id'] in names:e['display_name'],e['summary']=names[e['id']]
    else:e['display_name'],e['summary']=e['name'],' / '.join(e.get('tags',[]))
    base=ROOT/e['path']
    deliverables=e.get('deliverables',{})
    image=deliverables.get('cover','examples/frame-0s.png' if 'video' in e['media'] else 'examples/preview.png')
    e['cover']=e['path']+'/'+image if (base/image).exists() else ''
    e['preview']=e['path']+'/'+deliverables.get('video',deliverables.get('example','examples/index.html'))
    if e.get('showcase'):
        e['preview_kind']='showcase'
        e['preview']=e['path']+'/'+deliverables['preview']
    e['source_url']=next((s['url'] for s in e.get('sources',[]) if s.get('role')=='creative-origin' and s.get('url')),'')
    e['design']=e['path']+'/DESIGN.md'
    if 'video' in e['media']:
        e['prompt']='使用 UIgod 的“'+e['name']+'”风格，按工作区最新文案.md 制作视频。先读取该风格包的 SKILL.md、DESIGN.md 和参考帧，保留其排版、材质与动效语言，主体和分镜依新内容设计。需要换色时只替换强调色，保持视觉体系一致。先读取工作区制作要求与本地偏好，明确画幅、时长、声音和工具选择；按约定提交首帧与文案再继续。'
    else:
        e['prompt']='使用 UIgod 的 '+e['id']+' 风格制作我的网页。先读取该风格包的 SKILL.md、DESIGN.md 和参考图，保持其设计语言，根据我的内容重新安排信息结构，不照搬源站文案和品牌。请先检查当前工作区需求再开始。'
    entries[i]=e
data=json.dumps(entries,ensure_ascii=False).replace('<', r'\u003c')
html='''<!doctype html>
<html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>UIgod — 视觉风格与视频提示词库</title>
<style>
@font-face{font-family:LibrarySans;src:url('skills/style-manager/styles/neuroblue-halftone-motion/assets/NotoSansSC-700.ttf');font-weight:700;font-display:swap}
:root{--paper:#eeede7;--ink:#171715;--accent:#e74427;--muted:#74736b;--line:#cfcec5}*{box-sizing:border-box}html{scroll-behavior:smooth}body{margin:0;background:var(--paper);color:var(--ink);font-family:LibrarySans,'Microsoft YaHei',sans-serif;font-weight:700}button,input,a{-webkit-tap-highlight-color:transparent}button,input{font:inherit}a{color:inherit;text-decoration:none}a:hover{text-decoration:underline}button,a,input{outline-offset:5px}header,main,footer{max-width:1440px;margin:auto;padding-left:48px;padding-right:48px}header{height:104px;display:flex;align-items:center;justify-content:space-between;border-bottom:1px solid var(--line)}.brand{font-size:30px;letter-spacing:-1.6px}.brand i{font-style:normal;color:var(--accent)}nav{display:flex;gap:28px;font-size:14px}.hero{display:grid;grid-template-columns:1.1fr 1fr;gap:60px;padding:76px 0 70px;align-items:center}.eyebrow{color:var(--accent);font-size:15px;margin-bottom:22px}h1{font-size:clamp(44px,5.2vw,76px);line-height:1.18;letter-spacing:-3px;margin:0 0 28px}h1 span{color:var(--accent)}.intro{max-width:420px;font-size:17px;line-height:1.85;color:#67665f;margin-bottom:30px}.cta{display:inline-flex;background:var(--ink);color:var(--paper);padding:16px 24px;gap:40px}.feature{background:var(--ink);color:var(--paper);overflow:hidden}.feature img{width:100%;display:block;aspect-ratio:16/9;object-fit:cover;transition:transform .4s}.feature:hover img{transform:scale(1.02)}.feature-label{padding:17px 22px;display:flex;justify-content:space-between;gap:15px;font-size:14px}.feature-label span{color:#a5a49c}.section-head{display:flex;flex-wrap:wrap;justify-content:space-between;gap:24px;align-items:center;padding-top:30px;border-top:1px solid var(--ink)}h2{font-size:30px;letter-spacing:-1px;margin:0}.controls{display:flex;flex-wrap:wrap;gap:12px;align-items:center}.tabs{display:flex;gap:4px}button{cursor:pointer}.tab{border:0;background:transparent;padding:10px 15px;color:#6e6d65}.tab[aria-pressed=true]{color:var(--paper);background:var(--ink)}#media-filter,#content-filter,#sort-filter{font:inherit;font-size:14px;background:transparent;border:1px solid var(--line);padding:11px;color:var(--ink)}#search{border:1px solid var(--line);background:transparent;padding:11px 14px;width:220px;border-radius:0;font-size:14px}.grid{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:42px 26px;padding:32px 0 70px}.card{min-width:0;overflow-wrap:anywhere}.cover{position:relative;display:block;overflow:hidden;background:#d7d6ce;border:1px solid #d1d0c7;aspect-ratio:16/10;width:100%;padding:0}.cover .fallback{position:absolute;inset:0;display:flex;align-items:center;justify-content:center;padding:24px;background:#232320;color:#eeede7;font-size:25px}.cover img{width:100%;height:100%;display:block;object-fit:cover;object-position:top;transition:transform .35s}.cover.original{aspect-ratio:16/9}.cover.original img{object-fit:contain}.cover:hover img{transform:scale(1.035)}.cover .play{position:absolute;right:14px;bottom:14px;background:var(--paper);color:var(--ink);padding:9px 14px;font-size:13px}.meta{display:flex;justify-content:space-between;margin-top:16px;font-size:12px;color:var(--muted)}.meta .video{color:var(--accent)}h3{font-size:23px;margin:8px 0 9px}.pending{display:inline-block;color:var(--muted);font-size:12px;margin-bottom:8px}.summary{font-size:14px;line-height:1.7;color:#737168;margin:0;min-height:48px}.actions{display:flex;flex-wrap:wrap;gap:14px;align-items:center;margin-top:17px;font-size:13px}.copy{border:0;border-bottom:1px solid var(--ink);padding:0 0 3px;background:transparent;color:var(--ink)}.actions a{color:var(--muted)}.empty{grid-column:1/-1;padding:48px 0;color:var(--muted)}.how{background:var(--ink);color:var(--paper);padding:38px;margin-bottom:64px}.how h2{font-size:25px}.steps{display:grid;grid-template-columns:repeat(3,1fr);gap:30px;margin-top:30px}.steps b{color:#ff684b;font-size:20px}.steps p{font-size:14px;line-height:1.8;color:#bab9b1;max-width:300px}.steps strong{color:var(--paper)}footer{padding-top:22px;padding-bottom:32px;border-top:1px solid var(--line);display:flex;gap:20px;justify-content:space-between;font-size:12px;color:var(--muted)}dialog{border:0;padding:0;background:var(--ink);color:var(--paper);width:min(1000px,95vw);max-height:92vh}dialog::backdrop{background:#000b}.dialog-head{padding:18px 22px;display:flex;justify-content:space-between;align-items:center}.close{background:none;border:0;color:var(--paper);font-size:25px}video{width:100%;display:block}textarea{display:block;width:calc(100% - 44px);min-height:190px;margin:0 22px 22px;background:#252522;color:var(--paper);border:1px solid #666;padding:15px;font:15px/1.8 sans-serif}.dialog-foot{padding:0 22px 22px;color:#aaa;font-size:13px}#toast{position:fixed;bottom:26px;left:50%;transform:translateX(-50%);padding:13px 24px;background:var(--ink);color:var(--paper);font-size:14px;opacity:0;pointer-events:none;transition:opacity .2s}#toast.show{opacity:1}@media(max-width:1000px){header,main,footer{padding-left:28px;padding-right:28px}.hero{gap:30px}.grid{grid-template-columns:repeat(2,minmax(0,1fr))}.section-head{align-items:flex-start;flex-direction:column}.controls{width:100%;justify-content:space-between}}@media(max-width:620px){header,main,footer{padding-left:20px;padding-right:20px}header{height:80px}nav{gap:16px;font-size:12px}.hero{grid-template-columns:1fr;padding:40px 0;gap:32px}h1{letter-spacing:-2px}.intro{font-size:15px}.grid{grid-template-columns:1fr;gap:34px;padding-bottom:42px}.controls{align-items:stretch;flex-direction:column}#search{width:100%}.steps{grid-template-columns:1fr;gap:10px}.how{padding:25px;margin-bottom:40px}.pending{display:inline-block;color:var(--muted);font-size:12px;margin-bottom:8px}.summary{min-height:0}footer{flex-direction:column}h2{font-size:26px}}@media(prefers-reduced-motion:reduce){*{scroll-behavior:auto!important;transition:none!important}}
</style></head><body>
<header><a class="brand" href="#">UIgod<i>.</i></a><nav><a href="#library">风格库</a><a href="#how">开始制作</a><a href="README.md">使用说明</a></nav></header>
<main><section class="hero"><div><div class="eyebrow">视觉风格与视频提示词库</div><h1>选一种风格。<br>做出<span>你的作品。</span></h1><p class="intro">从真实作品里沉淀视觉语言。先看效果，再选风格，把提示词交给 Claude，带上自己的内容开始制作。</p><a class="cta" href="#library">进入风格库</a></div><a class="feature" href="skills/style-manager/styles/neuroblue-halftone-motion/showcase.html"><img src="skills/style-manager/styles/neuroblue-halftone-motion/references/showcase-v2/frame-14-at-124s.png" alt="灰度思维 v2 原作尾帧：看得见灰色与网点球体"><div class="feature-label"><strong>灰度思维 · 黑白网点与朱红重音</strong><span>查看作品</span></div></a></section>
<section id="library"><div class="section-head"><h2>选择你的视觉语言 <span id="count"></span></h2><div class="controls"><div class="tabs" aria-label="浏览范围"><button class="tab" data-scope="all" aria-pressed="true">全部</button><button class="tab" data-scope="featured" aria-pressed="false">精选</button><button class="tab" data-scope="bookmarks" aria-pressed="false">收藏</button></div><select id="media-filter" aria-label="筛选媒介"><option value="all">所有类型</option><option value="video">视频</option><option value="web">网页</option><option value="image">图片</option><option value="interactive">交互</option></select><select id="content-filter" aria-label="筛选内容"><option value="all">所有内容</option>__CONTENT_OPTIONS__</select><select id="sort-filter" aria-label="排序"><option value="default">精选优先 · 最近收录</option><option value="updated">最近更新</option></select><button class="tab" id="export-bookmarks">导出收藏</button><input id="search" type="search" placeholder="搜索名称、网点、海报…" aria-label="搜索风格"></div></div><div class="grid" id="cards"></div></section>
<section class="how" id="how"><h2>从风格到作品，三步开始。</h2><div class="steps"><div><b>01 / 看效果</b><p>全部默认显示所有条目；精选由维护者管理；收藏仅保存在当前浏览器。<strong>外部参考保留作者与原帖。</strong></p></div><div><b>02 / 拿提示词</b><p>复制风格卡片的提示词，换成自己的主题、文案和强调色。</p></div><div><b>03 / 交给 Claude</b><p>在制作工作区发送提示词。视频先看实际首帧，确认后继续全片。</p></div></div></section></main>
<footer><span>UIgod / 视觉风格档案</span><span><a href="catalog.json">风格目录</a> · <a href="SKILL.md">AI 入口</a> · <a href="skills/uigod/docs/VIDEO-CONTRACT.md">收录规范</a></span></footer>
<dialog id="modal"><div class="dialog-head"><strong id="modal-title"></strong><button class="close" aria-label="关闭">×</button></div><div id="modal-body"></div></dialog><div id="toast" role="status" aria-live="polite"></div>
<script id="library-data" type="application/json">__DATA__</script>
<script src="assets/gallery.js"></script></body></html>'''
taxonomy=json.loads((ROOT/'taxonomy.json').read_text(encoding='utf-8'))
options=''.join('<option>'+x+'</option>' for x in taxonomy['content_types'])
(ROOT/'index.html').write_text(html.replace('__DATA__',data).replace('__CONTENT_OPTIONS__',options),encoding='utf-8')
print('Gallery built:',ROOT/'index.html')
