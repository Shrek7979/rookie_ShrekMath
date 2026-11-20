"""2023학년도 수능 (평가원) 2~3점 문항 해설 (ShrekMath 작성)"""
E = {
'2023-11-c1': '<b>핵심</b> 밑을 $2$로 통일<br>$\\dfrac4{2^{\\sqrt2}}=2^{2-\\sqrt2}$<br>$2^{(2-\\sqrt2)(2+\\sqrt2)}=2^2=4$',
'2023-11-c2': '<b>핵심</b> 분자·분모를 $x$로 나눈다<br>$\\dfrac{\\sqrt{1-\\frac2{x^2}}+3}{1+\\frac5x}\\to4$',
'2023-11-c3': '<b>핵심</b> $\\dfrac{a_4+a_6}{a_2+a_4}=r^2=\\dfrac14$ → $r=\\dfrac12$<br>$a_1\\left(\\dfrac12+\\dfrac18\\right)=30$ → $a_1=48$',
'2023-11-c4': '<b>핵심</b> 곱의 미분법<br>$g\'(x)=2xf(x)+x^2f\'(x)$<br>$g\'(2)=4\\times1+4\\times3=16$',
'2023-11-c5': '<b>핵심</b> $\\cos\\left(\\dfrac\\pi2+\\theta\\right)=-\\sin\\theta$<br>$\\sin\\theta=-\\dfrac{\\sqrt5}5$, $\\tan\\theta<0$ → $\\cos\\theta>0$<br>$\\cos\\theta=\\dfrac{2\\sqrt5}5$',
'2023-11-c6': '<b>핵심</b> $f\'(1)=0$으로 $a$, 다른 근이 $b$<br>$6-18+a=0$, $a=12$<br>$f\'(x)=6(x-1)(x-2)$ → $b=2$<br>$a+b=14$',
'2023-11-c7': '<b>핵심</b> $a_n=nd$, 분모 유리화 → 망원합<br>'
    '$\\dfrac1{\\sqrt{a_k}+\\sqrt{a_{k+1}}}=\\dfrac{\\sqrt{a_{k+1}}-\\sqrt{a_k}}d$<br>'
    '합 $=\\dfrac{\\sqrt{16d}-\\sqrt d}d=\\dfrac3{\\sqrt d}=2$ → $d=\\dfrac94$<br>$a_4=4d=9$',
'2023-11-c8': '<b>핵심</b> 접점을 $(t,\\ t^3-t+2)$로 두고 $(0,4)$ 대입<br>'
    '$4=(3t^2-1)(0-t)+t^3-t+2$ → $t^3=-1$, $t=-1$<br>접선 $y=2x+4$ → $x$절편 $-2$',
'2023-11-c9': '<b>핵심</b> $-\\sqrt3\\tan2x$는 감소 → 왼쪽 끝이 최대, 오른쪽 끝이 최소<br>'
    '$f\\left(-\\dfrac\\pi6\\right)=a+3=7$ → $a=4$<br>$f(b)=4-\\sqrt3\\tan2b=3$ → $2b=\\dfrac\\pi6$, $b=\\dfrac\\pi{12}$<br>$ab=\\dfrac\\pi3$',
'2023-11-c10': '<b>핵심</b> $A=B$ ⟺ $\\displaystyle\\int_0^2\\{(-x^2+k)-(x^3+x^2)\\}dx=0$<br>'
    '$2k-\\dfrac{16}3-4=0$ → $k=\\dfrac{14}3$',
'2023-11-c16': '<b>핵심</b> $2=\\log_24$로 바꿔 진수 비교<br>$3x+2=4(x-2)$ → $x=10$',
'2023-11-c17': '<b>핵심</b> 적분 후 $f(0)$으로 적분상수<br>$f(x)=x^4-x^2+3$<br>$f(2)=16-4+3=15$',
'2023-11-c18': '<b>핵심</b> $\\Sigma$를 나눠 계산<br>$3\\displaystyle\\sum a_k+25=55$ → $\\sum a_k=10$<br>$\\sum b_k=32-10=22$',
'2023-11-c19': '<b>핵심</b> $2x^3-6x^2=-k$ → 그래프와 직선 $y=-k$<br>'
    '극댓값 $g(0)=0$, 극솟값 $g(2)=-8$<br>양의 근 $2$개 ⟺ $-8<-k<0$ → $k=1,\\cdots,7$<br>$7$개',
'2023-11-k23': '<b>핵심</b> 이항정리: $x^9=(x^3)^3$<br>${}_5\\mathrm C_3\\times3^2=90$',
'2023-11-m23': '<b>핵심</b> 분모 유리화 + $\\dfrac{\\ln(1+x)}x\\to1$<br>$\\dfrac{\\ln(x+1)}{x}(\\sqrt{x+4}+2)\\to1\\times4=4$',
'2023-11-g23': '<b>핵심</b> $x$축 대칭 → $y$, $z$ 부호 바뀜<br>B$(2,-2,1)$<br>$\\overline{\\mathrm{BC}}=\\sqrt{16+9+0}=5$',
'2023-11-k24': '<b>핵심</b> 천의 자리 $4,5$ / 일의 자리 홀수 $1,3,5$<br>$2\\times5\\times5\\times3=150$',
'2023-11-m24': '<b>핵심</b> 구분구적법 $\\dfrac1n\\displaystyle\\sum f\\left(\\frac kn\\right)\\to\\int_0^1f(x)dx$<br>'
    '$\\displaystyle\\int_0^1\\sqrt{1+3x}\\,dx=\\left[\\frac29(1+3x)^{\\frac32}\\right]_0^1=\\frac29(8-1)=\\frac{14}9$',
'2023-11-g24': '<b>핵심</b> 초점 $(p,0)$, 준선 $x=-p$ → $y^2=4px$<br>$p=\\dfrac13$: $y^2=\\dfrac43x$<br>$4=\\dfrac43a$ → $a=3$',
'2023-11-k25': '<b>핵심</b> 여사건: 모두 검은색<br>$1-\\dfrac{{}_9\\mathrm C_3}{{}_{14}\\mathrm C_3}=1-\\dfrac{84}{364}=\\dfrac{10}{13}$',
'2023-11-m25': '<b>핵심</b> 분모는 $\\dfrac{4^n}2$이 지배 → 공비 $4$여야 극한이 $0$이 아닌 값<br>'
    '$a_n=a\\times4^{n-1}$: $\\dfrac{a\\cdot4^{n-1}}{\\frac12\\cdot4^n}\\to\\dfrac a2=3$ → $a=6$<br>$a_2=24$',
'2023-11-g25': '<b>핵심</b> 접선 기울기 $-\\dfrac{b^2x_1}{a^2y_1}$, 점 대입<br>'
    '$-\\dfrac{2b^2}{a^2}=-\\dfrac12$ → $a^2=4b^2$<br>$\\dfrac4{4b^2}+\\dfrac1{b^2}=1$ → $b^2=2$, $a^2=8$<br>$c=\\sqrt6$, $2c=2\\sqrt6$',
'2023-11-k26': '<b>핵심</b> 공은 모두 $6$개, $\\mathrm P(A\\cup B)=\\mathrm P(A)+\\mathrm P(B)-\\mathrm P(A\\cap B)$<br>'
    '$A$: $2\\times{}_4\\mathrm C_2=12$ / $B$(2 세 개): ${}_4\\mathrm C_3=4$ / $A\\cap B$: 흰 2 + 검은 2 두 개 $=3$<br>'
    '$\\dfrac{12+4-3}{{}_6\\mathrm C_3}=\\dfrac{13}{20}$',
'2023-11-m26': '<b>핵심</b> 단면 넓이 $y^2=\\sec^2x+\\tan x$<br>'
    '$\\displaystyle\\int_0^{\\frac\\pi3}(\\sec^2x+\\tan x)dx=\\left[\\tan x-\\ln\\cos x\\right]_0^{\\frac\\pi3}=\\sqrt3+\\ln2$',
'2023-11-g26': '<b>핵심</b> $(\\vec p-\\vec a)\\cdot(\\vec p-\\vec b)=0$ → 지름이 AB인 원: 중심 $(2,6)$, 반지름 $2$<br>'
    '$\\vec q$의 끝점: 직선 $y=2$<br>최솟값 $=(\\text{중심과 직선 사이 거리})-(\\text{반지름})=4-2=2$',
'2023-11-k27': '<b>핵심</b> 신뢰구간의 길이 $2z\\dfrac{\\sigma}{\\sqrt n}$<br>'
    '$2\\times1.96\\times\\dfrac\\sigma4=9.8$ → $\\sigma=10$<br>$2\\times2.58\\times\\dfrac{10}{\\sqrt n}\\le6$ → $\\sqrt n\\ge8.6$, $n\\ge73.96$<br>최솟값 $74$',
'2023-11-m27': '<b>핵심</b> 첫 그림의 넓이와 닮음비(넓이비)만 구하면 등비급수<br>'
    'P$_1\\left(\\dfrac35,\\dfrac45\\right)$, $\\overline{\\mathrm{P_1A_1}}^2=\\dfrac45$ → 색칠 넓이 $\\dfrac{\\overline{\\mathrm{P_1A_1}}^2}4=\\dfrac15$<br>'
    'Q$_1\\left(\\dfrac25,\\dfrac15\\right)$, $\\overline{\\mathrm{OQ_1}}^2=\\dfrac15$ → 공비 $\\dfrac15$<br>'
    '$\\dfrac{\\frac15}{1-\\frac15}=\\dfrac14$',
'2023-11-g27': '<b>핵심</b> $\\overline{\\mathrm{AC}}=1$로 두고 길이로 계산<br>'
    'C의 높이 $\\sin\\left(\\dfrac\\pi2-\\theta_1\\right)=\\dfrac35$ → 정사영 C\'에서 $\\overline{\\mathrm{AC\'}}=\\dfrac45$<br>'
    'AB 방향 성분 $\\cos\\theta_1=\\dfrac35$ → C\'에서 직선 AB까지 $\\sqrt{\\frac{16}{25}-\\frac9{25}}=\\dfrac{\\sqrt7}5$<br>'
    'C에서 직선 AB까지 $\\sin\\theta_1=\\dfrac45$ → $\\cos\\theta_2=\\dfrac{\\sqrt7/5}{4/5}=\\dfrac{\\sqrt7}4$',
}
A = {'2023-11-c1': 5, '2023-11-c2': 4, '2023-11-c3': 1, '2023-11-c4': 3, '2023-11-c5': 5, '2023-11-c6': 2, '2023-11-c7': 4, '2023-11-c8': 4,
     '2023-11-c9': 3, '2023-11-c10': 4, '2023-11-c16': 10, '2023-11-c17': 15, '2023-11-c18': 22, '2023-11-c19': 7,
     '2023-11-k23': 3, '2023-11-m23': 4, '2023-11-g23': 5, '2023-11-k24': 2, '2023-11-m24': 3, '2023-11-g24': 3,
     '2023-11-k25': 5, '2023-11-m25': 5, '2023-11-g25': 4, '2023-11-k26': 3, '2023-11-m26': 4, '2023-11-g26': 2,
     '2023-11-k27': 2, '2023-11-m27': 2, '2023-11-g27': 1}
