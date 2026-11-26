"""킬러들의 수학몰 화면(src/killer_template.html)을 그대로 쓰고, 루키용으로 바꿀 곳만 고친다 → template.html
킬러 화면이 바뀌면: 킬러 저장소의 template.html 을 src/killer_template.html 로 복사한 뒤 이 스크립트를 다시 돌리면 된다.
(고칠 곳을 찾지 못하면 멈춘다 → 그 자리만 손보면 됨)"""
import os, re, sys, json
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
s = open(os.path.join(ROOT, 'src', 'killer_template.html'), encoding='utf-8').read()


def rep(old, new, count=1):
    global s
    n = s.count(old)
    if n != count:
        sys.exit(f'[patch] {n}번 발견 (기대 {count}): {old[:90]!r}')
    s = s.replace(old, new)


# ── 이름·표기 ──
s = s.replace('킬러들의 수학몰', '루키들의 수학몰').replace("KILLERS' MATH MALL", "ROOKIES' MATH MALL")
rep("const KEY='km:v2';", "const KEY='rk:v2';")
# 로고만 초록 (나머지 색·배치는 킬러와 같게)
# 밝은 화면: 배치는 킬러와 같게 두고, 전체 밝기를 뒤집은 뒤(invert + hue-rotate) 문제지·그림만 원래대로 되돌린다.
# 뒤집기 전 색을 미리 골라 두면 뒤집힌 결과가 루키 색이 된다: 배경 크림 #fffaf0, 카드 흰색, 강조 새싹 초록 #1f9d55
PRE = {'#e50914': '#24a25a', '#141414': '#090400', '#1b1b1b': '#050200', '#181818': '#050200', '#1f1f1f': '#000000',
       '#2b2b2b': '#120d02', '#2a2a2a': '#1a1408', '#262626': '#1a1408', '#2c2c2c': '#1a1408', '#333': '#281f0b'}
for a, b in PRE.items():
    s = re.sub(re.escape(a) + r'(?![0-9a-fA-F])', b, s)
s = s.replace('rgba(229,9,20,', 'rgba(36,162,90,')

def pre(hexc):
    """뒤집힌 화면에서 hexc 로 보이게 하려면 뒤집기 전에 넣을 색 (invert + hue-rotate(180deg) 의 역)"""
    H = [[-0.574, 1.43, 0.144], [0.426, 0.43, 0.144], [0.426, 1.43, -0.856]]
    d = (H[0][0]*(H[1][1]*H[2][2]-H[1][2]*H[2][1]) - H[0][1]*(H[1][0]*H[2][2]-H[1][2]*H[2][0]) + H[0][2]*(H[1][0]*H[2][1]-H[1][1]*H[2][0]))
    inv = [[(H[(j+1)%3][(i+1)%3]*H[(j+2)%3][(i+2)%3]-H[(j+1)%3][(i+2)%3]*H[(j+2)%3][(i+1)%3])/d for j in range(3)] for i in range(3)]
    f = [int(hexc[k:k+2], 16)/255 for k in (1, 3, 5)]
    pv = [min(1, max(0, 1 - sum(inv[r][c]*f[c] for c in range(3)))) for r in range(3)]
    return '#' + ''.join(f'{round(v*255):02x}' for v in pv)

# 단원·과목별 색 (보이는 색 → 뒤집기 전 색)
UNIT_COL = {'중학 복습': '#f59e0b', '다항식': '#10b981', '복소수·이차방정식': '#8b5cf6', '이차함수': '#f97316', '여러 방정식·부등식': '#06b6d4',
            '도형의 방정식': '#3b82f6', '집합과 명제': '#ec4899', '함수': '#14b8a6', '경우의 수·확률·수열': '#84cc16', '기타': '#94a3b8',
            '공통': '#10b981', '확률과 통계': '#f97316', '미적분': '#3b82f6', '기하': '#8b5cf6',
            # 평가원 기출 단원
            '지수·로그': '#f59e0b', '삼각함수': '#ec4899', '수열': '#8b5cf6', '함수의 극한': '#06b6d4', '미분': '#3b82f6', '적분': '#10b981',
            '경우의 수': '#f97316', '확률': '#d946ef', '통계': '#84cc16', '수열의 극한': '#6366f1', '미분법': '#0ea5e9', '적분법': '#14b8a6',
            '이차곡선': '#a855f7', '평면벡터': '#f43f5e', '공간도형': '#0891b2'}

