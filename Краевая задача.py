#Для уравнения y^{\prime\prime}=y+2\alpha+2+\alpha x(1-x), \alpha=2+0.1\cdot N, где N=9 на отрезке [0,1] 
#Решить краевую задачу методом стрельбы и методом прогонки со следующими краевыми условиями: 
#y(0)=0; y^\prime(1)+y(1)=2e+\alpha-2. 
#Для решения задачи Коши в методе стрельбы использовать метод третьего порядка, основанный на разложении в ряд Тейлора,
#для решения нелинейного уравнения в методе стрельбы использовать метод хорд,
#аппроксимацию краевых условий в методе прогнки проводить по двум узлам.

import math
from sympy import *
import numpy as np
from pylab import *
x_0=0
y_0=0
N=50
h=1/N
alpha=2+0.1*9
gam=symbols('gam')
gam_0=0
gam0=gam_0
gam_1=1
gam_2=0
mu=[0]*(N+1)
lamb=[0]*(N+1)
x=[0]*(N+1)
y1=[0]*(N+1)
y2=[0]*(N+1)
y2[0]=y_0
y3=[0]*(N+1)
y3[0]=y_0
z3=[0]*(N+1)
z3[0]=gam
def f(x_i):
    return math.exp(x_i)+math.exp(-x_i)+alpha*(x_i)**2-alpha*(x_i)-2
def yn(y_i,z_i):
    return y_i+h*z_i
def zn(x_i,y_i,z_i):
    return z_i+(x_i**2)*alpha*h*(-1-h/2-h**2/3)+x_i*alpha*h*(1-h/2-h**2/6)+
           +y_i*h*(1+h/2+h**2/6)+h*(2*alpha+2+3*h*alpha/2+h+alpha*(h**2)/6+h**2/3)
for i in range(0,N+1):
    x[i]=i*h
    y1[i]=f(x[i])
for i in range(1,N+1):
    y3[i]=yn(y3[i-1],z3[i-1])
    z3[i]=zn(x[i-1],y3[i-1],z3[i-1])
g=y3[N]+z3[N]-2*math.exp(1)-alpha+2
while abs(g.subs(gam,gam_0))>10**(-6):
    gam_2=gam_1-g.subs(gam,gam_1)*(gam_1-gam0)/(g.subs(gam,gam_1)-g.subs(gam,gam0))
    gam_0=gam_1
    gam_1=gam_2
z3[0]=gam_0
for i in range(1,N+1):
    y3[i]=yn(y3[i-1],z3[i-1])
    z3[i]=zn(x[i-1],y3[i-1],z3[i-1])
for i in range(2,N+1):
    mu[i]=((h**2)*(2*alpha+2+alpha*x[i-1]*(1-x[i-1]))-mu[i-1])/(lamb[i-1]-2-h**2)
    lamb[i]=-1/(lamb[i-1]-2-h**2)
y2[N]=(h*(2*(math.exp(1)) + alpha -2)+mu[N])/(-lamb[N]+1+h)
i=N-1
while i>0:
    y2[i]=lamb[i+1]*y2[i+1]+mu[i+1]
    i-=1
plot (x,y1)
plot (x,y2)
plot (x,y3)
xlabel('x')
ylabel('y')
title('N=50')
legend(('Correct Solution','Tridiagonal matrix algorithm','Shooting method'))
savefig("numeth6_50.png",dpi=(640/8))