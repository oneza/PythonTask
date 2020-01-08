#Задание утеряно
#Метод подвижных хорд

import math 
now=0.5 
previous=math.pi/2 
next=1 
epsilon=0.5*10**(-5) 
n=0 
def f(xn): 
    return math.sin(xn)+0.1-2*xn**2 
while abs(now-previous)>epsilon: 
    next=now-f(now)*(now-previous)/(f(now)-f(previous)) 
    previous=now 
    now=next 
    n+=1 
print (now) 
print (n) 