LIGHT = """<style id="rookieLight">
html{filter:invert(1) hue-rotate(180deg);background:#090400}
img,video,iframe,canvas,.sheet,.art .paper,#fullSheet,#lb,#gBtn{filter:invert(1) hue-rotate(180deg)}
.sheet img,.art .paper img,#fullSheet img,#fullSheet .sheet,#lb img{filter:none}
.result.no{background:rgba(255,129,129,.16)!important;border-color:#ff8181!important}.st.no{background:#ff8181!important;color:#000!important}   /* 오답은 빨강 유지 */
.btn:not(.ghost),.hero .go,.cta:not(.ghostc),#auth .abtn:not(.ghost):not(.danger),.stage.on,#fsGrade,#fsDone{color:#000!important}
#fullSheet .btn,#fullSheet #fsGrade,#fullSheet #fsDone{color:#fff!important}   /* 초록 위 글자는 흰색으로 보이게 */
"""+f"""
/* ── 컬러풀 ── */
.hero::after{{background:linear-gradient(120deg,{pre('#e3f8ec')}ee,{pre('#e1f0ff')}dd 40%,{pre('#fff3d6')}dd 70%,{pre('#f6e6ff')}ee)!important}}
.mosaic{{opacity:.45}}
.hero h1 em{{color:{pre('#16a34a')}}}
.topbar{{border-bottom:2px solid transparent;border-image:linear-gradient(90deg,{pre('#22c55e')},{pre('#06b6d4')},{pre('#3b82f6')},{pre('#a855f7')},{pre('#f97316')}) 1}}
#tabs button{{background:transparent!important;border:0!important;border-radius:0!important;opacity:1!important;color:{pre('#6b7280')}!important;padding:10px 14px!important;font-size:.98rem!important}}
#tabs button.on{{color:{pre('#111827')}!important;font-weight:700!important}}
#tabs button[data-tab="g1"].on{{box-shadow:inset 0 -3px 0 {pre('#16a34a')}}}
#tabs button[data-tab="past"].on{{box-shadow:inset 0 -3px 0 {pre('#2563eb')}}}
#tabs button .n{{font-weight:500}}
#tabs button:focus{{outline:none}}#tabs button:focus-visible{{outline:2px solid {pre('#93c5fd')};outline-offset:2px}}
.stats .tile:nth-child(1){{background:linear-gradient(160deg,{pre('#dcfce7')},{pre('#ffffff')});border-color:{pre('#86efac')};--tc:{pre('#22c55e')}}}
.stats .tile:nth-child(2){{background:linear-gradient(160deg,{pre('#dbeafe')},{pre('#ffffff')});border-color:{pre('#93c5fd')};--tc:{pre('#3b82f6')}}}
.stats .tile:nth-child(3){{background:linear-gradient(160deg,{pre('#fef3c7')},{pre('#ffffff')});border-color:{pre('#fcd34d')};--tc:{pre('#f59e0b')}}}
.ghead::before{{content:"";width:6px;height:1.1em;border-radius:3px;background:linear-gradient(180deg,{pre('#22c55e')},{pre('#3b82f6')})}}
.card .dbadge{{background:var(--dc)!important;color:#000!important}}
/* 유사문항 */
.simq{{background:{pre('#ffffff')};border:1px solid {pre('#e7e1d3')};border-radius:12px;padding:18px 20px 12px;margin:14px 0 6px;box-shadow:0 1px 3px rgba(0,0,0,.12)}}
.simq .entext{{font-size:1.04rem;line-height:1.95;font-weight:400;color:{pre('#2f3640')};-webkit-font-smoothing:antialiased}}
.simq .entext p{{font-weight:400!important;margin:0 0 .9em}}
.simq .entext b{{font-weight:600}}
.simq .entext .choices{{display:grid;grid-template-columns:repeat(auto-fill,minmax(128px,1fr));gap:.55em 1.2em;margin:1em 0 .4em;padding-top:.8em;border-top:1px dashed {pre('#e7e1d3')}}}
.simq .entext .choices span{{white-space:nowrap}}
.simq .entext .box{{background:{pre('#fbf8f0')}}}
.simansin{{margin:18px 0 6px!important;padding:14px 16px;border-radius:12px;background:{pre('#f3f8f4')};border:1px solid {pre('#d5e9da')};justify-content:flex-start!important;row-gap:10px}}
.simansin .al{{width:100%;font-size:.86rem;font-weight:600;color:{pre('#15803d')}}}
.simansin+div .result{{margin-top:10px}}
/* 5지선다 번호 버튼 */
.chpad{{display:flex;gap:8px;flex-wrap:wrap}}
.chb{{width:50px;height:50px;border-radius:50%;font-size:1.45rem;line-height:1;cursor:pointer;font-family:inherit;border:2px solid {pre('#d6d0c2')};background:{pre('#ffffff')};color:{pre('#1f2937')};transition:transform .08s}}
.chb:hover{{border-color:{pre('#16a34a')}}}.chb:active{{transform:scale(.94)}}
.chb.on{{background:{pre('#16a34a')};border-color:{pre('#16a34a')};color:{pre('#ffffff')}}}
#fullSheet .chb{{border-color:#d6d0c2;background:#fff;color:#1f2937}}#fullSheet .chb:hover{{border-color:#16a34a}}
#fullSheet .chb.on{{background:#16a34a;border-color:#16a34a;color:#fff}}
.ansin .chpad~input{{display:none}}
/* 진행 방식 칩: 킬러와 같은 모양(진한 테두리 알약 + 같은 색 글자) */
#flowPast{{gap:7px}}
#flowPast span{{font-weight:700!important;font-size:.9rem;padding:4px 13px;border-radius:999px;border:1.5px solid var(--fc);color:var(--fc);background:var(--fb)}}
#flowPast .f1{{--fc:{pre('#dc2626')};--fb:{pre('#fde8e8')}}}
#flowPast .f2{{--fc:{pre('#2563eb')};--fb:{pre('#e3ecfd')}}}
#flowPast .f3{{--fc:{pre('#b7791f')};--fb:{pre('#fdf3dc')}}}
#flowPast .f4{{--fc:{pre('#15803d')};--fb:{pre('#e2f6e8')}}}
#flowPast .f5{{--fc:{pre('#db2777')};--fb:{pre('#fde7f1')}}}
/* 로고 */
.logo{{color:{pre('#1c2d47')}!important;text-shadow:none!important;font-weight:800!important;font-size:1.32rem!important;letter-spacing:-.03em!important;position:relative;padding-left:44px}}
.logo em{{font-style:normal;color:{pre('#5cb531')}}}
.logo .rkico{{position:absolute;left:0;top:-3px;width:36px;height:36px}}
.logo small{{font-weight:500!important;font-size:.52rem!important;letter-spacing:.22em!important;margin-top:4px!important}}
.logo .meta{{background:transparent!important;border:1px solid {pre('#e5e7eb')}!important;padding:3px 9px!important;font-size:.72rem}}
.logo .meta b{{font-weight:600!important}}
/* 카드 미리보기: 문제 첫 줄부터 읽히게 + 형광펜 */
.snap .paper{{top:34px!important;height:58%!important}}
.snap .paper img{{width:135%!important;margin:0 0 0 -2px!important}}
.snap .paper::before{{background:var(--hl)!important}}
.snap .paper:has(img)::after{{content:"";position:absolute;left:4px;top:11px;width:74%;height:11px;border-radius:3px;background:color-mix(in srgb,var(--hl) 38%,transparent);mix-blend-mode:multiply;transform:rotate(-.6deg)}}
.snap .paper:has(img) img+*{{display:none}}
/* 굵은 글씨 줄이기 */
.card .topic{{font-weight:600!important;font-size:.98rem!important;text-shadow:0 1px 6px rgba(0,0,0,.9)!important}}
.card .top,.card .top .num,.chip,.flow span,.tile .lbl,.dbadge,.tag,#tabs button,select{{font-weight:500!important}}
.tile .big{{font-weight:800!important}}
.ghead{{font-weight:700!important}}
.btn,.cta,.hero .go{{font-weight:600!important}}
</style>
"""
s = s.replace('<style>/*__KATEX_CSS__*/</style>', '<style>/*__KATEX_CSS__*/</style>\n' + LIGHT, 1)

RKSVG = '<img class="rkico" src="/icon-192.png" alt="">'
# ── 5지선다: 번호 버튼을 눌러 고르기 / 단답형: 숫자만 입력 ──
rep("const ai=el('div','ansin');ai.hidden=true;const inp=el('input');inp.type='number';inp.min=1;inp.max=999;inp.id='answer';inp.placeholder=J.choice?'번호 1~5':'정답';const gb=el('button','btn','채점');ai.append(el('span',null,'내 답'),inp,gb);if(auto)b.append(ai);",
    "const ai=el('div','ansin');ai.hidden=true;const inp=el('input');inp.type='text';inp.inputMode='numeric';inp.pattern='[0-9]*';inp.maxLength=3;inp.oninput=()=>{inp.value=inp.value.replace(/[^0-9]/g,'')};inp.id='answer';inp.placeholder=J.choice?'번호 1~5':'숫자 입력';const gb=el('button','btn','채점');ai.append(el('span',null,'내 답'),inp,gb);if(J.choice)choicePad(ai,inp);if(auto)b.append(ai);")
rep("'답은 ①~⑤ 중 번호(1~5)를 입력하세요.':'답은 자연수를 입력하세요.'", "'답은 ①~⑤ 중 하나를 눌러 고른 뒤 채점을 누르세요.':'답은 숫자로 입력하세요.'")
rep("if(window.innerWidth<=900)$('#fullBtn').click();else if(auto)inp.focus()};", "if(window.innerWidth<=900)$('#fullBtn').click();else if(auto&&!J.choice)inp.focus()};", 2)
rep("const grade=()=>{if(inp.value==='')return;", "const grade=()=>{if(inp.value===''){toast(J&&J.choice?'번호를 먼저 고르세요':'답을 입력하세요');return}", 4)
rep("$('#fsAns').value='';$('#fullSheet').hidden=false;if(solving&&autoG&&window.innerWidth>900)setTimeout(()=>$('#fsAns').focus(),50);",
    "$('#fsAns').value='';fsPad();$('#fullSheet').hidden=false;if(solving&&autoG&&window.innerWidth>900&&!(J&&J.choice))setTimeout(()=>$('#fsAns').focus(),50);")
