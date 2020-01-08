#Задание утеряно
#Метод хорд

import math 
now=0.5 
previous=1 
x0=math.pi/2 
epsilon=0.5*10**(-5) 
n=0 
def f(xn): 
    return math.sin(xn)+0.1-2*xn**2 
fx0=f(x0) 
while abs(now-previous)>epsilon: 
    previous=now 
    now=now-f(now)*(now-x0)/(f(now)-fx0) 
    n+=1 
print (now) 
print (n) 