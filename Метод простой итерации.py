#Задание утеряно
#Метод простой итерации

import math 
now=0.5 
previous=1 
epsilon=0.5*10**(-5) 
n=0 
x0=math.pi/2 
def f(xn): 
    return math.sqrt((0.1+math.sin(xn))/2) 
fx0=f(x0) 
while abs(now-previous)>epsilon: 
    previous=now 
    now=f(now) 
    n+=1 
print (now) 
print (n) 