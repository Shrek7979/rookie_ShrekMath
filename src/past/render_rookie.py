"""평가원 문제지 PDF → 루키용(2~3점·쉬운 4점) 문항 잘라내기 + 정답 붙이기
사용: python render_rookie.py <공통.pdf> <확통.pdf> <미적.pdf> <기하.pdf> <킬러 answers.json>
킬러들의 수학몰 src/past/render_past.py 의 자르기 함수를 그대로 쓴다."""
import os, sys, json
KILLER_PAST = '/home/claude/killer_shrekmath/src/past'
sys.path.insert(0, KILLER_PAST)
import render_past as rp, parse_answers as pa
ROOT = os.path.dirname(os.path.abspath(__file__))
rp.IMG = os.path.join(ROOT, 'img'); os.makedirs(rp.IMG, exist_ok=True)
STAR_C = {1: 1, 2: 1, 3: 1, 4: 1, 5: 2, 6: 2, 7: 2, 8: 2, 9: 3, 10: 3, 16: 1, 17: 1, 18: 2, 19: 2}
STAR_S = {23: 1, 24: 1, 25: 2, 26: 2, 27: 3}
PLAN = {'c': (STAR_C, '공통'), 'k': (STAR_S, '확률과 통계'), 'm': (STAR_S, '미적분'), 'g': (STAR_S, '기하')}

def answers(pdf, known_path):
    known = {k: v for k, v in json.load(open(known_path, encoding='utf-8')).items() if not k.startswith('_')}
    res = {}
    for t in pa.tables(pdf):
        m = [ex for ex, d in known.items() if all(t.get(k) == v for k, v in d.items() if v is not None)]
        if len(m) == 1: res[m[0]] = t
        else: print('정답표 매칭 실패', m, len(t))
    return res

def main(pdfs, known):
    ans = answers(pdfs[0], known)
    out = []
    for key, pdf in zip('ckmg', pdfs):
        stars, subj = PLAN[key]
        span = 8 if key == 'c' else 4
        for y, mo, pg in rp.exams(pdf):
            got = rp.crop_items(pdf, pg, pg + span - 1, set(stars))
            ex = f'{y}-{mo[:-1].zfill(2)}'
            for n in sorted(stars):
                if n not in got: print('  missing', ex, key, n); continue
                iid = f'{ex}-{key}{n}'
                got[n].save(os.path.join(rp.IMG, iid + '.webp'), 'WEBP', quality=86, method=6)
                a = ans.get(ex, {}).get(f'{key}{n}')
                if a is None: print('  no answer', iid)
                out.append({'id': iid, 'year': y, 'month': mo, 'part': subj, 'num': n, 'stars': stars[n],
                            'choice': (n <= 15) if key == 'c' else (n <= 28), 'answer': a})
    out.sort(key=lambda x: (x['year'], x['month'], 'ckmg'.index(x['id'].split('-')[2][0]), x['num']))
    json.dump(out, open(os.path.join(ROOT, 'index.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(len(out), '문항')

if __name__ == '__main__':
    main(sys.argv[1:5], sys.argv[5])
