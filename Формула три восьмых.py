#Вычислить значение интеграла $\int\limits_1^2 e^{{-x}^3} dx$ 
#по составной формуле средних прямоугольников и формуле  «3/8» с шагом 0,1; 0,05; 0,025. 

import math
a=1
b=2
x0=a
h=0.1
i=0
int1=0
int2=0
n1=(b-a)/h
n2=((b-a)*2)/h
s0=0
s1=0
s2=0
def f0(xi):
    return math.exp(-(xi)**3)
def f1(xi,h):
    return math.exp(-(xi+h/3)**3)
def f2(xi, h):
    return math.exp(-(xi+2*h/3)**3)
while i<n1:
    s0=s0+f0(x0)
    s1=s1+f1(x0,h)
    s2=s2+f2(x0,h)
    x0=x0+h
    i+=1
int1=h*(f0(b)-f0(a)+2*s0+3*s1+3*s2)/8
x0=a
i=0
s0=0
s1=0
s2=0
h=h/2
while i<n2:
    s0=s0+f0(x0)
    s1=s1+f1(x0,h)
    s2=s2+f2(x0,h)
    x0=x0+h
    i+=1
int2=h*(-f0(b)-f0(a)+2*s0+3*s1+3*s2)/8
R=16*(int2-int1)/15
print (int1)
print (R)
print (n1)