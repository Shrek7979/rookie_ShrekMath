"""고1 전국연합학력평가(교육청) 문제지 PDF → 루키용 문항 잘라내기 + 정답·출제의도 붙이기
사용: python render_g1.py <PDF 폴더>   (파일 이름: 2019년11월교육청_수리_문제.pdf / _정답.pdf)"""
import os, re, sys, json, subprocess
sys.path.insert(0, '/home/claude/killer_shrekmath/src/past')
import render_past as rp
ROOT = os.path.dirname(os.path.abspath(__file__))
rp.IMG = os.path.join(ROOT, 'img'); os.makedirs(rp.IMG, exist_ok=True)
STAR = {**{n: 1 for n in range(1, 6)}, **{n: 2 for n in range(6, 11)}, **{n: 3 for n in range(11, 15)}, 22: 1, 23: 1, 24: 2, 25: 2, 26: 3}
CIR = {'①': 1, '②': 2, '③': 3, '④': 4, '⑤': 5}


def answers(pdf):
    """정답표(첫 쪽 왼쪽 단)를 단어 좌표로 읽는다. 단답형 숫자가 수식 글꼴이라 글자로 안 나오면 그 칸만 OCR."""
    t = subprocess.run(['pdftotext', '-layout', pdf, '-'], capture_output=True, text=True).stdout
    intent = {}
    for m in re.finditer(r'(\d{1,2})\.\s*\[출제의도\]\s*([^\n]+?)(?:\s{3,}|\n)', t):
        intent.setdefault(int(m.group(1)), m.group(2).strip())
    pw, ph, ws = rp.words(pdf, 1)
    hd = [w for w in ws if w[4] == '답' and w[0] < pw * 0.4]
    y0 = min(w[1] for w in hd) if hd else 0
    tab = [w for w in ws if y0 < w[1] < y0 + 330 and w[0] < pw * 0.36]
    rows = {}
    for w in tab: rows.setdefault(round(w[1] / 8), []).append(w)
    ans, boxes = {}, {}
    for r in rows.values():
        r.sort(key=lambda w: w[0])
        if not r or not re.fullmatch(r'\d{1,2}', r[0][4]): continue
        first = int(r[0][4])
        if first % 5 != 1: continue
        # 번호 칸은 first, first+1, ... 순서로 왼쪽→오른쪽에 나온다. 그 사이 토큰이 값.
        labels, want = [], first
        for k, w in enumerate(r):
            if w[4] == str(want) and (not labels or w[0] - r[labels[-1]][2] > 12):
                labels.append(k); want += 1
        for li, k in enumerate(labels):
            n = first + li; end = labels[li + 1] if li + 1 < len(labels) else len(r)
            vals = r[k + 1:end]
            v = next((CIR[x[4]] for x in vals if x[4] in CIR), None)
            if v is None:
                v = next((int(x[4]) for x in vals if re.fullmatch(r'\d{1,3}', x[4])), None)
            if v is not None: ans[n] = v; continue
            x1 = r[end][0] - 2 if end < len(r) else r[k][2] + 75
            boxes[n] = (r[k][2] + 2, r[k][1] - 4, min(x1, r[k][2] + 80), r[k][3] + 4)
    # 두 번째 방법: 정답표 줄을 글자로 읽어 "번호 값" 쌍 찾기. 두 방법이 다르면 버린다(오답 정답 방지).
    lines = t.split('\n')
    k0 = next((i for i, l in enumerate(lines) if re.fullmatch(r'정\s+답', l.strip()[:5].strip()) or re.match(r'\s*정 답\s*$', l)), None)
    alt = {}
    if k0 is not None:
        for l in lines[k0 + 1:k0 + 40]:
            for m in re.finditer(r'(?<![\d.])(\d{1,2})\s+(①|②|③|④|⑤|\d{1,3})(?=\s|$)', l[:90]):
                n = int(m.group(1))
                if 1 <= n <= 30: alt.setdefault(n, CIR.get(m.group(2)) or int(m.group(2)))
    out = {}
    for n in set(ans) | set(alt):
        a, b = ans.get(n), alt.get(n)
        if a is not None and b is not None and a != b: continue
        v = a if a is not None else b
        # 단답형 값이 다음 번호처럼 보이는 경우(예: 22 → 23) 버린다
        if n >= 16 and v == n + 1: continue
        out[n] = v
    return out, intent


def cut_gap(im):
    """테두리 쪽 단 구분선(세로줄)을 지우고 아래 여백만 없앤다 (그림 속 빈칸에서 자르지 않음)."""
    im = im.convert('RGB'); w, h = im.size; g = im.convert('L'); px = g.load()
    for x in list(range(0, min(30, w))) + list(range(max(0, w - 30), w)):
        if sum(px[x, y] < 160 for y in range(h)) > h * 0.6:
            im.paste((255, 255, 255), (x, 0, x + 1, h)); g.paste(255, (x, 0, x + 1, h))
    last = 0
    for y in range(h):
        if any(px[x, y] < 200 for x in range(4, w - 4, 2)): last = y
    return im.crop((0, 0, w, min(h, last + 24)))


def _ink(px, y, xa, xb):
    return any(px[x, y] < 200 for x in range(xa, xb, 2))


TEXT = {}   # 마지막 crop_items 호출에서 문항별 글자 (단원 분류용)