rep("$('#fsGrade').onclick=()=>{const v=$('#fsAns').value.trim();if(!v){$('#fsAns').focus();return}",
    "function choicePad(row,inp){const p=el('div','chpad');for(let n=1;n<=5;n++){const b=el('button','chb','①②③④⑤'[n-1]);b.type='button';b.setAttribute('aria-label',n+'번');b.onclick=()=>{inp.value=String(n);p.querySelectorAll('.chb').forEach(x=>x.classList.toggle('on',x===b))};p.append(b)}row.insertBefore(p,inp);return p}\nfunction fsPad(){const r=$('#fsAnsRow');const o=r.querySelector('.chpad');if(o)o.remove();const i=$('#fsAns');i.type='text';i.inputMode='numeric';i.maxLength=3;i.placeholder='숫자 입력';i.oninput=()=>{i.value=i.value.replace(/[^0-9]/g,'')};if(J&&J.choice&&mode==='japan')choicePad(r,i)}\n$('#fsGrade').onclick=()=>{const v=$('#fsAns').value.trim();if(!v){if(J&&J.choice)toast('번호를 먼저 고르세요');else $('#fsAns').focus();return}")


# ── 학생 관점 보완: 오답일 때 정답 가리기, 진단에 내 답, 유사문항도 채점, 같은 단원 이어 풀기 ──
rep("function choicePad(row,inp){", "const cN=v=>J&&J.choice&&/^[1-5]$/.test(String(v))?'①②③④⑤'[Number(v)-1]:v;\nfunction simAns(s){const a=String(s.ans&&s.ans.ko||'').trim();const c='①②③④⑤'.indexOf(a[0]);if(c>=0)return{choice:true,v:c+1};const m=a.replace(/\\$/g,'').trim().match(/^\\d+$/);return{choice:false,v:m?Number(m[0]):null}}\nfunction choicePad(row,inp){")
rep("${auto&&rec.ans!=null?`내 답 <b class=\"num\">${esc(rec.ans)}</b> · 정답 <b class=\"num\">${esc(J.answer)}</b> · `:''}",
    "${auto&&rec.ans!=null?`내 답 <b class=\"num\">${esc(cN(rec.ans))}</b> · 정답 ${rec.r==='no'?`<button class=\"reveal\" data-a=\"${esc(cN(J.answer))}\" onclick=\"this.outerHTML='<b class=&quot;num&quot;>'+this.dataset.a+'</b>'\">눌러서 보기</button>`:`<b class=\"num\">${esc(cN(J.answer))}</b>`} · `:''}")
rep("<dt>정답</dt><dd class=\"num\">${J.answer==null?'미등록 (스스로 점검)':(J.choice?['①','②','③','④','⑤'][J.answer-1]||J.answer:J.answer)}</dd>`));",
    "<dt>정답</dt><dd class=\"num\">${J.answer==null?'미등록 (스스로 점검)':(J.choice?['①','②','③','④','⑤'][J.answer-1]||J.answer:J.answer)}</dd>${S.jrec[J.num]&&S.jrec[J.num].ans!=null?`<dt>내 답</dt><dd class=\"num\">${esc(cN(S.jrec[J.num].ans))} · ${S.jrec[J.num].r==='ok'?'<b style=\"color:var(--ok,#1f9d55)\">정답</b>':'<b style=\"color:#ff8181\">오답</b>'}${S.jrec[J.num].secs?' · '+mmss(S.jrec[J.num].secs):''}</dd>`:''}`));")
rep("`정답 <b class=\"num\">${esc(J.answer)}</b>. 맞았어도", "`정답 <b class=\"num\">${esc(cN(J.answer))}</b>. 맞았어도")
rep("`정답은 <b class=\"num\">${esc(J.answer)}</b>. 내 풀이가", "`정답은 <b class=\"num\">${esc(cN(J.answer))}</b>. 내 풀이가")
rep("const re=el('button','btn ghost',tj('다시 풀기','もう一度解く'));re.onclick=()=>{delete S.jrec[J.num];save();unlocked=false;openJapan(J.num,0)};row.append(re);\n    const hm=",
    "const su=isP&&JLIST.find(x=>x.num!==J.num&&x.kind==='past'&&isG1(x)===isG1(J)&&(x.unit||x.subj)===(J.unit||J.subj)&&!S.jrec[x.num]);if(su){const sb=el('button','btn ghost','같은 단원 더 풀기 · '+esc(J.unit||J.subj));sb.onclick=()=>location.hash='j'+su.num;row.append(sb)}\n    const re=el('button','btn ghost',tj('다시 풀기','もう一度解く'));re.onclick=()=>{delete S.jrec[J.num];save();unlocked=false;openJapan(J.num,0)};row.append(re);\n    const hm=")
rep("bt.onclick=()=>{an.hidden=false;bt.hidden=true};const row=el('div','btnrow');row.append(bt);b.append(row,an);",
    "bt.onclick=()=>{an.hidden=false;bt.hidden=true};const row=el('div','btnrow');const sa=simAns(s);\n    if(!ja&&sa.v!=null){bt.className='btn ghost';bt.textContent='풀지 않고 정답·풀이 보기';const ai=el('div','ansin');const si=el('input');si.type='text';si.inputMode='numeric';si.maxLength=3;si.placeholder='숫자 입력';si.oninput=()=>{si.value=si.value.replace(/[^0-9]/g,'')};const gb=el('button','btn','채점');ai.append(el('span',null,'내 답'),si,gb);if(sa.choice)choicePad(ai,si);const res=el('div');\n      gb.onclick=()=>{if(!si.value){toast(sa.choice?'번호를 먼저 고르세요':'답을 입력하세요');return}const ok=Number(si.value)===sa.v;res.innerHTML='';res.append(el('div','result '+(ok?'ok':'no'),`<div class=\"big\">${ok?'정답입니다':'오답입니다'}</div><div>${ok?'같은 개념을 제대로 잡았어요. 풀이와 내 방법을 비교해 보세요.':'풀이를 보고 어느 단계에서 달라졌는지 찾아보세요.'}</div>`));an.hidden=false;bt.hidden=true;ai.hidden=true};\n      si.onkeydown=e=>{if(e.key==='Enter')gb.click()};b.append(ai,res)}\n    row.append(bt);b.append(row,an);")
rep("'원문제와 같은 아이디어로 조건을 바꾼 문제입니다. 종이에 풀고 나서 답을 확인하세요.'", "'원문제와 같은 아이디어로 조건을 바꾼 문제입니다. 종이에 풀고 답을 골라 채점하면 풀이가 열립니다.'")

# ── 유사문항 가독성: 문제는 종이 카드에, 보기는 한 줄씩, 답 고르기 칸은 따로 ──
rep("const q=el('div');renderEnBlocks(q,ja?s.ja:s.ko);if(ja)q.lang='ja';b.append(q);", "const q=el('div','simq');renderEnBlocks(q,ja?s.ja:s.ko);if(ja)q.lang='ja';b.append(q);")
rep("const gb=el('button','btn','채점');ai.append(el('span',null,'내 답'),si,gb);if(sa.choice)choicePad(ai,si);", "const gb=el('button','btn','채점');ai.className='ansin simansin';ai.append(el('span','al',sa.choice?'답 고르기':'답 입력'),si,gb);if(sa.choice)choicePad(ai,si);")

rep("'※ 유사문항은 ShrekMath 자체 제작입니다. (정답은 계산과 전수 확인으로 검증)'", "'※ 유사문항은 ShrekMath 자체 제작입니다.'")
rep("'※ 類題はShrekMathの自作問題です(答えは計算・全数確認で検証済み)。'", "'※ 類題はShrekMathの自作問題です。'")

# ── 로고: 새싹 아이콘 + '루키들의' + 초록 '수학몰' ──
rep('<a class="logo" id="logoHome" href="#" title="홈으로">루키들의 수학몰<span class="meta">',
    '<a class="logo" id="logoHome" href="#" title="홈으로">'+RKSVG+'루키들의 <em>수학몰</em><span class="meta">')
