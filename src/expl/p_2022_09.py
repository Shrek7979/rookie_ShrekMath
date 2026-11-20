"""2022학년도 9월 모의평가 (평가원) 2~3점 문항 해설 (ShrekMath 작성)"""
E = {
'2022-09-c1': '<b>핵심</b> 밑을 $3$으로 통일<br>$3^{-\\frac14}\\times3^{-\\frac74}=3^{-2}=\\dfrac19$',
'2022-09-c2': '<b>핵심</b> 다항함수의 미분<br>$f\'(x)=6x^2+4$, $f\'(1)=10$',
'2022-09-c3': '<b>핵심</b> $a_2a_4=a_1^2r^4$<br>$4r^4=36$ → $r^4=9$<br>$\\dfrac{a_7}{a_3}=r^4=9$',
'2022-09-c4': '<b>핵심</b> 연속 ⟺ $x=-1$에서 두 식의 값이 같다<br>$-2+a=1+5-a$ → $a=4$',
'2022-09-c5': '<b>핵심</b> $f\'(x)=6(x+2)(x-1)$<br>$M=f(-2)=21$, $m=f(1)=-6$<br>$M+m=15$',
'2022-09-c6': '<b>핵심</b> 통분하면 $\\dfrac{2\\sin^2\\theta}{1-\\sin^2\\theta}=2\\tan^2\\theta=4$<br>'
    '$\\tan^2\\theta=2$ → $\\cos^2\\theta=\\dfrac1{1+\\tan^2\\theta}=\\dfrac13$<br>제2사분면 → $\\cos\\theta=-\\dfrac{\\sqrt3}3$',
'2022-09-c7': '<b>핵심</b> $\\dfrac{a_{k+1}-a_k}{a_ka_{k+1}}=\\dfrac1{a_k}-\\dfrac1{a_{k+1}}$ (망원합)<br>'
    '$\\dfrac1{a_1}-\\dfrac1{a_{n+1}}=\\dfrac1n$<br>$n=12$: $-\\dfrac14-\\dfrac1{a_{13}}=\\dfrac1{12}$ → $a_{13}=-3$',
'2022-09-c8': '<b>핵심</b> 극한값 존재 → $f(0)=0$, $f(1)=0$, $f\'(0)=f\'(1)=1$<br>'
    '$f(x)=x(x-1)(ax+b)$: $f\'(0)=-b=1$, $f\'(1)=a+b=1$ → $a=2$, $b=-1$<br>$f(2)=2\\times1\\times3=6$',
'2022-09-c9': '<b>핵심</b> 가속도 $=v\'(t)$, 거리 $=\\displaystyle\\int|v|dt$<br>'
    '$-12k^2+24k=12$ → $k=1$<br>$t>3$에서 $v<0$: $\\displaystyle\\int_3^4(4t^3-12t^2)dt=\\left[t^4-4t^3\\right]_3^4=27$',
'2022-09-c10': '<b>핵심</b> 주기 $\\dfrac2b$, 최댓값 $a$인 점: $x=\\dfrac1{2b}$, $\\dfrac5{2b}$<br>'
    '기울기 곱 $\\dfrac{a}{\\frac1{2b}}\\times\\dfrac{a}{\\frac5{2b}}=\\dfrac{4a^2b^2}5=\\dfrac54$ → $ab=\\dfrac54$<br>'
    '넓이 $\\dfrac12\\times\\dfrac2b\\times a=\\dfrac ab=5$<br>$a=\\dfrac52$, $b=\\dfrac12$ → $3$',
'2022-09-c16': '<b>핵심</b> $2\\log_25=\\log_225$<br>$\\log_2\\dfrac{100}{25}=2$',
'2022-09-c17': '<b>핵심</b> 적분 후 $f(0)$으로 적분상수<br>$f(x)=2x^4-4x^3+7x+3$<br>$f(1)=8$',
'2022-09-c18': '<b>핵심</b> $\\displaystyle\\sum a_k=A$, $\\sum b_k=B$로 연립<br>$A+2B=45$, $A-B=3$ → $B=14$<br>$14-\\dfrac12\\times10=9$',
'2022-09-c19': '<b>핵심</b> 평균변화율 $=\\dfrac{f(4)-f(0)}4=-3$<br>'
    '$3a^2-12a+5=-3$ → $3a^2-12a+8=0$ (두 근 모두 $0<a<4$)<br>곱 $\\dfrac83$ → $p+q=11$',
'2022-09-k23': '<b>핵심</b> $\\mathrm E(X)=np$<br>$60\\times\\dfrac14=15$',
'2022-09-m23': '<b>핵심</b> 분자·분모를 $3^n$으로 나눈다<br>$\\dfrac{6+\\frac5{3^n}}{1+2\\left(\\frac23\\right)^n}\\to6$',
'2022-09-g23': '<b>핵심</b> $xy$평면 대칭 → $z$부호만<br>B$(3,0,2)$<br>$\\overline{\\mathrm{BC}}=\\sqrt{9+16+0}=5$',
'2022-09-k24': '<b>핵심</b> 전체 $16$가지, $ab>31$인 쌍<br>$(5,8)$, $(7,6)$, $(7,8)$ → $3$가지<br>$\\dfrac3{16}$',
'2022-09-m24': '<b>핵심</b> 덧셈정리<br>$\\tan\\alpha=\\dfrac23$<br>$\\dfrac{\\frac23+t}{1-\\frac23t}=1$ → $t=\\dfrac15$',
'2022-09-g24': '<b>핵심</b> 점근선 기울기 $\\pm\\dfrac ba$<br>$\\dfrac4a=3$ → $a=\\dfrac43$',
'2022-09-k25': '<b>핵심</b> 일반항 ${}_5\\mathrm C_ra^rx^{10-3r}$<br>'
    '$\\dfrac1{x^2}$: $r=4$ → $5a^4$ / $x$: $r=3$ → $10a^3$<br>$5a^4=10a^3$ → $a=2$',
'2022-09-m25': '<b>핵심</b> $\\dfrac{dy}{dx}=\\dfrac{dy/dt}{dx/dt}$<br>$t=\\ln2$: $\\dfrac{dx}{dt}=e^t+4e^{-t}=4$, $\\dfrac{dy}{dt}=1$<br>$\\dfrac14$',
'2022-09-g25': '<b>핵심</b> $\\vec p\\cdot\\vec a=3$ → $3p_x=3$, P는 직선 $x=1$ 위<br>'
    'Q는 중심 $(4,2)$, 반지름 $1$인 원 위<br>최솟값 $=3-1=2$',
'2022-09-k26': '<b>핵심</b> 조건부확률 $\\dfrac{\\mathrm P(\\text{5 이상}\\cap\\text{흰흰})}{\\mathrm P(\\text{흰흰})}$<br>'
    'A: $\\dfrac13\\times\\dfrac1{15}=\\dfrac1{45}$, B: $\\dfrac23\\times\\dfrac3{15}=\\dfrac6{45}$<br>$\\dfrac{1}{1+6}=\\dfrac17$',
'2022-09-m26': '<b>핵심</b> 단면 넓이 $y^2=\\dfrac3x+\\dfrac1{x^2}$<br>'
    '$\\left[3\\ln x-\\dfrac1x\\right]_1^2=3\\ln2+\\dfrac12$',
'2022-09-g26': '<b>핵심</b> $\\overline{\\mathrm{AB}}=\\overline{\\mathrm{AF}}=\\overline{\\mathrm{BF}}$ → 정삼각형, BF는 $x$축과 $60°$<br>'
    'F에서 BF 방향으로 $s$만큼: C$\\left(p-\\frac s2,\\ \\frac{\\sqrt3}2s\\right)$, $\\overline{\\mathrm{CF}}=$ 준선까지 거리 → $s=2p-\\dfrac s2$, $s=\\dfrac43p$<br>'
    '$\\overline{\\mathrm{BF}}=4p$ → $\\overline{\\mathrm{BC}}=\\dfrac83p$<br>$\\dfrac83p+4p=6$ → $p=\\dfrac9{10}$',
'2022-09-k27': '<b>핵심</b> $\\overline X\\sim\\mathrm N\\left(220,\\frac{\\sigma^2}n\\right)$, $\\overline Y\\sim\\mathrm N\\left(240,\\frac{(1.5\\sigma)^2}{9n}\\right)$<br>'
    '$0.1587$ → $z=-1$: $\\dfrac\\sigma{\\sqrt n}=5$<br>$\\overline Y$의 표준편차 $\\dfrac{1.5}3\\times5=2.5$<br>$\\mathrm P(Z\\ge-2)=0.9772$',
'2022-09-m27': '<b>핵심</b> 좌표로 첫 넓이, 다음 직사각형과의 닮음비<br>'
    'B$_1$ 원점, D$_1(2,1)$: E$_1(2-\\sqrt3,0)$, F$_1\\left(2-\\frac1{\\sqrt3},0\\right)$, $\\overline{\\mathrm{E_1F_1}}=\\dfrac2{\\sqrt3}$, H$_1$의 높이 $\\dfrac23$<br>'
    '$S_1=\\left(\\dfrac23-\\dfrac{2\\sqrt3}9\\right)+\\dfrac{\\sqrt3}9=\\dfrac23-\\dfrac{\\sqrt3}9$<br>'
    'C$_2(2h,1-h)$가 직선 E$_1$G$_1$: $y=x-2+\\sqrt3$ 위 → $h=1-\\dfrac{\\sqrt3}3$, 넓이비 $h^2=\\dfrac{4-2\\sqrt3}3$<br>'
    '$\\dfrac{S_1}{1-h^2}=\\dfrac{\\sqrt3}3$',
'2022-09-g27': '<b>핵심</b> AD $\\perp$ 평면 BCD → $\\overline{\\mathrm{AP}}=\\sqrt{9+\\overline{\\mathrm{DP}}^2}$<br>'
    '$\\overline{\\mathrm{DP}}$가 최소일 때 합도 최소: D에서 BC까지 거리 $\\dfrac{2\\times2\\sqrt3}{4}=\\sqrt3$<br>'
    '$\\sqrt{12}+\\sqrt3=3\\sqrt3$',
}
A = {'2022-09-c1': 1, '2022-09-c2': 5, '2022-09-c3': 5, '2022-09-c4': 4, '2022-09-c5': 3, '2022-09-c6': 1, '2022-09-c7': 4, '2022-09-c8': 2,
     '2022-09-c9': 3, '2022-09-c10': 3, '2022-09-c16': 2, '2022-09-c17': 8, '2022-09-c18': 9, '2022-09-c19': 11,
     '2022-09-k23': 3, '2022-09-m23': 3, '2022-09-g23': 5, '2022-09-k24': 3, '2022-09-m24': 2, '2022-09-g24': 4,
     '2022-09-k25': 2, '2022-09-m25': 4, '2022-09-g25': 2, '2022-09-k26': 1, '2022-09-m26': 2, '2022-09-g26': 3,
     '2022-09-k27': 5, '2022-09-m27': 3, '2022-09-g27': 1}