def _climb(px, top, lim, xa, xb, gap=12):
    """top 줄에서 위로 올라가며 같은 줄에 붙은 글자(분수 분자·벡터 화살표·근호)를 찾는다.
    흰 줄이 gap 픽셀 넘게 이어지면 그 줄은 끝난 것. 반환: 가장 위 글자 줄."""
    hi = top; y = top - 1; run = 0
    while y > top - lim:
        if sum(px[x, y] < 160 for x in range(xa, xb, 4)) > (xb - xa) / 4 * 0.7: break   # 머리줄(가로 선)에서 멈춤
        if _ink(px, y, xa, xb): hi = y; run = 0
        else:
            run += 1
            if run > gap: break
        y -= 1
    return hi


def crop_items(pdf, first, last, wanted):
    """render_past.crop_items 와 같지만 단 경계를 실제 문항 번호 위치로 정한다 (A4·A3 문제지 모두).
    위·아래 경계는 번호 줄에서 시작해 글자(지수·분수)가 이어지는 동안만 넓히고, 흰 줄을 만나면 멈춘다
    → 윗부분이 잘리지도, 앞 문항·머리줄이 끼지도 않는다."""
    found = {}
    sc = rp.DPI / 72
    for pg in range(first, last + 1):
        pw, ph, ws = rp.words(pdf, pg)
        nums = [(w, int(w[4][:-1])) for w in ws if re.fullmatch(r'\d{1,2}\.', w[4])]
        left = [n for n in nums if n[0][0] < pw * 0.25]
        right = [n for n in nums if pw * 0.4 < n[0][0] < pw * 0.62]
        # 오른쪽 단 시작: 번호들의 x 중앙값 (본문 속 "3." 같은 숫자에 속지 않게)
        rxs = sorted(n[0][0] for n in right)
        rx = rxs[len(rxs) // 2] if rxs else pw / 2 + 8
        lxs = sorted(n[0][0] for n in left)
        lx = lxs[len(lxs) // 2] if lxs else 50
        right = [n for n in right if abs(n[0][0] - rx) < 30]
        left = [n for n in left if abs(n[0][0] - lx) < 30]
        # 왼쪽 단 오른쪽 끝: 글자가 rx-10 을 살짝 넘는 문제지가 있다 (2015년 9월 등)
        lmax = max([w[2] for w in ws if w[0] < rx - 20 and w[2] < rx + 2] or [rx - 10])
        lx1 = min(rx - 2, max(rx - 10, lmax + 3))
        img = None
        for lst, x0, x1 in ((left, lx - 6, lx1), (right, rx - 4, pw - lx + 8)):
            lst.sort(key=lambda n: n[0][1])
            for i, (w, n) in enumerate(lst):
                if n not in wanted or n in found: continue
                if img is None: img = rp.render(pdf, pg); gpx = img.convert('L').load()
                xa, xb = int((x0 + 6) * sc), int((x1 - 6) * sc)
                top = int(w[1] * sc); lim = int(22 * sc)
                y0 = max(0, _climb(gpx, top, lim, xa, xb) - 6)
                if i + 1 < len(lst):
                    nt = int(lst[i + 1][0][1] * sc)
                    y1 = _climb(gpx, nt, lim, xa, xb) - 2   # 다음 문항의 위 첨자·분수 윗부분 건너뛰기
                else:
                    y1 = int(ph * 0.88 * sc)
                y1 = min(y1, int(ph * 0.9 * sc))   # 쪽 번호 상자 빼기
                # 마지막 쪽 "※ 확인 사항" 상자 빼기
                chk = [t[1] for k, t in enumerate(ws) if x0 - 10 <= t[0] < x1 and w[1] < t[1] and t[1] * sc < y1
                       and t[4] == '확인' and k + 1 < len(ws) and ws[k + 1][4] == '사항']
                if chk: y1 = min(y1, int((min(chk) - 20) * sc))   # 상자 윗선까지 빼기
                found[n] = cut_gap(img.crop((int(x0 * sc), y0, int(max(x1, x0 + 200) * sc), y1)))
                TEXT[n] = ' '.join(t[4] for t in ws if x0 <= t[0] < x1 and y0 <= t[1] * sc < y1)
    return found


def main(d):
    out = []
    for f in sorted(os.listdir(d)):
        m = re.match(r'(\d{4})년(\d{1,2})월교육청_수리_문제\.pdf', f)
        if not m: continue
        y, mo = m.group(1), int(m.group(2)); pdf = os.path.join(d, f)
        ans, intent = answers(pdf.replace('_문제', '_정답'))
        n_pages = int(re.search(r'Pages:\s+(\d+)', subprocess.run(['pdfinfo', pdf], capture_output=True, text=True).stdout).group(1))
        got = crop_items(pdf, 1, n_pages, set(STAR))
        ex = f'g1-{y}-{mo:02d}'
        for n in sorted(STAR):
            if n not in got: print('  missing', ex, n); continue
            if n not in ans: print('  no answer', ex, n); continue
            iid = f'{ex}-{n}'
            got[n].save(os.path.join(rp.IMG, iid + '.webp'), 'WEBP', quality=86, method=6)
            out.append({'id': iid, 'year': y, 'month': f'{mo}월', 'part': '고1', 'num': n, 'stars': STAR[n],
                        'choice': n <= 21, 'answer': ans[n], 'topic': intent.get(n, '')})
        print(ex, len([x for x in out if x['id'].startswith(ex)]), '문항', '정답', len(ans), '출제의도', len(intent))
    json.dump(out, open(os.path.join(ROOT, 'index.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(len(out), '문항')


if __name__ == '__main__':
    main(sys.argv[1])
