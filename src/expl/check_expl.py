"""해설 파일(src/expl/*.py)의 A(해설이 도달한 정답)를 공식 정답(index.json)과 대조한다. build.py 가 먼저 실행한다."""
import os, sys, json, glob, importlib.util
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
ans = {}
for f in ('src/g1/index.json', 'src/past/index.json', 'src/g3/index.json'):
    for x in json.load(open(os.path.join(ROOT, f), encoding='utf-8')): ans[x['id']] = x['answer']
bad = []; n = 0
for f in sorted(glob.glob(os.path.join(ROOT, 'src', 'expl', '*.py'))):
    if f.endswith('check_expl.py'): continue
    spec = importlib.util.spec_from_file_location('e', f); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    for k in m.E:
        n += 1
        if k not in ans: bad.append(f'{k}: 없는 문항'); continue
        if k not in m.A: bad.append(f'{k}: A 없음'); continue
        if str(m.A[k]) != str(ans[k]): bad.append(f'{k}: 해설 {m.A[k]} ≠ 공식 {ans[k]}')
if bad: print('\n'.join(bad)); sys.exit(1)
print(f'해설 {n}개 정답 대조 통과')
