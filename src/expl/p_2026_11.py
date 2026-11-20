"""2026학년도 수능 (평가원) 2~3점 문항 해설 (ShrekMath 작성)"""
E = {
'2026-11-c1': '<b>핵심</b> 밑을 $3$으로 통일<br>$9^{\\frac14}=3^{\\frac12}$<br>$3^{\\frac12}\\times3^{-\\frac12}=3^0=1$',
'2026-11-c2': '<b>핵심</b> 미분계수의 정의 $=f\'(1)$<br>$f\'(x)=9x^2+4$, $f\'(1)=13$',
'2026-11-c3': '<b>핵심</b> $\\Sigma$를 나눠 계산<br>$2\\displaystyle\\sum a_k-(1+2+3+4)=0$<br>$\\displaystyle\\sum_{k=1}^4a_k=5$',
'2026-11-c4': '<b>핵심</b> 연속 ⟺ $x=1$에서 두 식의 값이 같다<br>$3-2=1-3+a$, $a=3$',
'2026-11-c5': '<b>핵심</b> 곱의 미분법<br>$f\'(x)=(2x^2-x-2)+(x+2)(4x-1)$<br>$f\'(1)=-1+3\\times3=8$',
'2026-11-c6': '<b>핵심</b> 로그를 지수로<br>$b=a^3$, $\\dfrac ba=a^2=\\sqrt3$<br>$ab=a^4=3$, $\\log_93=\\dfrac12$',
'2026-11-c7': '<b>핵심</b> (위 곡선) − (아래 곡선)을 적분<br>$\\displaystyle\\int_0^2\\left(x^2+\\frac15x^2\\right)dx=\\frac65\\times\\frac83=\\frac{16}5$',
'2026-11-c8': '<b>핵심</b> $\\tan\\theta=-3$, $\\cos(\\pi-\\theta)=-\\cos\\theta>0$ → $\\cos\\theta<0$<br>'
    '제2사분면 → $\\sin\\theta=\\dfrac{3}{\\sqrt{10}}=\\dfrac{3\\sqrt{10}}{10}$',
'2026-11-c9': '<b>핵심</b> $y=5$가 접한다 ⟺ 극값이 $5$<br>'
    '$f\'(x)=3(x+3a)(x-a)$, 극댓값 $f(-3a)=27a^3+4=5$ → $a=\\dfrac13$<br>(극솟값 $f(a)=-5a^3+4<5$)<br>'
    '$f(x)=x^3+x^2-x+4$, $f(2)=14$',
'2026-11-c10': '<b>핵심</b> A$(t,\\ a^t-2)$, B$(t,0)$, C$(t,-2)$ (점근선 $y=-2$)<br>'
    '$\\overline{\\mathrm{AB}}=\\overline{\\mathrm{BC}}=2$ → $a^t=4$, $\\overline{\\mathrm{AC}}=4$<br>'
    '넓이 $\\dfrac12\\times4\\times t=8$ → $t=4$, $a^4=4$, $a=\\sqrt2$<br>$a\\times\\overline{\\mathrm{OB}}=4\\sqrt2=2^{\\frac52}$',
'2026-11-c16': '<b>핵심</b> 차례로 대입<br>$a_2=1\\times1+1=2$, $a_3=4\\times2+1=9$',
'2026-11-c17': '<b>핵심</b> 적분 후 $F(0)$으로 적분상수<br>$F(x)=x^4-x^2+4$<br>$F(2)=16-4+4=16$',
'2026-11-c18': '<b>핵심</b> 넓이 $=\\dfrac12bc\\sin A$<br>$\\sin A=\\dfrac45$<br>$\\dfrac12\\times5\\times6\\times\\dfrac45=12$',
'2026-11-c19': '<b>핵심</b> $|g(x)|\\le k$ ⟺ 범위에서 $g$의 최댓값·최솟값의 절댓값 이하<br>'
    '$g\'(x)=6(x+2)(x-1)$<br>$g(-2)=12$, $g(1)=-15$, $g(2)=-4$<br>$k$의 최솟값 $15$',
'2026-11-k23': '<b>핵심</b> 중복순열 ${}_n\\Pi_r=n^r$<br>$4^3=64$',
'2026-11-m23': '<b>핵심</b> $\\displaystyle\\lim_{x\\to0}\\frac{\\tan x}{x}=1$<br>$\\dfrac{\\tan6x}{6x}\\times3\\to3$',
'2026-11-g23': '<b>핵심</b> 성분끼리 더한다<br>$(3,0)$, 합 $3$',
'2026-11-k24': '<b>핵심</b> 곱셈정리와 덧셈정리<br>'
    '$\\mathrm P(A\\cap B)=\\dfrac25\\times\\dfrac14=\\dfrac1{10}$<br>$1=\\dfrac25+\\mathrm P(B)-\\dfrac1{10}$, $\\mathrm P(B)=\\dfrac7{10}$',
'2026-11-m24': '<b>핵심</b> 근호 안을 인수분해 → 치환적분<br>'
    '$\\sin x-\\sin^3x=\\sin x\\cos^2x$, $\\sqrt{\\ }=\\cos x\\sqrt{\\sin x}$ ($0\\le x\\le\\dfrac\\pi2$)<br>'
    '$\\sin x=t$: $\\displaystyle\\int_0^1\\sqrt t\\,dt=\\frac23$',
'2026-11-g24': '<b>핵심</b> $y^2=4px$의 초점과 준선 사이 거리 $2p$ (평행이동해도 같음)<br>$4p=12$, $p=3$ → $6$',
'2026-11-k25': '<b>핵심</b> (같은 색) + (다른 색인데 같은 수)<br>'
    '같은 색 $2\\times{}_5\\mathrm C_2=20$, 같은 수 $2,3,4,5$ → $4$<br>$\\dfrac{24}{45}=\\dfrac8{15}$',
'2026-11-m25': '<b>핵심</b> 샌드위치: $\\sqrt{9n^2-5}+2n\\approx5n$ → $\\dfrac{a_n}{n}\\to5$<br>'
    '분자·분모를 $n^2$으로 나누면 $\\dfrac{25}{5+5}=\\dfrac52$',
'2026-11-g25': '<b>핵심</b> $yz$평면 대칭: $x$부호만, 원점 대칭: 모두 부호 바꿈<br>'
    'B$(-3,-\\frac32,-2)$, C$(-3,\\frac32,2)$<br>$\\overline{\\mathrm{BC}}=\\sqrt{0+9+16}=5$',
'2026-11-k26': '<b>핵심</b> 신뢰구간의 폭 $=2\\times2.58\\times\\dfrac{\\sigma}{\\sqrt n}$<br>'
    '$2\\times2.58\\times\\dfrac56=4.3$<br>$a=1.2+4.3=5.5$',
'2026-11-m26': '<b>핵심</b> 단면이 한 변 $y$인 정삼각형 → 넓이 $\\dfrac{\\sqrt3}4y^2$를 적분<br>'
    '$\\dfrac{\\sqrt3}4\\displaystyle\\int_1^2(x+x\\ln x)dx=\\frac{\\sqrt3}4\\left(\\frac32+2\\ln2-\\frac34\\right)$<br>'
    '$=\\dfrac{\\sqrt3(3+8\\ln2)}{16}$',
'2026-11-g26': '<b>핵심</b> $y^2-x^2=a^2$, 초점 $(0,\\pm\\sqrt2a)$, 접선 공식<br>'
    '접선 $\\sqrt2y-x=a$ → P$\\left(0,\\dfrac a{\\sqrt2}\\right)$<br>'
    '$\\left(\\sqrt2a-\\dfrac a{\\sqrt2}\\right)\\left(\\sqrt2a+\\dfrac a{\\sqrt2}\\right)=\\dfrac32a^2=8$<br>$a=\\dfrac{4\\sqrt3}{3}$',
'2026-11-k27': '<b>핵심</b> 확률의 합 $=1$로 $a$, $\\mathrm V(cX)=c^2\\mathrm V(X)$<br>'
    '$\\dfrac{1+1+3+5}{12}+a=1$, $a=\\dfrac16$<br>$\\mathrm E(X)=\\dfrac52$, $\\mathrm E(X^2)=\\dfrac{15}2$, $\\mathrm V(X)=\\dfrac54$<br>$\\mathrm V(6X)=36\\times\\dfrac54=45$',
'2026-11-m27': '<b>핵심</b> 만나는 점의 $t$를 찾고 $\\dfrac{dy}{dx}=\\dfrac{dy/dt}{dx/dt}$<br>'
    '$t=\\dfrac14$: $x=\\dfrac32e$, $y=-\\dfrac e2=3x-5e$ ✓<br>'
    '$\\dfrac{dx}{dt}=e(6+\\pi)$, $\\dfrac{dy}{dt}=e(3\\pi-2)$<br>기울기 $\\dfrac{3\\pi-2}{\\pi+6}$',
'2026-11-g27': '<b>핵심</b> AB는 지름 → CD ∥ AB인 등변사다리꼴로 좌표 설정<br>'
    'A$(-\\frac52,0,0)$, B$(\\frac52,0,0)$, D$(-\\frac32,2,h)$, H$(-\\frac32,2,0)$<br>'
    '$\\triangle\\mathrm{ABH}=\\dfrac12\\times5\\times2=5$<br>ABCD $=\\dfrac{5+3}{2}\\sqrt{4+h^2}=20$ → $h^2=21$, $h=\\sqrt{21}$',
}
A = {'2026-11-c1': 1, '2026-11-c2': 4, '2026-11-c3': 5, '2026-11-c4': 3, '2026-11-c5': 3, '2026-11-c6': 2, '2026-11-c7': 5, '2026-11-c8': 1,
     '2026-11-c9': 4, '2026-11-c10': 3, '2026-11-c16': 9, '2026-11-c17': 16, '2026-11-c18': 12, '2026-11-c19': 15,
     '2026-11-k23': 3, '2026-11-m23': 3, '2026-11-g23': 3, '2026-11-k24': 1, '2026-11-m24': 4, '2026-11-g24': 1,
     '2026-11-k25': 2, '2026-11-m25': 3, '2026-11-g25': 5, '2026-11-k26': 5, '2026-11-m26': 1, '2026-11-g26': 2,
     '2026-11-k27': 4, '2026-11-m27': 2, '2026-11-g27': 4}