rep('<a class="logo" id="logoOp" href="#" title="홈으로">루키들의 수학몰<span class="tot"',
    '<a class="logo" id="logoOp" href="#" title="홈으로">'+RKSVG+'루키들의 <em>수학몰</em><span class="tot"')

# ── 관(탭): 고1 기초관 · 기출관 (킬러·논술·일본관은 숨김) ──
rep('<button data-tab="killer" class="on">킬러관<span class="n" id="nKiller">0</span></button>',
    '<button data-tab="g1" class="on">고1 기초관<span class="n" id="nG1">0</span></button>')
rep('<button data-tab="essay">논술관<span class="n" id="nEssay">0</span></button>',
    '')
rep('<button data-tab="japan">일본관<span class="n" id="nJapan">0</span></button>',
    '<span hidden><span id="nKiller"></span><span id="nEssay"></span><span id="nJapan"></span></span>')
rep("let S={rec:{},erec:{},jrec:{},fs:1,tab:'killer',", "let S={rec:{},erec:{},jrec:{},fs:1,tab:'g1',")
rep("S.tab='killer';save();if(location.hash)", "S.tab='g1';save();if(location.hash)")
rep('id="langBtn" title="View in English (Past Exams)">EN</button>', 'id="langBtn" title="View in English (Past Exams)" hidden>EN</button>')

rep("const TAB_KO={killer:'킬러관',essay:'논술관',past:'기출관',japan:'일본관'}, TAB_EN={killer:'Killer',essay:'Essay',past:'Past',japan:'Japan'};",
    "const TAB_KO={g1:'고1 기초관',killer:'킬러관',essay:'논술관',past:'기출관',japan:'일본관'}, TAB_EN={g1:'Grade 10',killer:'Killer',essay:'Essay',past:'Past',japan:'Japan'};")
# 고1·평가원을 같은 '기출' 형식(문제지 이미지 + 자동 채점)으로 쓰되, 탭에 따라 목록을 나눈다
rep("function _jsplit(){if(_jcSrc!==JLIST){const jp=[],pa=[],no=new Map();for(const x of JLIST){const a=x.kind==='past'?pa:jp;a.push(x);no.set(x,a.length)}_jc={jp,pa,no};_jcSrc=JLIST}return _jc}\nconst JP=()=>_jsplit().jp, PAST=()=>_jsplit().pa;",
    "function _jsplit(){if(_jcSrc!==JLIST){const jp=[],pa=[],g1=[],no=new Map();for(const x of JLIST){const a=x.kind!=='past'?jp:x.part==='고1'?g1:pa;a.push(x);no.set(x,a.length)}_jc={jp,pa,g1,no};_jcSrc=JLIST}return _jc}\nconst JP=()=>_jsplit().jp, PAST=()=>S.tab==='g1'?_jsplit().g1:_jsplit().pa, isG1=x=>x&&x.part==='고1';")
rep("$('#nPast').textContent=PAST().length;setTot();", "$('#nPast').textContent=_jsplit().pa.length;$('#nG1').textContent=_jsplit().g1.length;setTot();")
rep("const h='<b>'+(LIST.length+ELIST.length+JP().length+PAST().length).toLocaleString()", "const h='<b>'+(LIST.length+ELIST.length+JLIST.length).toLocaleString()")
rep("function rankOf(n){RANKS[RANKS.length-1][0]=LIST.length||", "function rankOf(n){RANKS[RANKS.length-1][0]=JLIST.length||")
rep("$('#tabs').onclick=e=>{const b=e.target.closest('button');if(!b)return;S.tab=b.dataset.tab;save();home()};",
    "$('#tabs').onclick=e=>{const b=e.target.closest('button');if(!b)return;if(S.tab!==b.dataset.tab)Object.assign(pfilt,{year:'',mon:'',part:'',five:false});S.tab=b.dataset.tab;save();home()};")
rep("else if(S.tab==='past'){pool=PAST()", "else if(S.tab==='past'||S.tab==='g1'){pool=PAST()")

# home(): 두 관 모두 '기출' 화면, 문구는 관마다
rep("  const essay=S.tab==='essay', japan=S.tab==='japan', past=S.tab==='past', other=essay||japan||past;",
    "  if(!['g1','past'].includes(S.tab))S.tab='g1';const g1=S.tab==='g1';\n  const essay=S.tab==='essay', japan=S.tab==='japan', past=S.tab==='past'||g1, other=essay||japan||past;")
rep("  mosaic();$('#heroTitle').innerHTML=past?",
    "  mosaic();$('#heroTitle').innerHTML=g1?'고1 기초관: <em>한 문제씩</em> 기본기 쌓기':past?")
rep("$('#heroText').textContent=past?", "$('#heroText').textContent=g1?'2012~2020년 고1 전국연합학력평가에서 2점·3점 위주로 고른 문항입니다. 문제지 이미지 그대로 시험처럼 풀고, 공식 정답으로 바로 채점합니다. 유사문항(쌍둥이 문제)으로 같은 개념을 한 번 더 확인하세요.':past?")
rep("'기출관: 평가원이 <em>진짜로 낸</em> 킬러'", "'기출관: 평가원 기출의 <em>2~3점과 쉬운 4점</em>'")
rep("'2022~2026학년도 6월·9월 모의평가와 수능의 공통 11~15·20~22번, 미적분 28·29·30번, 확통·기하 28·29·30번. 문제지 이미지 그대로 시험처럼 풀고, 평가원 정답으로 바로 채점합니다.'",
    "'2022~2026학년도 6월·9월 모의평가와 수능의 공통 1~10·16~19번, 선택과목(확률과 통계·미적분·기하) 23~27번. 문제지 이미지 그대로 시험처럼 풀고, 평가원 정답으로 바로 채점합니다.'")
rep("$('#flowNote').textContent=past?'제한시간: 22·30번 13분 · 13·15·21·29번과 미적분 28번 10분 · 11·12·14·20번과 확통·기하 28·30번 8분. 문제지 그대로, 평가원 정답표로 자동 채점.'",
    "$('#flowNote').textContent=past?'제한시간: ★ 4분 · ★★ 6분 · ★★★ 8분. 넘어도 끝까지 풀 수 있어요. 문제지 그대로, 공식 정답표로 자동 채점.'")
rep("  else if(past)$('#footPast').innerHTML=window.__footPastKo||$('#footPast').innerHTML;",
    "  else if(past)$('#footPast').innerHTML=g1?'문항: 시·도교육청 2012~2020년 고1 전국연합학력평가 수학 영역 (문제지 이미지 그대로, 공식 정답표로 자동 채점). 예전 교육과정 문항이라 지금 교과서와 단원 이름이 다를 수 있어요. 유사문항은 ShrekMath가 새로 썼습니다.<br>기록은 이 브라우저에만 저장됩니다.':'문항: 한국교육과정평가원 2022~2026학년도 6월·9월 모의평가와 대학수학능력시험 수학 영역 (홀수형, 문제지 이미지 그대로, 평가원 정답표로 자동 채점). 해설은 EBSi 등에서 확인하세요.<br>더 어려운 문제는 <a href=\"https://killershrekmath.vercel.app\" target=\"_blank\" rel=\"noopener\">킬러들의 수학몰</a>에서.';")
rep('<div class="flow" id="flowPast" hidden><span style="--kc:var(--k-solve)">① 실전 · 제한시간</span><span style="--kc:var(--k-intro)">② 채점 · 진단</span><span style="--kc:var(--k-end)">③ 정리</span></div>',
    '<div class="flow" id="flowPast" hidden><span class="f1">① 실전</span><span class="f2">② 진단</span><span class="f3">③ 해설</span><span class="f4">④ 유사</span><span class="f5">⑤ 정리</span></div>')
