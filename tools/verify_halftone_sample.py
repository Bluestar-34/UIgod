from pathlib import Path
import subprocess,json,base64,hashlib
from playwright.sync_api import sync_playwright
from PIL import Image,ImageDraw

root=Path(__file__).resolve().parents[1]
pack=root/'skills/neuroblue-halftone-motion'
out=pack/'examples'
with sync_playwright() as pw:
    browser=pw.chromium.launch(headless=True)
    page=browser.new_page(viewport={'width':1440,'height':1100},device_scale_factor=1)
    errors=[];page.on('pageerror',lambda e:errors.append(str(e)))
    page.goto((pack/'preview.html').as_uri()+'?mode=transfer')
    page.evaluate('window.ready')
    assert page.evaluate('document.fonts.check("700 114px StyleSans")')
    # Same t after arbitrary seeks must generate identical pixels.
    hashes=[]
    for t in [2,8,0,2]:
        page.evaluate('(t)=>renderFrame(t)',t)
        raw=page.evaluate('canvas.toDataURL("image/png")')
        if t==2:hashes.append(hashlib.sha256(raw.encode()).hexdigest())
    assert hashes[0]==hashes[1], 'nondeterministic seek'
    sheet=Image.new('RGB',(1280,3*384),'#222');d=ImageDraw.Draw(sheet)
    for i,t in enumerate([0,2.8,4.3,6.5,7.7,9.5]):
        page.evaluate('(t)=>renderFrame(t)',t)
        data=base64.b64decode(page.evaluate('canvas.toDataURL("image/png").split(",")[1]'))
        p=out/f'frame-{t:g}s.png';p.write_bytes(data)
        im=Image.open(p).resize((640,360));x=(i%2)*640;y=(i//2)*384;sheet.paste(im,(x,y+24));d.text((x+10,y+6),f'{t:g}s',fill='white')
    sheet.save(out/'contact-sheet.jpg',quality=92)
    page.evaluate('renderFrame(0)')
    page.screenshot(path=str(out/'preview-desktop.png'))
    page.set_viewport_size({'width':390,'height':844})
    assert page.evaluate('document.documentElement.scrollWidth <= innerWidth'), 'mobile overflow'
    page.screenshot(path=str(out/'preview-mobile.png'),full_page=True)
    page.goto((out/'index.html').as_uri())
    frame=page.frames[1];frame.evaluate('window.ready')
    assert frame.evaluate('mode')=='transfer'
    page.goto((pack/'preview.html').as_uri())
    page.evaluate('window.ready');page.evaluate('renderFrame(0)')
    page.screenshot(path=str(pack/'preview-mobile.png'),full_page=True)
    page.set_viewport_size({'width':1440,'height':1100})
    page.screenshot(path=str(pack/'preview-desktop.png'))
    page.goto((pack/'preview.html').as_uri()+'?mode=transfer');page.evaluate('window.ready')
    fps=24
    proc=subprocess.Popen(['ffmpeg','-v','error','-y','-f','image2pipe','-framerate',str(fps),'-vcodec','png','-i','pipe:0','-an','-c:v','libx264','-preset','veryfast','-crf','20','-pix_fmt','yuv420p','-movflags','+faststart',str(out/'transfer.mp4')],stdin=subprocess.PIPE)
    try:
        for i in range(10*fps):
            page.evaluate('(t)=>renderFrame(t)',i/fps)
            data=page.evaluate('canvas.toDataURL("image/png").split(",")[1]')
            proc.stdin.write(base64.b64decode(data))
            if i%48==0:print('render:',i,'/',240,flush=True)
    finally:proc.stdin.close()
    assert proc.wait()==0
    assert not errors,errors
    browser.close()
subprocess.run(['ffmpeg','-v','error','-xerror','-i',str(out/'transfer.mp4'),'-f','null','-'],check=True)
info=json.loads(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration:stream=codec_name,width,height,r_frame_rate','-of','json',str(out/'transfer.mp4')],text=True,encoding='utf-8'))
result={'status':'awaiting-visual-review','visual_review':False,'decode_pass':True,'browser_errors':errors,'font_loaded':True,'deterministic_seek':True,'mobile_no_horizontal_overflow':True,'example_iframe_loaded':True,'media':info,'limitations':['纯视觉10秒示例，无配音和音乐','浏览器移动端等比显示，不等于竖屏成片已验证','不是用户确认的正式视频']}
(out/'verification.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('VERIFY: render, decode, font, seek and viewport checks passed')
