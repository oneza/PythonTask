#На отрезке [0,1] решить задачу Коши явным методом Эйлера,
#методом Тейлора второго порядка и трёхшаговым явным методом Адамса

import math
from pylab import *
x_0=0
y_0=0.5
N=10
d=1
h=d/N
x=[0]*(N+1)
y1=[0]*(N+1)
y2=[0]*(N+1)
y2[0]=y_0
y3=[0]*(N+1)
y3[0]=y_0
y4=[0]*(N+1)
y4[0]=y_0
def f(x_n):
    return 1/(10*(x_n)**2-8*(x_n)+2)
def Euler(x_n, y_n):
    return y_n-20*h*(y_n**2)*(x_n-0.4)
def Taylor(x_n, y_n):
    return y_n-(y_n**2)*(20*h*x_n-8*h+10*h**2)+(y_n**3)*16*(h**2)*(2-5*x_n)**2
def Adams(x_n,y_n,x_n1,y_n1,x_n2,y_n2):
    return y_n+h*(23*(-20*(y_n**2)*(x_n-0.4))-
                 -16*(-20*(y_n1**2)*(x_n1-0.4))+
                  +5*(-20*(y_n2**2)*(x_n2-0.4)))/12
def k1(x_n,y_n):
    return -h*20*(y_n**2)*(x_n-0.4)
def k2(x_n,y_n,k1):
     return -h*20*((y_n+k1/2)**2)*(x_n+(h/2)-0.4)
def k3(x_n,y_n,k2):
     return -h*20*((y_n+k2/2)**2)*(x_n+(h/2)-0.4)
def k4(x_n,y_n,k3):
     return -h*20*((y_n+k3)**2)*(x_n+h-0.4)
def RK(y_n,k1,k2,k3,k4):
    return y_n+(k1+2*k2+2*k3+k4)/6
for i in range(0,N+1):
    x[i]=i*h
for i in range(0,N+1):
    y1[i]=f(x[i])
for i in range(1,N+1):
    y2[i]=Euler(x[i-1],y2[i-1])
for i in range(1,N+1):
    y3[i]=Taylor(x[i-1],y3[i-1])
a1=k1(x[0],y4[0])
a2=k2(x[0],y4[0],a1)
a3=k3(x[0],y4[0],a2)
a4=k4(x[0],y4[0],a3)
y4[1]=RK(y4[0],a1,a2,a3,a4)
b1=k1(x[1],y4[1])
b2=k2(x[1],y4[1],b1)
b3=k3(x[1],y4[1],b2)
b4=k4(x[1],y4[1],b3)
y4[2]=RK(y4[1],b1,b2,b3,b4)
for i in range(3,N+1):
    y4[i]=Adams(x[i-1],y4[i-1],x[i-2],y4[i-2],x[i-3],y4[i-3])
plot (x,y1)
plot (x,y2)
plot (x,y3)
plot (x,y4)
xlabel('x')
ylabel('y')
title('N=10')
legend(('Correct Solution','Euler','Taylor','Adams'))
savefig("nummeth5_10.png",dpi=(640/8))