# 통계 타일: 킬러·논술 대신 채점 기준
rep('<span>킬러 <b id="rSolved">0</b></span>', '<span>채점 <b id="rSolved">0</b></span>')
rep('<span>논술 <b id="rEssay">0</b></span><span>논술 평균 <b id="rEssayAvg">–</b></span>', '<span hidden><b id="rEssay">0</b><b id="rEssayAvg">–</b></span>')
# 배경 모자이크: 루키 문항으로
rep("...PAST().filter(x=>x.num0>=22).map(x=>({t:x.year+' '+x.track,c:'var(--d'+x.stars+')',n:'기출'}))",
    "...JLIST.filter((x,i)=>i%3===0).map(x=>({t:x.subj,c:'var(--d'+(x.stars+1)+')',n:x.part==='고1'?'고1':'기출'}))")

# 기출관 목록: 시험·과목(단원) 필터를 관에 맞게
rep("  const grid=$('#grid');grid.innerHTML='';const P=PAST();\n  const ys=$('#pYearSel');if(ys.options.length<=1){",
    "  const grid=$('#grid');grid.innerHTML='';const P=PAST();const g1=S.tab==='g1';\n  const ys=$('#pYearSel');if(ys.dataset.tab!==S.tab){ys.dataset.tab=S.tab;ys.length=1;ys.options[0].textContent=g1?'모든 연도':'모든 학년도';\n    const ms=$('#pMonSel');ms.length=0;(g1?[['','3·6·9·11월'],['3월','3월'],['6월','6월'],['9월','9월'],['11월','11월']]:[['','6월·9월·수능'],['6월','6월 모의평가'],['9월','9월 모의평가'],['11월','수능']]).forEach(([v,t])=>{const o=el('option',null,t);o.value=v;ms.append(o)});\n    const pc=$('#pPartChips');pc.innerHTML='';(g1?[...new Set(P.map(x=>x.subj))].sort((a,b)=>UNIT_ORDER.indexOf(a)-UNIT_ORDER.indexOf(b)):['공통','확률과 통계','미적분','기하']).forEach(v=>{const c=el('button','chip',esc(v));c.dataset.k='part';c.dataset.v=v;pc.append(c)});$('#pPartLbl').textContent=g1?'단원':'과목'}\n  if(ys.options.length<=1){")
rep("[...ys.options].forEach(o=>{if(o.value)o.textContent=EN()?o.value:o.value+'학년도'});",
    "[...ys.options].forEach(o=>{if(o.value)o.textContent=EN()?o.value:o.value+(g1?'년':'학년도')});")
rep("(!pfilt.part||x.part===pfilt.part)&&(!pfilt.five||x.stars>=5)", "(!pfilt.part||(g1?x.subj:x.part)===pfilt.part)&&(!pfilt.five||x.stars>=3)")
rep("L=[...L].sort((a,b)=>b.year.localeCompare(a.year)||['11월','9월','6월'].indexOf(a.month)-['11월','9월','6월'].indexOf(b.month)||a.num-b.num);",
    "L=[...L].sort((a,b)=>b.year.localeCompare(a.year)||['11월','9월','6월','3월'].indexOf(a.month)-['11월','9월','6월','3월'].indexOf(b.month)||a.num-b.num);")
# 과목 칩 자리: 관마다 채운다
s2 = re.sub(r'<div class="fgrp"><span class="fl" data-en="Subject">과목</span>\s*<button class="chip" data-k="part" data-v="공통"[^\n]*\n[^\n]*\n[^\n]*\n[^\n]*\n\s*</div>',
            '<div class="fgrp"><span class="fl" id="pPartLbl">과목</span><span id="pPartChips" class="fchips"></span></div>', s, count=1)
if s2 == s: sys.exit('[patch] 과목 칩 자리를 찾지 못함')
s = s2
rep('<button class="chip" data-k="five" data-v="1" data-en="★★★★★ only">★★★★★만</button>', '<button class="chip" data-k="five" data-v="1">★★★ 도전만</button>')
# 카드: 별 3개 만점, 난이도 이름, 연도 표기
rep("<span class=\"num\">#P${JNO(x)}</span> · ${EN()?({'11월':'CSAT','6월':'June','9월':'Sept.'}[x.month]):(x.month==='11월'?'수능':x.month)}",
    "<span class=\"num\">${isG1(x)?'#G':'#P'}${JNO(x)}</span> · ${isG1(x)?x.month:(x.month==='11월'?'수능':x.month)}")
rep("<div class=\"topic\">${EN()?esc(pTrack(x))+' · '+x.year:esc(x.track)+' · '+x.year+'학년도'}</div>",
    "<div class=\"topic\">${esc(x.track)+' · '+x.year+(isG1(x)?'년':'학년도')}</div>")
rep("<span class=\"stars\">${'★'.repeat(x.stars)}${'☆'.repeat(5-x.stars)}</span><span class=\"dbadge\">${EN()?DIFF_EN(x.stars):x.stars>=5?'킬러':x.stars>=4?'고난도':'준킬러'}</span>",
    "<span class=\"stars\">${'★'.repeat(x.stars)}${'☆'.repeat(3-x.stars)}</span><span class=\"dbadge\">${RDN[x.stars]}</span>")
rep("(x.choice?'5지선다':'주관식')+' · '+(LIMIT[x.stars]||8)+'분'+(x.answer==null?' · 정답 미등록':'')",
    "(x.choice?'5지선다':'단답형')+' · '+(LIMIT[x.stars]||8)+'분'+(x.sim?' · 🌱유사':'')")
# 제한시간·난이도 (루키: ★1~★3)
rep("const LIMIT={5:13,4:10,3:8,2:8};   // 제한시간(분): 킬러 13 · 고난도 10 · 준킬러 8",
    "const LIMIT={3:8,2:6,1:4};   // 제한시간(분): ★★★ 8 · ★★ 6 · ★ 4\nconst RDN={1:'기본',2:'실력',3:'도전'};\nconst UNIT_ORDER=['중학 복습','다항식','복소수·이차방정식','이차함수','여러 방정식·부등식','도형의 방정식','집합과 명제','함수','경우의 수·확률·수열','기타'];")

# 카드·모자이크 색: 난이도 대신 단원·과목 색 (더 알록달록하게)
rep("const RDN={1:'기본',2:'실력',3:'도전'};", "const RDN={1:'기본',2:'실력',3:'도전'};\nconst UCOL=" + json.dumps({k: pre(v) for k, v in UNIT_COL.items()}, ensure_ascii=False) + ";const UC=x=>UCOL[x.unit]||UCOL[x.subj]||UCOL[x.part]||'#5a5a5a';\nconst UCOLR=" + json.dumps(UNIT_COL, ensure_ascii=False) + ";const UCR=x=>UCOLR[x.unit]||UCOLR[x.subj]||UCOLR[x.part]||'#facc15';")
rep("const c=el('button','card');const rec=S.jrec[x.num];c.style.setProperty('--dc',DC(x.stars));c.dataset.big=String(x.num0);",
    "const c=el('button','card');const rec=S.jrec[x.num];c.style.setProperty('--dc',UC(x));c.style.setProperty('--hl',UCR(x));c.dataset.big=String(x.num0);")
