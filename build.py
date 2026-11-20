"""루키들의 수학몰 빌드: 킬러들의 수학몰과 같은 화면(template.html) + 루키 문항 → site/ (Vercel 정적 배포)
사용: python build.py
  1) src/patch_template.py 로 킬러 화면(src/killer_template.html)에서 template.html 을 만든다
  2) 문항(고1 학력평가, 평가원 기출)과 유사문항을 킬러 '기출관' 형식(jlist.json)으로 내보낸다"""
import os, re, json, shutil, time, subprocess, sys, glob, importlib.util
from PIL import Image, ImageDraw
ROOT = os.path.dirname(os.path.abspath(__file__))
SITE = os.path.join(ROOT, 'site')
PAST = os.path.join(ROOT, 'src', 'past')
G1 = os.path.join(ROOT, 'src', 'g1')
APP = os.path.join(ROOT, 'src', 'app')
PACKAGE = 'com.shrekmath.rookiemath'
CIRC = '①②③④⑤'

# 고1 학력평가 출제의도 → 2022 개정 공통수학 단원 (앞에서부터 먼저 맞는 것)
UNITS = [
    ('도형의 방정식', ['부등식의 영역', '두 점 사이', '내분점', '외분점', '직선', '원의 방정식', '원과 직선', '평행이동', '대칭이동', '도형의 이동', '점의 평행', '내분']),
    ('이차함수', ['이차함수']),
    ('중학 복습', ['제곱근', '피타고라스', '삼각비', '닮음', '일차함수', '순환소수', '유리수', '최소공배수', '소수와 약수', '히스토그램', '상대도수', '표준편차', '원의 성질', '원에서', '삼각형', '사다리꼴', '수직선', '입체도형', '일차방정식', '규칙성', '실수의', '절댓값의', '거듭제곱', '도수', '무리수의 뜻', '줄기', '최빈값', '유한소수', '회전체', '원주각', '부채꼴', '대푯값', '지수', '평균']),
    ('집합과 명제', ['집합', '명제', '필요조건', '충분조건', '필요충분', '진리집합', '드 모르간', '서로소', '절대부등식']),
    ('함수', ['합성', '역함수', '함수의 뜻', '유리함수', '무리함수', '유리식', '무리식', '함수 이해']),
    ('경우의 수·확률·수열', ['경우의', '확률', '수열', '등차', '등비']),
    ('복소수·이차방정식', ['복소수', '이차방정식', '판별식', '근과 계수', '실근', '허근']),
    ('여러 방정식·부등식', ['삼차방정식', '사차방정식', '연립', '부등식', '절댓값']),
    ('다항식', ['다항식', '곱셈공식', '곱셈 공식', '인수분해', '나머지', '인수정리', '조립제법', '항등식', '미정계수', '최대공약수', '분모의 유리화']),
]
PUA = re.compile(r'[-]')


def unit(topic):
    for u, keys in UNITS:
        if any(k in topic for k in keys): return u
    return '기타'


def icon(size, pad=0.0):
    """새싹 아이콘: src/app/icon.svg 를 1024px 로 그려 둔 PNG 를 줄여 쓴다 (pad>0 이면 마스커블용)"""
    f = 'icon-maskable-1024.png' if pad else 'icon-1024.png'
    return Image.open(os.path.join(ROOT, 'src', 'app', f)).convert('RGBA').resize((size, size), Image.LANCZOS)


def blocks(html):
    """유사문항 문제 문자열(KaTeX $…$, <br>, 표) → 킬러 화면의 블록 [{p:…},{box:[…]}]"""
    html = html.replace('&lsquo;', '‘').replace('&rsquo;', '’')
    out = []
    for part in re.split(r'(<table class="mt">.*?</table>)', html):
        if part.startswith('<table'):
            rows = re.findall(r'<tr>(.*?)</tr>', part)
            out.append({'box': [' · '.join(re.sub(r'<[^>]+>', '', c).strip() for c in re.findall(r'<t[hd]>(.*?)</t[hd]>', r)) for r in rows]})
        else:
            for line in re.split(r'<br\s*/?>', part):
                line = line.strip()
                if line: out.append({'p': line})
    return out


def sim_of(m):
    q = blocks(m['q'])
    if m['ch']: q.append({'ch': [c.strip()[1:-1] if c.strip().startswith('$') and c.strip().endswith('$') else c for c in m['ch']]})
    ans = f"{CIRC[m['a'] - 1]} {m['ch'][m['a'] - 1]}" if m['ch'] else f"${m['a']}$"
    return {'ko': q, 'ans': {'ko': ans}, 'sol': {'ko': blocks(m['sol'])}}


