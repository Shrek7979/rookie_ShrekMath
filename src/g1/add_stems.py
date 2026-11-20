"""[13~14]처럼 두 문항이 함께 쓰는 공통 지문(조건·그림)을 문항 이미지 위에 붙인다.
사용: python3 add_stems.py <교육청 PDF 폴더>   (render_g1.py 로 이미지를 다시 만든 뒤 실행)"""
import os, re, sys, json, glob
sys.path.insert(0, '/home/claude/killer_shrekmath/src/past'); sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import render_past as rp, render_g1 as g1
from PIL import Image
HERE = os.path.dirname(os.path.abspath(__file__))
idx = {x['id'] for x in json.load(open(os.path.join(HERE, 'index.json'), encoding='utf-8'))}
src = sys.argv[1]; done = []
for pdf in sorted(glob.glob(os.path.join(src, '*문제.pdf'))):
    m = re.match(r'(\d{4})년(\d+)월', os.path.basename(pdf)); ex = f'g1-{m[1]}-{int(m[2]):02d}'
    import subprocess
    n = int(re.search(r'Pages:\s+(\d+)', subprocess.run(['pdfinfo', pdf], capture_output=True, text=True).stdout)[1])
    for pg in range(1, n + 1):
        pw, ph, ws = rp.words(pdf, pg)
        for k, w in enumerate(ws):
            if not w[4].startswith('['): continue
            txt = ''.join(t[4] for t in ws[k:k + 5])
            mm = re.match(r'\[(\d+)[~～∼](\d+)\]', txt)
            if not mm: continue
            a, b = int(mm[1]), int(mm[2]); ids = [f'{ex}-{i}' for i in range(a, b + 1)]
            if not any(i in idx for i in ids): continue
            mid = pw / 2; left = w[0] < mid
            # 같은 단에서 [a~b] 아래 처음 나오는 문항 번호 a.
            first = [t for t in ws if t[4] == f'{a}.' and (t[0] < mid) == left and t[1] > w[1]]
            sc = rp.DPI / 72; img = rp.render(pdf, pg)
            x0 = (w[0] - 6) if left else (w[0] - 4)
            x1 = (mid - 3) if left else (pw - 36)
            y1 = (first[0][1] - 8) if first else ph * 0.9
            stem = g1.cut_gap(img.crop((int(x0 * sc), int((w[1] - 6) * sc), int(x1 * sc), int(y1 * sc))))
            for i in ids:
                f = os.path.join(HERE, 'img', i + '.webp')
                if i not in idx or not os.path.exists(f): continue
                it = Image.open(f).convert('RGB')
                s = stem.resize((it.width, int(stem.height * it.width / stem.width))) if stem.width != it.width else stem
                out = Image.new('RGB', (it.width, s.height + 10 + it.height), 'white')
                out.paste(s, (0, 0)); out.paste(it, (0, s.height + 10))
                out.save(f, 'WEBP', quality=86, method=6); done.append(i)
print(len(done), done)
