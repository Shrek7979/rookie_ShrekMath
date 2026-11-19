"""루키들의 수학몰 빌드: src/ → site/ (Vercel 정적 배포)
사용: python build.py"""
import os, re, json, shutil, time
from PIL import Image, ImageDraw
ROOT = os.path.dirname(os.path.abspath(__file__))
SITE = os.path.join(ROOT, 'site')
PAST = os.path.join(ROOT, 'src', 'past')
APP = os.path.join(ROOT, 'src', 'app')
PACKAGE = 'com.shrekmath.rookiemath'
G1 = os.path.join(ROOT, 'src', 'g1')
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


def unit(topic):
    for u, keys in UNITS:
        if any(k in topic for k in keys): return u
    return '기타'


def icon(size, pad=0.0):
    """초록 둥근 사각형 위 새싹(떡잎 두 장 + 줄기)"""
    S = 4 * size; im = Image.new('RGBA', (S, S), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    p = int(S * pad); d.rounded_rectangle((p, p, S - p, S - p), radius=int(S * .22), fill=(31, 157, 85, 255))
    cx, k = S / 2, (S - 2 * p) / 100
    y = lambda v: p + v * k; x = lambda v: p + v * k
    d.rounded_rectangle((cx - 3.2 * k, y(44), cx + 3.2 * k, y(80)), radius=int(3 * k), fill='#fffaf0')
    d.ellipse((x(18), y(26), x(52), y(50)), fill='#fffaf0')
    d.ellipse((x(48), y(18), x(84), y(46)), fill='#ffd36b')
    d.rounded_rectangle((x(28), y(78), x(72), y(84)), radius=int(3 * k), fill='#f07b22')
    return im.resize((size, size), Image.LANCZOS)


def main():
    shutil.rmtree(SITE, ignore_errors=True); os.makedirs(os.path.join(SITE, 'img'))
    items = json.load(open(os.path.join(PAST, 'index.json'), encoding='utf-8'))
    for x in items: x['key'] = x['id'].split('-')[2][0]; x['src'] = PAST
    g1 = json.load(open(os.path.join(G1, 'index.json'), encoding='utf-8'))
    for x in g1:
        x['key'] = 'h'; x['src'] = G1; x['unit'] = unit(re.sub(r'[\ue000-\uf8ff]', '', x.get('topic', '')))
        x['topic'] = re.sub(r'[\ue000-\uf8ff]', '', x['topic']).strip()
    items = g1 + items
    for x in items:
        im = Image.open(os.path.join(x.pop('src'), 'img', x['id'] + '.webp')).convert('RGB')
        g = im.convert('L').point(lambda v: 255 if v < 200 else 0); bb = g.getbbox()   # 글자 있는 영역
        if bb: im = im.crop((0, 0, min(im.width, bb[2] + 24), im.height))          # 오른쪽 빈 여백만 잘라 글자를 크게
        im.save(os.path.join(SITE, 'img', x['id'] + '.webp'), 'WEBP', quality=86, method=6)
        x['w'], x['h'] = im.size
    json.dump(items, open(os.path.join(SITE, 'list.json'), 'w', encoding='utf-8'), ensure_ascii=False, separators=(',', ':'))
    tpl = open(os.path.join(ROOT, 'template.html'), encoding='utf-8').read()
    open(os.path.join(SITE, 'index.html'), 'w', encoding='utf-8').write(tpl.replace('/*__INLINE_DATA__*/', ''))
    icon(192).save(os.path.join(SITE, 'icon-192.png')); icon(512).save(os.path.join(SITE, 'icon-512.png'))
    icon(512, pad=.12).save(os.path.join(SITE, 'icon-maskable.png')); icon(32).save(os.path.join(SITE, 'favicon-32.png'))
    json.dump({'name': '루키들의 수학몰', 'short_name': '루키수학몰', 'id': '/', 'start_url': '/', 'scope': '/', 'lang': 'ko',
               'display': 'standalone', 'background_color': '#fffaf0', 'theme_color': '#fffaf0', 'categories': ['education'],
               'description': '오늘의 루키가 내일의 킬러가 된다. 평가원 기출 2~3점 문항을 한 문제씩 풀고 바로 채점하는 수학 학습 앱',
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
    print(f'{len(items)}문항 → site/')


if __name__ == '__main__':
    main()
