# 루키들의 수학몰

오늘의 루키가 내일의 킬러가 된다. 일반고 중하위권 학생을 위한 수학 문제 풀이 앱 — [킬러들의 수학몰](https://killershrekmath.vercel.app)의 짝.

- 고1 전국연합학력평가(2012~2020) 482문항 + 평가원 모의평가·수능(2022~2026) 435문항 + 고3 학력평가(2021~2025) 214문항 + 2023 수능대비 자기주도학습자료 77문항, 모든 문항 해설 포함
- 문항 출처: `src/g1`, `src/past`, `src/g3`(3점형 + 9·10번 도전), `src/sd`(자기주도학습자료) · 해설: `src/expl/*.py`
- 화면: 킬러들의 수학몰과 같은 코드(src/killer_template.html) + 루키용 수정(src/patch_template.py) → template.html
- 빌드: `python build.py` → `site/` (Vercel 정적 배포)
- 문항 자르기: `src/past/render_rookie.py`, `src/g1/render_g1.py`

ShrekMath
