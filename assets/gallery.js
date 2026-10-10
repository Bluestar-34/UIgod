const entries = JSON.parse(document.getElementById('library-data').textContent);
const byId = new Map(entries.map(e => [e.id, e]));
let scope = 'all', filter = 'all', content = 'all', sorting = 'default';
let bookmarks = new Map();
try {
  const saved = JSON.parse(localStorage.getItem('uigod-bookmarks-v1'));
  if (Array.isArray(saved)) {
    for (const item of saved) if (byId.has(item.id)) bookmarks.set(item.id, item.saved_at);
  } else {
    // Old per-browser "精选" becomes a private bookmark list, never public curation.
    const old = JSON.parse(localStorage.getItem('uigod-curation-v1'));
    if (Array.isArray(old)) {
      for (const id of old) if (byId.has(id)) bookmarks.set(id, new Date().toISOString());
      persist();
    }
  }
} catch {}
const cards = document.getElementById('cards'), modal = document.getElementById('modal');
function persist() {
  try { localStorage.setItem('uigod-bookmarks-v1', JSON.stringify([...bookmarks].map(([id,saved_at]) => ({id,saved_at})))); } catch {}
}
function el(tag, cls, text) {
  const node = document.createElement(tag);
  if (cls) node.className = cls;
  if (text) node.textContent = text;
  return node;
}
function openModal(title, node) {
  document.getElementById('modal-title').textContent = title;
  document.getElementById('modal-body').replaceChildren(node);
  modal.showModal();
}
function preview(e) {
  if (e.preview_kind === 'external' || e.preview_kind === 'showcase') { window.open(e.preview, '_blank', 'noopener'); return; }
  if (e.media.includes('video')) {
    const box = el('div'), video = el('video');
    video.controls = true; video.autoplay = true; video.playsInline = true; video.src = e.preview;
    box.append(video, el('p', 'dialog-foot', '迁移样例；验证范围见作品说明。'));
    openModal(e.display_name, box);
  } else window.open(e.preview, '_blank', 'noopener');
}
function showPrompt(e, fallback=false) {
  const box = el('div'), ta = el('textarea'); ta.value = e.prompt; ta.readOnly = true;
  const note = e.kind === 'external-reference' ? (e.prompt_partial ? '上游标注：提示词不完整，尚未逐项验证。' : '上游原始提示词，尚未逐项验证。') : '可复用制作提示词。';
  box.append(ta, el('p','dialog-foot', note + (fallback ? ' 当前浏览器不允许直接复制，请选中文本复制。' : '')));
  openModal(e.display_name, box); if (fallback) ta.select();
}
async function copy(e) {
  try {
    await navigator.clipboard.writeText(e.prompt);
    const toast = document.getElementById('toast'); toast.textContent = '已复制'; toast.classList.add('show');
    setTimeout(() => toast.classList.remove('show'), 2500);
  } catch { showPrompt(e, true); }
}
function compare(a,b) {
  let result = 0;
  if (scope === 'bookmarks') result = (bookmarks.get(b.id)||'').localeCompare(bookmarks.get(a.id)||'');
  else if (scope === 'featured') result = a.featured_rank - b.featured_rank;
  else if (sorting === 'updated') result = Date.parse(b.updated_at)-Date.parse(a.updated_at);
  else result = Number(b.featured)-Number(a.featured) || (a.featured && b.featured ? a.featured_rank-b.featured_rank : Date.parse(b.added_at)-Date.parse(a.added_at));
  return result || a.id.localeCompare(b.id, 'en');
}
function render() {
  const query = document.getElementById('search').value.trim().toLowerCase();
  const shown = entries.filter(e => !e.hidden && (scope==='all' || (scope==='featured' ? e.featured : bookmarks.has(e.id))) && (filter==='all' || e.media.includes(filter)) && (content==='all' || e.content_type===content) && [e.name,e.display_name,e.author||'',e.prompt_text||'',e.summary,...e.aliases,...e.tags].join(' ').toLowerCase().includes(query)).sort(compare);
  document.getElementById('count').textContent = ' / '+shown.length;
  document.getElementById('sort-filter').disabled = scope !== 'all';
  cards.replaceChildren();
  if (!shown.length) { cards.append(el('p','empty',scope==='bookmarks' ? '还没有匹配的收藏。点击作品上的“收藏”即可加入。' : '没有匹配的条目，请调整筛选或搜索。')); return; }
  for (const e of shown) {
    const card = el('article','card'), cover = el('button','cover'); card.dataset.id=e.id;
    cover.setAttribute('aria-label','预览'+e.display_name);
    if (e.cover) {
      const im = el('img'); im.src=e.cover; im.alt=e.display_name+'效果预览'; im.loading='lazy'; im.referrerPolicy='no-referrer';
      im.onerror=()=>{im.remove();cover.prepend(el('span','fallback',e.display_name));}; cover.append(im);
    }
    cover.append(el('span','play',e.preview_kind==='external'?'看原作与复刻':e.preview_kind==='showcase'?'看作品':e.media.includes('video')?'看样片':'看网页'));
    if (e.preview_kind==='showcase') cover.classList.add('original'); cover.onclick=()=>preview(e);
    const meta=el('div','meta');
    meta.append(el('span',e.media.includes('video')?'video':'',e.content_type));
    const state = e.kind==='external-reference' ? (e.prompt_partial?'外部参考 · 部分提示词':'外部参考') : e.status==='sample-verified'?'短样例已验证':e.status==='production-verified'?'完整迁移已验证':'风格包 · 未验证';
    meta.append(el('span','',(e.featured?'精选 · ':'')+state));
    const actions=el('div','actions'), copyBtn=el('button','copy',e.kind==='external-reference'?'复制原提示词':'复制提示词');
    copyBtn.onclick=()=>copy(e); actions.append(copyBtn);
    const design=el('a','',e.kind==='external-reference'?'查看完整记录':'风格说明'); design.href=e.design;
    if (e.kind==='external-reference') {
      const show=el('button','copy','查看提示词'); show.onclick=()=>showPrompt(e); actions.append(show,design);
    } else {
      const demo=el('a','',e.preview_kind==='showcase'?'作品展示':'交互预览'); demo.href=e.path+'/'+(e.deliverables?.preview||'preview.html'); actions.append(design,demo);
    }
    if (e.source_url) {
      const source=el('a','','创作来源'); source.href=e.source_url; source.target='_blank'; source.rel='noopener noreferrer';
      if (e.author) source.title='原作者：@'+e.author; actions.append(source);
    }
    const pick=el('button','copy bookmark',bookmarks.has(e.id)?'取消收藏':'收藏'); pick.setAttribute('aria-pressed',String(bookmarks.has(e.id)));
    pick.onclick=()=>{if(bookmarks.has(e.id))bookmarks.delete(e.id);else bookmarks.set(e.id,new Date().toISOString());persist();render();}; actions.append(pick);
    const title=el('h3','',e.display_name);
    card.append(cover,meta,title);
    if (e.naming_status==='pending') card.append(el('span','pending','待命名'));
    if (e.availability==='broken') card.append(el('span','pending','预览链接待修复'));
    card.append(el('p','summary',e.summary),actions); cards.append(card);
  }
}
document.querySelectorAll('.tab[data-scope]').forEach(button => button.onclick=()=>{
  scope=button.dataset.scope;document.querySelectorAll('.tab[data-scope]').forEach(b=>b.setAttribute('aria-pressed',String(b===button)));render();
});
document.getElementById('export-bookmarks').onclick=()=>{
  const data={version:1,bookmarks:[...bookmarks].map(([id,saved_at])=>({id,saved_at}))};
  const link=document.createElement('a'), url=URL.createObjectURL(new Blob([JSON.stringify(data,null,2)],{type:'application/json'}));
  link.href=url;link.download='bookmarks.json';link.click();setTimeout(()=>URL.revokeObjectURL(url),1000);
};
document.getElementById('media-filter').onchange=e=>{filter=e.target.value;render();};
document.getElementById('content-filter').onchange=e=>{content=e.target.value;render();};
document.getElementById('sort-filter').onchange=e=>{sorting=e.target.value;render();};
document.getElementById('search').oninput=render;
document.querySelector('.close').onclick=()=>modal.close();
modal.addEventListener('close',()=>modal.querySelectorAll('video').forEach(v=>v.pause()));
modal.addEventListener('click',e=>{if(e.target===modal)modal.close();});
render();