rep("artEl(x.text,x.subj,x.art,x.id,DC(x.stars),null,x.qimg&&x.qimg[0])", "artEl(x.text,x.subj,x.art,x.id,UC(x),null,x.qimg&&x.qimg[0])", 2)
rep("...JLIST.filter((x,i)=>i%3===0).map(x=>({t:x.subj,c:'var(--d'+(x.stars+1)+')',n:x.part==='고1'?'고1':'기출'}))",
    "...JLIST.filter((x,i)=>i%3===0).map(x=>({t:x.subj,c:UC(x),n:x.part==='고1'?'고1':'기출'}))")
# 문제 화면
rep("$('#opId').innerHTML=isP?`#P${JNO(J)} · 평가원 기출 <span class=\"subj\" style=\"--sc:${SC(J.subj)}\">${esc(J.part)}</span>`",
    "$('#opId').innerHTML=isP?`${isG1(J)?'#G':'#P'}${JNO(J)} · ${isG1(J)?'고1 학력평가':'평가원 기출'} <span class=\"subj\" style=\"--sc:${SC(J.subj)}\">${esc(isG1(J)?J.subj:J.part)}</span>`")
rep("const nx=JLIST.find(x=>x.num>J.num&&(x.kind==='past')===isP);", "const nx=JLIST.find(x=>x.num>J.num&&(x.kind==='past')===isP&&isG1(x)===isG1(J));")
rep("    b.append(el('dl','kv',`<dt>출처</dt><dd>한국교육과정평가원 · ${J.year}학년도 ${J.month==='11월'?'대학수학능력시험':'대학수학능력시험 '+J.month+' 모의평가'} (홀수형)</dd><dt>과목</dt><dd>${esc(J.part)}</dd><dt>형식</dt><dd>${J.choice?'5지선다형':'단답형'} · 4점</dd><dt>난이도</dt><dd><span class=\"stars\" style=\"--dc:${DC(J.stars)}\">${'★'.repeat(J.stars)}</span> ${J.stars>=5?'킬러':J.stars>=4?'고난도':'준킬러'} · 제한 ${lim}분</dd>",
    "    b.append(el('dl','kv',`<dt>출처</dt><dd>${isG1(J)?`시·도교육청 · ${J.year}년 ${J.month} 고1 전국연합학력평가`:J.id.startsWith('g3')?`시·도교육청 · ${J.year}년 ${J.month} 고3 전국연합학력평가`:`한국교육과정평가원 · ${J.year}학년도 ${J.month==='11월'?'대학수학능력시험':'대학수학능력시험 '+J.month+' 모의평가'} (홀수형)`}</dd><dt>${isG1(J)?'단원':'과목'}</dt><dd>${esc(isG1(J)?J.subj:J.part)}${J.topic?' · '+esc(J.topic):''}</dd><dt>형식</dt><dd>${J.choice?'5지선다형':'단답형'}</dd><dt>난이도</dt><dd><span class=\"stars\" style=\"--dc:${DC(J.stars)}\">${'★'.repeat(J.stars)}</span> ${RDN[J.stars]} · 제한 ${lim}분</dd>")
rep("    b.append(el('p','note','평가원 기출은 해설을 싣지 않습니다. EBSi(ebsi.co.kr) 기출문제 해설이나 교사의 풀이로 확인하세요. 같은 번호 자리의 창작 문항은 킬러관에 있습니다.'));",
    "    b.append(el('p','note',(J.expl?'다음 단계에서 해설을 보고, ':'해설은 준비 중입니다. ')+(J.sim?'유사문항(쌍둥이 문제)으로 같은 개념을 한 번 더 확인하세요.':'선생님 풀이나 EBSi(ebsi.co.kr) 해설로 확인하세요.')));")
# 유사문항: 한국어만 있으면 언어 버튼 숨김
rep("const ja2=!s.ko;if(ja2)ja=true;if(!ja2)b.append(langSeg(jaRefresh));", "const ja2=!s.ko;if(ja2)ja=true;else ja=false;if(!ja2&&s.ja)b.append(langSeg(jaRefresh));")

# ── 쉬운 말로 (루키): 쇼핑몰 표현 → 학습 표현, 내부 관리 번호 숨기고 시험·문항 번호 보이기 ──
rep("const RANKS=[[0,'손님'],[3,'단골'],[10,'VIP'],[25,'점원'],[45,'매니저'],[72,'사장']];", "const RANKS=[[0,'씨앗'],[3,'새싹'],[10,'떡잎'],[25,'줄기'],[45,'꽃'],[72,'열매']];")
rep('<div class="big" id="rankName">손님</div>', '<div class="big" id="rankName">씨앗</div>')
rep('<div class="lbl">회원 등급</div>', '<div class="lbl">학습 단계 · 채점한 문제 수로 자라요</div>')
rep("rankSub').textContent=nx?`${nx[1]}까지 ${nx[0]-g.length}문항`:'이 몰의 상품을 전부 털었어요';", "rankSub').textContent=nx?`‘${nx[1]}’까지 ${nx[0]-g.length}문제 더`:'모든 문제를 풀었어요!';")
rep('<span class="lbl"> 아무거나</span>', '<span class="lbl"> 랜덤 문제</span>')
rep('<span class="lbl"> 영수증 뽑기</span>', '<span class="lbl"> 학습 기록 내보내기</span>')
rep("toast('영수증을 복사했어요 (엑셀·시트에 붙여넣기)')", "toast('학습 기록을 복사했어요 (엑셀·시트에 붙여넣기)')")
rep('>환불은 없다, 풀이만 있다. 영수증(기록)은 내 브라우저에만 남습니다.</div>', '>푼 기록은 이 기기(브라우저)에 저장돼요. 로그인하면 다른 기기에서도 이어서 풀 수 있어요.</div>')
rep('>입장하기 <span>›</span></button>', '>문제 풀러 가기 <span>›</span></button>')
rep('<div class="lbl">영수증 · 실전 기록 ', '<div class="lbl">학습 기록 ')
rep('<span>오늘 <b id="rToday">0</b>문항</span><span>연속 <b id="rStreak">0</b>일</span><span>복습 필요 <b id="rReview">0</b></span>',
    '<span>오늘 푼 문제 <b id="rToday">0</b></span><span>연속 학습 <b id="rStreak">0</b>일</span><span>다시 풀 문제 <b id="rReview">0</b></span>')
rep('<span>채점 <b id="rSolved">0</b></span><span>정답률 <b id="rAcc">–</b></span><span>평균 <b id="rAvg">–</b></span>',
    '<span>푼 문제 <b id="rSolved">0</b></span><span>정답률 <b id="rAcc">–</b></span><span>평균 시간 <b id="rAvg">–</b></span>')
rep(">복습 필요 (오답·시간초과)</button>", ">다시 풀 문제 (틀림·시간초과)</button>")
# 내부 관리 번호(#G284 등) 대신 시험·문항 번호
rep("c.innerHTML=`<div class=\"top\"><span><span class=\"num\">${isG1(x)?'#G':'#P'}${JNO(x)}</span> · ${isG1(x)?x.month:(x.month==='11월'?'수능':x.month)}",
    "c.innerHTML=`<div class=\"top\"><span><span class=\"num\">${x.year}${isG1(x)?'년':'학년도'} ${isG1(x)?x.month:(x.month==='11월'?'수능':x.month+' 모평')}</span>")
rep("<div class=\"topic\">${esc(x.track)+' · '+x.year+(isG1(x)?'년':'학년도')}</div>", "<div class=\"topic\">${esc(x.track)}</div>")
rep("$('#opId').innerHTML=isP?`${isG1(J)?'#G':'#P'}${JNO(J)} · ${isG1(J)?'고1 학력평가':'평가원 기출'}", "$('#opId').innerHTML=isP?`${isG1(J)?'고1 학력평가':J.id.startsWith('g3')?'고3 학력평가':'평가원 기출'}")
rep("head('solve','STEP 0')", "head('solve','')", 4)

