#Вычислить значение интеграла $\int\limits_1^2 e^{{-x}^3} dx$ 
#по составной формуле средних прямоугольников и формуле  «3/8» с шагом 0,1; 0,05; 0,025. 

import math
a=1
b=2
h=0.1
i=0
int1=0
int2=0
n1=(b-a)/h
n2=((b-a)*2)/h
def f(xi, h):
    return math.exp(-((2*xi+h)/2)**3)
while i<=n1:
    int1=int1+f(a,h)
    a=a+h
    i+=1
int1=h*int1
a=1
i=0
h=h/2
while i<=n2:
    int2=int2+f(a,h)
    a=a+h
    i+=1
int2=h*int2
R=4*(int2-int1)/3
print (int1)
print (R)
print (n1)