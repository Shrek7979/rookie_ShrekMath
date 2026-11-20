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
            '공통': '#10b981', '확률과 통계': '#f97316', '미적분': '#3b82f6', '기하': '#8b5cf6'}

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
.mosaic{{opacity:.9}}
.hero h1 em{{color:{pre('#16a34a')}}}
.topbar{{border-bottom:3px solid transparent;border-image:linear-gradient(90deg,{pre('#22c55e')},{pre('#06b6d4')},{pre('#3b82f6')},{pre('#a855f7')},{pre('#f97316')}) 1}}
#tabs button[data-tab="g1"].on{{background:{pre('#22c55e')}!important;color:#000!important;border-color:{pre('#22c55e')}!important}}
#tabs button[data-tab="past"].on{{background:{pre('#3b82f6')}!important;color:#000!important;border-color:{pre('#3b82f6')}!important}}
.stats .tile:nth-child(1){{background:linear-gradient(160deg,{pre('#dcfce7')},{pre('#ffffff')});border-color:{pre('#86efac')};--tc:{pre('#22c55e')}}}
.stats .tile:nth-child(2){{background:linear-gradient(160deg,{pre('#dbeafe')},{pre('#ffffff')});border-color:{pre('#93c5fd')};--tc:{pre('#3b82f6')}}}
.stats .tile:nth-child(3){{background:linear-gradient(160deg,{pre('#fef3c7')},{pre('#ffffff')});border-color:{pre('#fcd34d')};--tc:{pre('#f59e0b')}}}
.ghead::before{{content:"";width:6px;height:1.1em;border-radius:3px;background:linear-gradient(180deg,{pre('#22c55e')},{pre('#3b82f6')})}}
.card .dbadge{{background:var(--dc)!important;color:#000!important}}
</style>
"""
s = s.replace('<style>/*__KATEX_CSS__*/</style>', '<style>/*__KATEX_CSS__*/</style>\n' + LIGHT, 1)

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
    '<div class="flow" id="flowPast" hidden><span style="--kc:var(--k-solve)">① 실전 · 제한시간</span><span style="--kc:var(--k-intro)">② 채점 · 진단</span><span style="--kc:var(--k-sim)">③ 유사문항</span><span style="--kc:var(--k-end)">④ 정리</span></div>')
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
rep("const RDN={1:'기본',2:'실력',3:'도전'};", "const RDN={1:'기본',2:'실력',3:'도전'};\nconst UCOL=" + json.dumps({k: pre(v) for k, v in UNIT_COL.items()}, ensure_ascii=False) + ";const UC=x=>UCOL[x.subj]||UCOL[x.part]||'#5a5a5a';")
rep("const c=el('button','card');const rec=S.jrec[x.num];c.style.setProperty('--dc',DC(x.stars));c.dataset.big=String(x.num0);",
    "const c=el('button','card');const rec=S.jrec[x.num];c.style.setProperty('--dc',UC(x));c.dataset.big=String(x.num0);")
rep("artEl(x.text,x.subj,x.art,x.id,DC(x.stars),null,x.qimg&&x.qimg[0])", "artEl(x.text,x.subj,x.art,x.id,UC(x),null,x.qimg&&x.qimg[0])", 2)
rep("...JLIST.filter((x,i)=>i%3===0).map(x=>({t:x.subj,c:'var(--d'+(x.stars+1)+')',n:x.part==='고1'?'고1':'기출'}))",
    "...JLIST.filter((x,i)=>i%3===0).map(x=>({t:x.subj,c:UC(x),n:x.part==='고1'?'고1':'기출'}))")
# 문제 화면
rep("$('#opId').innerHTML=isP?`#P${JNO(J)} · 평가원 기출 <span class=\"subj\" style=\"--sc:${SC(J.subj)}\">${esc(J.part)}</span>`",
    "$('#opId').innerHTML=isP?`${isG1(J)?'#G':'#P'}${JNO(J)} · ${isG1(J)?'고1 학력평가':'평가원 기출'} <span class=\"subj\" style=\"--sc:${SC(J.subj)}\">${esc(isG1(J)?J.subj:J.part)}</span>`")
rep("const nx=JLIST.find(x=>x.num>J.num&&(x.kind==='past')===isP);", "const nx=JLIST.find(x=>x.num>J.num&&(x.kind==='past')===isP&&isG1(x)===isG1(J));")
rep("    b.append(el('dl','kv',`<dt>출처</dt><dd>한국교육과정평가원 · ${J.year}학년도 ${J.month==='11월'?'대학수학능력시험':'대학수학능력시험 '+J.month+' 모의평가'} (홀수형)</dd><dt>과목</dt><dd>${esc(J.part)}</dd><dt>형식</dt><dd>${J.choice?'5지선다형':'단답형'} · 4점</dd><dt>난이도</dt><dd><span class=\"stars\" style=\"--dc:${DC(J.stars)}\">${'★'.repeat(J.stars)}</span> ${J.stars>=5?'킬러':J.stars>=4?'고난도':'준킬러'} · 제한 ${lim}분</dd>",
    "    b.append(el('dl','kv',`<dt>출처</dt><dd>${isG1(J)?`시·도교육청 · ${J.year}년 ${J.month} 고1 전국연합학력평가`:`한국교육과정평가원 · ${J.year}학년도 ${J.month==='11월'?'대학수학능력시험':'대학수학능력시험 '+J.month+' 모의평가'} (홀수형)`}</dd><dt>${isG1(J)?'단원':'과목'}</dt><dd>${esc(isG1(J)?J.subj:J.part)}${J.topic?' · '+esc(J.topic):''}</dd><dt>형식</dt><dd>${J.choice?'5지선다형':'단답형'}</dd><dt>난이도</dt><dd><span class=\"stars\" style=\"--dc:${DC(J.stars)}\">${'★'.repeat(J.stars)}</span> ${RDN[J.stars]} · 제한 ${lim}분</dd>")
rep("    b.append(el('p','note','평가원 기출은 해설을 싣지 않습니다. EBSi(ebsi.co.kr) 기출문제 해설이나 교사의 풀이로 확인하세요. 같은 번호 자리의 창작 문항은 킬러관에 있습니다.'));",
    "    b.append(el('p','note',(isG1(J)?'학력평가 기출은 해설을 싣지 않습니다. EBSi(ebsi.co.kr) 해설이나 선생님의 풀이로 확인하세요.':'평가원 기출은 해설을 싣지 않습니다. EBSi(ebsi.co.kr) 기출문제 해설이나 선생님의 풀이로 확인하세요.')+(J.sim?' 이 문항은 다음 단계에 유사문항(쌍둥이 문제)이 있어요.':'')));")
# 유사문항: 한국어만 있으면 언어 버튼 숨김
rep("const ja2=!s.ko;if(ja2)ja=true;if(!ja2)b.append(langSeg(jaRefresh));", "const ja2=!s.ko;if(ja2)ja=true;else ja=false;if(!ja2&&s.ja)b.append(langSeg(jaRefresh));")

open(os.path.join(ROOT, 'template.html'), 'w', encoding='utf-8').write(s)
print('template.html 생성 (킬러 화면 + 루키 수정)')