def main():
    subprocess.run([sys.executable, os.path.join(ROOT, 'src', 'patch_template.py')], check=True)
    shutil.rmtree(SITE, ignore_errors=True); os.makedirs(os.path.join(SITE, 'img'))
    sims = {}
    G3U = {}
    expls = {}   # 원문항 해설: src/expl/*.py 의 E = {id: '해설 문자열'}
    subprocess.run([sys.executable, os.path.join(ROOT, 'src', 'expl', 'check_expl.py')], check=True)
    for f in sorted(glob.glob(os.path.join(ROOT, 'src', 'expl', '*.py'))):
        if f.endswith('check_expl.py'): continue
        spec = importlib.util.spec_from_file_location('e', f); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
        expls.update(m.E); G3U.update(getattr(m, 'U', {}))
    for f in sorted(glob.glob(os.path.join(ROOT, 'src', 'sim', 'batch*.py'))):
        spec = importlib.util.spec_from_file_location('b', f); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
        sims.update(m.S)
    g1 = json.load(open(os.path.join(G1, 'index.json'), encoding='utf-8'))
    past = json.load(open(os.path.join(PAST, 'index.json'), encoding='utf-8'))
    PU = json.load(open(os.path.join(PAST, 'units.json'), encoding='utf-8'))   # 평가원 문항 단원(문항을 보고 분류)
    J = []
    for x in g1:   # 고1 기초관: 최신 시험부터
        t = PUA.sub('', x.get('topic', '')).strip(); u = unit(t)
        J.append({'kind': 'past', 'id': x['id'], 'year': x['year'], 'month': x['month'], 'num0': x['num'], 'stars': x['stars'],
                  'univ': f"{x['year']}년 {x['month']} 고1 학력평가", 'track': f"{x['num']}번 · {u}", 'part': '고1', 'subj': u, 'topic': t,
                  'text': t or u, 'answer': x['answer'], 'choice': x['choice'], 'src': G1})
    for x in past:
        mon = '수능' if x['month'] == '11월' else x['month'] + ' 모평'
        J.append({'kind': 'past', 'id': x['id'], 'year': x['year'], 'month': x['month'], 'num0': x['num'], 'stars': x['stars'],
                  'univ': f"{x['year']}학년도 {mon}", 'track': f"{x['part']} {x['num']}번 · {PU.get(x['id'], '')}", 'unit': PU.get(x['id'], ''), 'part': x['part'], 'subj': x['part'],
                  'text': f"{x['year']}학년도 {mon} {x['part']} {x['num']}번", 'answer': x['answer'], 'choice': x['choice'], 'src': PAST})
    # 고3 교육청 학력평가 3점 문항 (2021~2025): src/g3 — 단원은 해설 파일의 U
    G3 = os.path.join(ROOT, 'src', 'g3')
    for x in json.load(open(os.path.join(G3, 'index.json'), encoding='utf-8')):
        if x['id'] not in expls: continue   # 해설을 다 쓴 문항만 올린다
        u = G3U.get(x['id'], '')
        J.append({'kind': 'past', 'id': x['id'], 'year': x['year'], 'month': x['month'], 'num0': x['num'], 'stars': 1 if x['num'] <= 5 else 2,
                  'univ': f"{x['year']}년 {x['month']} 고3 학력평가", 'track': f"공통 {x['num']}번 · {u}", 'unit': u, 'part': '공통', 'subj': '공통',
                  'text': f"{x['year']}년 {x['month']} 고3 학력평가 {x['num']}번", 'answer': x['answer'], 'choice': x['choice'], 'src': G3})
    for i, x in enumerate(J, 1):
        im = Image.open(os.path.join(x.pop('src'), 'img', x['id'] + '.webp')).convert('RGB')
        g = im.convert('L').point(lambda v: 255 if v < 200 else 0); bb = g.getbbox()
        if bb: im = im.crop((0, 0, min(im.width, bb[2] + 24), im.height))   # 오른쪽 빈 여백만 잘라 글자를 크게
        im.save(os.path.join(SITE, 'img', x['id'] + '.webp'), 'WEBP', quality=86, method=6)
        x['num'] = i; x['qimg'] = ['img/' + x['id'] + '.webp']; x['simg'] = []; x['art'] = ''
        if x['id'] in sims: x['sim'] = sim_of(sims[x['id']])
        if x['id'] in expls:
            eb = blocks(expls[x['id']].replace('<b>', '**').replace('</b>', '**'))
            if eb and eb[0].get('p', '').startswith('**핵심**'): eb[0] = {'box': [eb[0]['p']]}   # 핵심 개념은 상자로
            x['expl'] = eb
    J = [{k: x[k] for k in ['num'] + [k for k in x if k != 'num']} for x in J]
    dump = lambda name, obj: json.dump(obj, open(os.path.join(SITE, name), 'w', encoding='utf-8'), ensure_ascii=False, separators=(',', ':'))
    dump('jlist.json', J); dump('list.json', []); dump('elist.json', []); dump('cats.json', {})

    tpl = open(os.path.join(ROOT, 'template.html'), encoding='utf-8').read()
    tpl = tpl.replace('/*__KATEX_CSS__*/', open(os.path.join(ROOT, 'src', 'katex.inline.css'), encoding='utf-8').read())
    skeleton = ('<!doctype html>\n<html lang="ko">\n<head>\n<meta charset="utf-8">\n'
                '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">\n'
                '<meta name="description" content="루키들의 수학몰 · 고1·고3 학력평가와 평가원 기출의 2~3점 문항을 시험처럼 풀고 바로 채점">\n'
                '<meta name="theme-color" content="#fdf9f6">\n'
                '<meta name="apple-mobile-web-app-capable" content="yes"><meta name="apple-mobile-web-app-status-bar-style" content="black-translucent"><meta name="apple-mobile-web-app-title" content="루키수학몰">\n'
                '<link rel="manifest" href="manifest.json">\n'
                '<link rel="icon" type="image/png" sizes="32x32" href="favicon-32.png">\n'
                '<link rel="icon" type="image/png" sizes="16x16" href="favicon-16.png">\n'
                '<link rel="apple-touch-icon" sizes="180x180" href="apple-touch-icon.png">\n'
                '<meta property="og:title" content="루키들의 수학몰"><meta property="og:image" content="https://rookieshrekmath.vercel.app/og-v2.png"><meta property="og:type" content="website"><meta property="og:url" content="https://rookieshrekmath.vercel.app/"><meta property="og:description" content="고1·고3 학력평가와 평가원 기출의 2~3점 문항을 시험처럼 풀고 바로 채점"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630"><meta name="twitter:card" content="summary_large_image">\n'
                '<style>:root{padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}img{max-width:100%}</style>\n'
                '<script>if("serviceWorker" in navigator)addEventListener("load",()=>navigator.serviceWorker.register("/sw.js").catch(()=>{}))</script>\n'
                '</head>\n<body>\n__BODY__\n</body>\n</html>\n')
    open(os.path.join(SITE, 'index.html'), 'w', encoding='utf-8').write(skeleton.replace('__BODY__', tpl.replace('/*__INLINE_DATA__*/', '')))

    icon(192).save(os.path.join(SITE, 'icon-192.png')); icon(512).save(os.path.join(SITE, 'icon-512.png'))
    icon(512, pad=.12).save(os.path.join(SITE, 'icon-maskable.png')); fav = Image.open(os.path.join(ROOT, 'src', 'app', 'favicon-1024.png')).convert('RGBA')
    fav.resize((32, 32), Image.LANCZOS).save(os.path.join(SITE, 'favicon-32.png')); fav.resize((16, 16), Image.LANCZOS).save(os.path.join(SITE, 'favicon-16.png'))
    fav.resize((48, 48), Image.LANCZOS).save(os.path.join(SITE, 'favicon.ico'), sizes=[(16, 16), (32, 32), (48, 48)])
    Image.open(os.path.join(ROOT, 'src', 'app', 'icon-square-1024.png')).resize((180, 180), Image.LANCZOS).save(os.path.join(SITE, 'apple-touch-icon.png'))
    shutil.copy(os.path.join(ROOT, 'src', 'app', 'og.png'), os.path.join(SITE, 'og.png')); shutil.copy(os.path.join(ROOT, 'src', 'app', 'og.png'), os.path.join(SITE, 'og-v2.png'))
    json.dump({'name': '루키들의 수학몰', 'short_name': '루키수학몰', 'id': '/', 'start_url': '/', 'scope': '/', 'lang': 'ko',
               'display': 'standalone', 'background_color': '#fdf9f6', 'theme_color': '#192c46', 'categories': ['education'],
               'description': '오늘의 루키가 내일의 킬러가 된다. 고1·고3 학력평가와 평가원 기출의 2~3점 문항을 시험처럼 풀고 바로 채점하는 수학 학습 앱',
               'icons': [{'src': 'icon-192.png', 'sizes': '192x192', 'type': 'image/png'}, {'src': 'icon-512.png', 'sizes': '512x512', 'type': 'image/png'},
                         {'src': 'icon-maskable.png', 'sizes': '512x512', 'type': 'image/png', 'purpose': 'maskable'}]},
              open(os.path.join(SITE, 'manifest.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    sw = open(os.path.join(APP, 'sw.js'), encoding='utf-8').read().replace('__VERSION__', time.strftime('%Y%m%d%H%M%S'))
    open(os.path.join(SITE, 'sw.js'), 'w', encoding='utf-8').write(sw)
    shutil.copy(os.path.join(APP, 'privacy.html'), os.path.join(SITE, 'privacy.html'))
    fp = os.path.join(APP, 'sha256.txt')
    if os.path.exists(fp):
        fps = [l.strip() for l in open(fp, encoding='utf-8') if l.strip() and not l.startswith('#')]
        if fps:
            os.makedirs(os.path.join(SITE, '.well-known'))
            json.dump([{'relation': ['delegate_permission/common.handle_all_urls'], 'target': {'namespace': 'android_app', 'package_name': PACKAGE, 'sha256_cert_fingerprints': fps}}],
                      open(os.path.join(SITE, '.well-known', 'assetlinks.json'), 'w'), indent=1)
    print(f"{len(J)}문항 (고1 {sum(x['part'] == '고1' for x in J)} · 평가원 {sum(x['part'] != '고1' for x in J)} · 유사문항 {sum('sim' in x for x in J)}) → site/")


if __name__ == '__main__':
    main()
