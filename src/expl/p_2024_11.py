"""2024학년도 수능 (평가원) 2~3점 문항 해설 (ShrekMath 작성)"""
E = {
'2024-11-c1': '<b>핵심</b> 같은 지수끼리 묶기<br>$24^{\\frac13}\\times9^{\\frac13}=216^{\\frac13}=6$',
'2024-11-c2': '<b>핵심</b> 미분계수의 정의 $=f\'(2)$<br>$f\'(x)=6x^2-10x$, $f\'(2)=4$',
'2024-11-c3': '<b>핵심</b> $\\sin(-\\theta)=-\\sin\\theta$<br>$\\sin\\theta=-\\dfrac13$, 제4사분면 → $\\cos\\theta=\\dfrac{2\\sqrt2}3$<br>$\\tan\\theta=-\\dfrac1{2\\sqrt2}=-\\dfrac{\\sqrt2}4$',
'2024-11-c4': '<b>핵심</b> 연속 ⟺ $x=2$에서 두 식의 값이 같다<br>$6-a=4+a$, $a=1$',
'2024-11-c5': '<b>핵심</b> 적분 후 $f(1)$로 적분상수<br>$f(x)=x^3-3x^2+C$, $f(1)=-2+C=6$, $C=8$<br>$f(2)=8-12+8=4$',
'2024-11-c6': '<b>핵심</b> $S_4-S_2=a_3+a_4$<br>$a_3=2a_4$ → 공비 $r=\\dfrac12$<br>$a_1=\\dfrac34\\times2^4=12$, $a_2=6$ → $18$',
'2024-11-c7': '<b>핵심</b> $f\'(x)=0$의 두 근<br>$x^2-4x-12=(x-6)(x+2)$<br>극대 $\\alpha=-2$, 극소 $\\beta=6$ → $8$',
'2024-11-c8': '<b>핵심</b> $(x-1)f(x)=3x(x^3-1)$ → $x-1$로 나눈다<br>'
    '$f(x)=3x(x^2+x+1)=3x^3+3x^2+3x$<br>대칭 구간에서 홀수 차수는 $0$: $2\\displaystyle\\int_0^23x^2dx=16$',
'2024-11-c9': '<b>핵심</b> 내분점 $=m\\times(\\text{Q})+(1-m)\\times(\\text{P})$<br>'
    '$m\\log_512+(1-m)\\log_53=1$ → $m\\log_54=\\log_5\\dfrac53$<br>$\\log_54^m=\\log_5\\dfrac53$ → $4^m=\\dfrac53$',
'2024-11-c10': '<b>핵심</b> 두 점의 위치의 차를 식으로<br>'
    '$\\displaystyle\\int_0^t(v_1-v_2)ds=\\frac{t^3}3-4t^2+12t=\\frac{t(t-6)^2}3\\ge0$ → $f(t)$<br>'
    '$f\'(t)=(t-6)(t-2)$ → $a=2$, $b=6$<br>'
    'Q의 거리 $\\displaystyle\\int_2^6|2t-7|dt=\\left(\\frac32\\right)^2+\\left(\\frac52\\right)^2=\\frac{17}2$',
'2024-11-c16': '<b>핵심</b> 밑을 $3$으로 통일<br>$x-8=-3x$, $x=2$',
'2024-11-c17': '<b>핵심</b> 곱의 미분법<br>$f\'(x)=(x^2+3)+(x+1)\\times2x$<br>$f\'(1)=4+4=8$',
'2024-11-c18': '<b>핵심</b> $\\displaystyle\\sum a_k=A$, $\\sum b_k=B$로 연립<br>$A=2B-10$, $3A+B=33$<br>$7B-30=33$, $B=9$',
'2024-11-c19': '<b>핵심</b> $\\sin\\left(\\dfrac\\pi2\\pm\\theta\\right)=\\cos\\theta$<br>'
    '$f(2+x)f(2-x)=\\cos^2\\dfrac{\\pi x}4<\\dfrac14$ ⟺ $\\left|\\cos\\dfrac{\\pi x}4\\right|<\\dfrac12$<br>'
    '자연수 $x$ → $\\dfrac{\\pi x}{4}=\\dfrac\\pi2+k\\pi$ 꼴만 가능: $x=2,6,10,14$<br>합 $32$',
'2024-11-k23': '<b>핵심</b> 같은 것이 있는 순열<br>$\\dfrac{5!}{2!\\,2!}=30$',
'2024-11-m23': '<b>핵심</b> $\\dfrac{\\ln(1+x)}x\\to1$<br>$\\dfrac{3x}{5x}=\\dfrac35$',
'2024-11-g23': '<b>핵심</b> 중점 $=\\left(\\dfrac{a+9}2,\\ 0,\\ \\dfrac{6+b}2\\right)$<br>$a=-1$, $b=8$ → $7$',
'2024-11-k24': '<b>핵심</b> 독립 ⟺ $\\mathrm P(A\\cap B)=\\mathrm P(A)\\mathrm P(B)$<br>$1-\\mathrm P(A)=2\\mathrm P(A)$ → $\\mathrm P(A)=\\dfrac13$<br>$\\mathrm P(B)=\\dfrac14\\div\\dfrac13=\\dfrac34$',
'2024-11-m24': '<b>핵심</b> $\\dfrac{dy}{dx}=\\dfrac{dy/dt}{dx/dt}$<br>'
    '$t=1$: $\\dfrac{dx}{dt}=\\dfrac{3t^2}{t^3+1}=\\dfrac32$, $\\dfrac{dy}{dt}=\\pi\\cos\\pi=-\\pi$<br>$-\\dfrac23\\pi$',
'2024-11-g24': '<b>핵심</b> 점을 대입해 $a^2$, 접선 기울기 $-\\dfrac{b^2x_1}{a^2y_1}$<br>'
    '$\\dfrac3{a^2}+\\dfrac46=1$ → $a^2=9$<br>$-\\dfrac{6\\sqrt3}{9\\times(-2)}=\\dfrac{\\sqrt3}3$',
'2024-11-k25': '<b>핵심</b> 양 끝 두 장만 보면 된다 (순서 있게 $6\\times5=30$가지)<br>'
    '합이 $10$ 초과: $5,6$뿐 → $2$가지<br>$1-\\dfrac2{30}=\\dfrac{14}{15}$',
'2024-11-m25': '<b>핵심</b> 역함수의 미분 $g\'(f(x))=\\dfrac1{f\'(x)}$<br>'
    '피적분함수 $=\\dfrac{f\'(x)}{f(x)}$ → $\\ln f(a)-\\ln f(1)=\\ln\\dfrac{a^2(a+1)}2$<br>'
    '$f(a)=8\\times\\dfrac{a^2(a+1)}2=4a^2(a+1)$<br>$f(2)=48$',
'2024-11-g25': '<b>핵심</b> 크기는 제곱해서 내적으로<br>'
    '$|2\\vec a-\\vec b|^2=44-4\\vec a\\cdot\\vec b+9=17$ → $\\vec a\\cdot\\vec b=9$<br>'
    '$|\\vec a-\\vec b|^2=11-18+9=2$ → $\\sqrt2$',
'2024-11-k26': '<b>핵심</b> $X\\sim\\mathrm B\\left(4,\\dfrac12\\right)$<br>'
    '$\\mathrm P(X=0)=\\dfrac1{16}$, $\\mathrm P(X=1)=\\dfrac4{16}$, $\\mathrm P(X\\ge2)=\\dfrac{11}{16}$<br>'
    '$\\mathrm E(Y)=0+\\dfrac4{16}+2\\times\\dfrac{11}{16}=\\dfrac{13}8$',
'2024-11-m26': '<b>핵심</b> 단면이 정사각형 → 넓이 $y^2=(1-2x)\\cos x$, 부분적분<br>'
    '$\\displaystyle\\int(1-2x)\\cos x\\,dx=(1-2x)\\sin x-2\\cos x$<br>'
    '$\\left[\\ \\right]_{\\frac34\\pi}^{\\frac54\\pi}=\\left(\\dfrac{\\sqrt2}2+\\dfrac{5\\sqrt2}4\\pi\\right)-\\left(\\dfrac{3\\sqrt2}2-\\dfrac{3\\sqrt2}4\\pi\\right)=2\\sqrt2\\pi-\\sqrt2$',
'2024-11-g26': '<b>핵심</b> $\\overline{\\mathrm{AB}}=\\overline{\\mathrm{A\'B\'}}$ → AB $\\parallel\\alpha$, 삼수선 정리로 PM $\\perp$ AB<br>'
    '두 평면이 이루는 각 $\\theta=\\angle\\mathrm{MPM\'}$<br>'
    '$\\triangle\\mathrm{A\'B\'P}=\\dfrac12\\times6\\times6=18$, $18\\cos\\theta=\\dfrac92$ → $\\cos\\theta=\\dfrac14$<br>'
    '$\\overline{\\mathrm{PM}}=\\dfrac{\\overline{\\mathrm{PM\'}}}{\\cos\\theta}=24$',
'2024-11-k27': '<b>핵심</b> 신뢰구간 $\\bar x\\pm1.96\\times\\dfrac{5}{7}=\\bar x\\pm1.4$<br>'
    '$a=\\bar x-1.4$, $\\dfrac65a=\\bar x+1.4$ → $\\dfrac a5=2.8$, $a=14$<br>$\\bar x=15.4$',
'2024-11-m27': '<b>핵심</b> 접점 $x=s$, 접선이 원점을 지남: $e^{-s}+e^t=-se^{-s}$, 기울기 $f(t)=-e^{-s}$<br>'
    '$f(a)=-e^{\\frac32}$ → $s=-\\dfrac32$, $e^a=\\dfrac12e^{\\frac32}$<br>'
    '$t$로 미분: $e^t=se^{-s}\\dfrac{ds}{dt}$, $f\'(t)=e^{-s}\\dfrac{ds}{dt}=\\dfrac{e^t}s$<br>'
    '$f\'(a)=\\dfrac{\\frac12e\\sqrt e}{-\\frac32}=-\\dfrac13e\\sqrt e$',
'2024-11-g27': '<b>핵심</b> F$(2,0)$, 준선 $x=-2$, A$(x_1,y_1)$ → B$(-2,y_1)$; 직선 BF를 B$+\\lambda$(F$-$B)로<br>'
    '$y_1^2(1-\\lambda)^2=8(4\\lambda-2)$의 두 근이 $c,\\ 2c$ (BC $=$ CD)<br>'
    '근과 계수: $3c=2+2k$, $2c^2=1+k$ ($k=\\dfrac{16}{y_1^2}$) → $k=\\dfrac18$, $y_1^2=128$, $x_1=16$<br>'
    'D$(4,-\\frac{y_1}2)$, $\\overline{\\mathrm{AB}}=18$, 높이 $\\dfrac32|y_1|=12\\sqrt2$<br>넓이 $108\\sqrt2$',
}
A = {'2024-11-c1': 1, '2024-11-c2': 4, '2024-11-c3': 2, '2024-11-c4': 1, '2024-11-c5': 4, '2024-11-c6': 4, '2024-11-c7': 5, '2024-11-c8': 2,
     '2024-11-c9': 4, '2024-11-c10': 2, '2024-11-c16': 2, '2024-11-c17': 8, '2024-11-c18': 9, '2024-11-c19': 32,
     '2024-11-k23': 3, '2024-11-m23': 3, '2024-11-g23': 4, '2024-11-k24': 4, '2024-11-m24': 2, '2024-11-g24': 3,
     '2024-11-k25': 5, '2024-11-m25': 4, '2024-11-g25': 2, '2024-11-k26': 2, '2024-11-m26': 3, '2024-11-g26': 5,
     '2024-11-k27': 2, '2024-11-m27': 1, '2024-11-g27': 3}
