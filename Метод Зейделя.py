#Задание утеряно
#Метод Зейделя

import math 
x01=23/17 
x02=241/68 
x03=144/85 
x1=0 
x2=0 
x3=0 
epsilon=0.5*10**(-4) 
n=0 
def f1(x1,x2,x3): 
    return 23/17-2*x3/17 
def f2(x1,x2,x3): 
    return 27/8+x1/8-x3/2 
def f3(x1,x2,x3): 
    return 24/5-x1/5-4*x2/5 
while math.sqrt((1.7*x01+0.2*x03-2.3)**2+ 
                (-0.1*x01+0.8*x02+0.4*x03-2.7)**2+ 
                (-0.1*x01-0.4*x02-0.5*x03+2.4)**2)>epsilon: 
    x1=f1(x01,x02,x03) 
    x2=f2(x1,x02,x03) 
    x3=f3(x1,x2,x03) 
    x01=x1 
    x02=x2 
    x03=x3 
    n+=1 
print (x01, x02, x03) 
print (n) 