# ── 원문항 해설 단계 (진단 → 해설 → 유사 → 정리) ──
rep("sim:['유사문항','같은 아이디어, 다른 조건']};", "sim:['유사문항','같은 아이디어, 다른 조건'],expl:['해설','풀이 과정']};")
rep("const ORDER=['solve','intro',", "const ORDER=['solve','intro','expl',")
rep("--k-answer:#a6e85c;", "--k-answer:#a6e85c; --k-expl:#f5a524;")
rep("    if(J.sim)pages.push({k:'sim'});\n  }", "    if(J.expl)pages.push({k:'expl'});\n    if(J.sim)pages.push({k:'sim'});\n  }")
rep("  if(p.k==='sim'){w.append(head('sim'));", "  if(p.k==='expl'){w.append(head('expl'));const b=el('div','body expl');b.append(el('p','lead',`정답 <b class=\"num\">${esc(cN(J.answer))}</b>`));const q=el('div');renderEnBlocks(q,J.expl);b.append(q);b.append(el('p','note','※ 해설은 ShrekMath가 작성했습니다. 다른 방법으로 풀었다면 두 방법을 비교해 보세요.'));w.append(b);return w}\n  if(p.k==='sim'){w.append(head('sim'));")

# ── 학생 입장 사용성 (2026-11 검토) ──
# 수식 라이브러리를 사이트에 직접 둔다 (학교망·느린 망에서 CDN이 막혀도 수식이 깨지지 않게)
rep('<script src="https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.16.11/katex.min.js"></script>', '<script src="/lib/katex.min.js"></script>')
rep('<script src="https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.16.11/contrib/auto-render.min.js"></script>', '<script src="/lib/auto-render.min.js"></script>')
# 휴대폰: 채점 뒤에도 문제를 접지 않는다 (해설·진단을 보며 문제를 같이 볼 수 있게. 필요하면 '접기')
rep("  if(window.innerWidth<=900&&unlocked&&!userUnfold){$('#exam').classList.add('fold');$('#foldBtn').textContent=LP()?'Unfold':'펼치기'}\n", "")
s = s.replace("</style>", """.card .topic{align-self:stretch!important;text-align:left}
@media (max-width:900px){
  .topbar .cta .lbl{display:inline!important;font-size:.72rem}
  .topbar .cta{padding:6px 9px!important}
  .veil{padding:10px 14px;font-size:.84rem;line-height:1.5}
  .veil b{font-size:1.1rem;margin-bottom:3px}
}
@media (max-width:380px){.topbar .cta .lbl{display:none!important}}
.topbar .cta .lm{display:none!important}
@media (max-width:900px){.topbar .cta .ld{display:none!important}.topbar .cta .lm{display:inline!important}}
</style>""", 1)
rep('🎲<span class="lbl"> 랜덤 문제</span>', '🎲<span class="lbl ld"> 랜덤 문제</span><span class="lbl lm"> 랜덤</span>')
rep('🧾<span class="lbl"> 학습 기록 내보내기</span>', '🧾<span class="lbl ld"> 학습 기록 내보내기</span><span class="lbl lm"> 기록</span>')

# ── 연습장: 문제 전체 화면 아래 빈 공간에 손가락·펜으로 쓰기 (저장 안 함, 원하면 '저장'으로 그림 파일) ──
rep('<button id="fullBtn" class="mob" data-en="Full view">전체 보기</button>', '<button id="fullBtn" data-en="Scratch pad">✏️ 연습장</button>')
rep('<div class="exam open fsexam" id="fullExam"></div>', '''<div class="exam open fsexam" id="fullExam"></div>
<div id="fsPad"><div class="padbar"><span class="padlbl">연습장</span><button data-c="#1f2937" class="pc on" title="검정 펜" style="--c:#1f2937"></button><button data-c="#dc2626" class="pc" title="빨강 펜" style="--c:#dc2626"></button><button data-c="#2563eb" class="pc" title="파랑 펜" style="--c:#2563eb"></button><button id="padEr" title="지우개">지우개</button><button id="padUndo" title="되돌리기">↶</button><button id="padClr" title="전체 지우기">전체 지우기</button><button id="padSave" title="문제와 함께 그림 파일로 저장">💾 저장</button><button id="padHide" title="연습장 숨기기">▾</button></div><canvas id="padCv"></canvas><div class="padtip" id="padTip">여기에 손가락이나 펜으로 풀어 보세요</div></div>''')
s = s.replace("</style>", """#fullSheet canvas{filter:none}
#fullSheet .fsexam{flex:0 1 auto!important;max-height:52%!important;padding-bottom:14px!important}
#fullSheet.padoff .fsexam{flex:1!important;max-height:none!important}
#fsPad{flex:1;min-height:150px;position:relative;border-top:2px dashed #d6cfbd;background:#fffdf7 repeating-linear-gradient(#fffdf7 0 31px,#ece6d6 31px 32px)}
#fullSheet.padoff #fsPad{flex:0 0 auto;min-height:0}
@media (min-width:901px){#fullSheet .fsexam img.pg{max-width:820px;display:block;margin:0 auto}}
#fullSheet.padoff #fsPad canvas,#fullSheet.padoff #fsPad .padtip,#fullSheet.padoff #fsPad .padbar>*:not(.padlbl):not(#padHide){display:none}
#fullSheet.padoff #fsPad .padbar{position:static;justify-content:flex-end;background:rgba(0,0,0,.03)}
#padCv{position:absolute;inset:0;width:100%;height:100%;touch-action:none;cursor:crosshair}
#fsPad .padbar{position:absolute;top:6px;right:8px;left:8px;z-index:2;display:flex;gap:5px;align-items:center;justify-content:flex-end;flex-wrap:wrap;pointer-events:none}
#fsPad .padbar>*{pointer-events:auto}
#fsPad .padlbl{margin-right:auto;font-size:.72rem;color:#9a937f;letter-spacing:.1em;font-weight:700;pointer-events:none}
#fsPad .padbar button{border:1px solid #d6cfbd;border-radius:8px;background:#fffffff0;color:#4a4639;font-size:.8rem;padding:5px 9px;line-height:1.2}
#fsPad .padbar button.on{background:#1f2937;color:#fff;border-color:#1f2937}
#fsPad .padbar .pc{width:28px;height:28px;padding:0;border-radius:50%;background:var(--c);border:3px solid #fff;box-shadow:0 0 0 1px #c9c1ad}
#fsPad .padbar .pc.on{background:var(--c);border-color:#fff;box-shadow:0 0 0 3px var(--c)}
#fullSheet.padoff #fsPad .padlbl{display:none!important}
#fsPad .padtip{position:absolute;inset:0;display:grid;place-items:center;color:#c5bda6;font-size:.95rem;pointer-events:none}
@media (max-width:900px){#fullSheet .fsexam{max-height:46%!important}#fsPad .padbar button{font-size:.74rem;padding:4px 7px}#fsPad .padbar .pc{width:24px;height:24px}}
</style>""", 1)
rep("fsPad();$('#fullSheet').hidden=false;", "fsPad();$('#fullSheet').hidden=false;PAD.open();")
s = s.replace("\n</script>", r"""
/* ───────── 연습장 ───────── */
const PAD=(()=>{const cv=$('#padCv'),ctx=cv.getContext('2d');let strokes=[],cur=null,color='#1f2937',erase=false,key='',penSeen=false;
  const fit=()=>{const r=cv.getBoundingClientRect();if(!r.width)return;const d=Math.min(2,devicePixelRatio||1);cv.width=Math.round(r.width*d);cv.height=Math.round(r.height*d);ctx.setTransform(d,0,0,d,0,0);draw()};
  const line=st=>{if(!st.p.length)return;ctx.globalCompositeOperation=st.e?'destination-out':'source-over';ctx.strokeStyle=st.c;ctx.lineWidth=st.e?22:2.4;ctx.lineCap='round';ctx.lineJoin='round';ctx.beginPath();ctx.moveTo(st.p[0][0],st.p[0][1]);if(st.p.length===1)ctx.lineTo(st.p[0][0]+.1,st.p[0][1]);for(let i=1;i<st.p.length;i++)ctx.lineTo(st.p[i][0],st.p[i][1]);ctx.stroke();ctx.globalCompositeOperation='source-over'};
  const draw=()=>{ctx.clearRect(0,0,cv.width,cv.height);strokes.forEach(line);$('#padTip').hidden=strokes.length>0};
  const pt=e=>{const r=cv.getBoundingClientRect();return[e.clientX-r.left,e.clientY-r.top]};
  cv.addEventListener('pointerdown',e=>{if(e.pointerType==='pen')penSeen=true;else if(penSeen&&e.pointerType==='touch')return;cv.setPointerCapture(e.pointerId);cur={c:color,e:erase,p:[pt(e)],id:e.pointerId};strokes.push(cur);draw();e.preventDefault()});
  cv.addEventListener('pointermove',e=>{if(!cur||e.pointerId!==cur.id)return;const ev=e.getCoalescedEvents?e.getCoalescedEvents():[e];ev.forEach(x=>cur.p.push(pt(x)));draw()});
  const end=e=>{if(cur&&e.pointerId===cur.id)cur=null};cv.addEventListener('pointerup',end);cv.addEventListener('pointercancel',end);
  document.querySelectorAll('#fsPad .pc').forEach(b=>b.onclick=()=>{color=b.dataset.c;erase=false;document.querySelectorAll('#fsPad .pc,#padEr').forEach(x=>x.classList.toggle('on',x===b))});
  $('#padEr').onclick=()=>{erase=!erase;$('#padEr').classList.toggle('on',erase);document.querySelectorAll('#fsPad .pc').forEach(x=>x.classList.toggle('on',!erase&&x.dataset.c===color))};
  $('#padUndo').onclick=()=>{strokes.pop();draw()};
  $('#padClr').onclick=()=>{if(!strokes.length)return;if(confirm('연습장을 모두 지울까요?')){strokes=[];draw()}};
  $('#padHide').onclick=()=>{const off=$('#fullSheet').classList.toggle('padoff');$('#padHide').textContent=off?'✏️ 연습장 펴기':'▾';try{localStorage.setItem('rk:padoff',off?'1':'')}catch(_){}if(!off)requestAnimationFrame(fit)};
  $('#padSave').onclick=async()=>{if(!strokes.length){toast('연습장에 쓴 내용이 없어요');return}
    const W=1000,ims=[...$('#fullExam').querySelectorAll('img.pg')].filter(i=>i.complete&&i.naturalWidth);let H=70;const hs=ims.map(i=>Math.round(i.naturalHeight*W/i.naturalWidth));hs.forEach(h=>H+=h+10);
    const r=cv.getBoundingClientRect(),sc=W/r.width,ph=Math.round(r.height*sc);H+=ph+20;
    const o=document.createElement('canvas');o.width=W;o.height=H;const g=o.getContext('2d');g.fillStyle='#fff';g.fillRect(0,0,W,H);
    g.fillStyle='#1f2937';g.font='bold 26px sans-serif';const ttl=($('#opTitle')&&$('#opTitle').textContent)||document.title;g.fillText(ttl.slice(0,40),24,44);
    g.fillStyle='#9a937f';g.font='18px sans-serif';g.fillText('루키들의 수학몰 · '+new Date().toLocaleDateString('ko-KR'),W-300,44);
    let y=70;ims.forEach((im,i)=>{g.drawImage(im,0,y,W,hs[i]);y+=hs[i]+10});
    g.strokeStyle='#d6cfbd';g.setLineDash([8,6]);g.beginPath();g.moveTo(0,y+5);g.lineTo(W,y+5);g.stroke();g.setLineDash([]);y+=15;
    g.drawImage(cv,0,y,W,ph);
    const blob=await new Promise(res=>o.toBlob(res,'image/png'));const t=new Date(),z=n=>String(n).padStart(2,'0');const name=`rookie_pad_${t.getFullYear()}${z(t.getMonth()+1)}${z(t.getDate())}_${z(t.getHours())}${z(t.getMinutes())}.png`;
    const f=new File([blob],name,{type:'image/png'});
    if(matchMedia('(pointer:coarse)').matches&&navigator.canShare&&navigator.canShare({files:[f]})){try{await navigator.share({files:[f],title:name});return}catch(e){if(e.name==='AbortError')return}}
    const a=document.createElement('a');a.href=URL.createObjectURL(blob);a.download=name;document.body.append(a);a.click();setTimeout(()=>{URL.revokeObjectURL(a.href);a.remove()},1500);toast('저장했어요: '+name)};
  addEventListener('resize',()=>{if(!$('#fullSheet').hidden)fit()});
  return{open(){const k=location.hash.split('-')[0];if(k!==key){key=k;strokes=[];penSeen=false}let off='';try{off=localStorage.getItem('rk:padoff')||''}catch(_){}$('#fullSheet').classList.toggle('padoff',!!off);$('#padHide').textContent=off?'✏️ 연습장 펴기':'▾';requestAnimationFrame(fit)}}})();
</script>""", 1)

# 첫 화면(인트로) 기본 문구: 킬러 문구 대신 루키 첫 관(고1 기초관) 문구 — 스크립트가 돌기 전·코드 입력 화면에서도 루키 문구가 보이게 (2026-11-26)
rep('<h1 id="heroTitle">이 몰의 상품은 <em>전부 킬러다</em></h1>', '<h1 id="heroTitle">고1 기초관: <em>한 문제씩</em> 기본기 쌓기</h1>')
rep(":'이 몰의 상품은 <em>전부 킬러다</em>';", ":'루키들의 수학몰: <em>기본기부터</em> 한 문제씩';")
rep('수능 15·20·21·22·29·30번 자리의 고난도 창작 문항과 2026 수능 기출 변형. 문항은 옆에 고정해 두고, 해설은 한 장씩 넘기며 어느 조건이 어느 단계에서 쓰이는지 눈으로 따라갑니다. 먼저 풀고, 채점하고, 그 다음에 분석.', '2012~2020년 고1 전국연합학력평가에서 2점·3점 위주로 고른 문항입니다. 문제지 이미지 그대로 시험처럼 풀고, 공식 정답으로 바로 채점합니다. 유사문항(쌍둥이 문제)으로 같은 개념을 한 번 더 확인하세요.', 2)
rep('id="flowNote">제한시간: 킬러 13분 · 고난도 10분 · 준킬러 8분. 넘어도 끝까지 풀 수 있어요.</div>', 'id="flowNote">제한시간: ★ 4분 · ★★ 6분 · ★★★ 8분. 넘어도 끝까지 풀 수 있어요. 문제지 그대로, 공식 정답표로 자동 채점.</div>')
rep('data-en="No refunds — only solutions. Your receipts (records) stay in this browser."', 'data-en="Your records are saved in this browser. Log in to continue on other devices."')

open(os.path.join(ROOT, 'template.html'), 'w', encoding='utf-8').write(s)
print('template.html 생성 (킬러 화면 + 루키 수정)')
