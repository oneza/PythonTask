#Найти наибольшее паpосочетание в двудольном гpафе. 
#Метод решения: сведение к задаче о максимальном потоке и использование алгоpитма Фоpда-Фалкеpсона.

import random
import sys
with open(r'in5.txt','r') as file:
    graf = [row.strip() for row in file]
result = open('out5.txt', 'w')
k=int(graf[0][0])
l=int(graf[0][2])
if k!=l:
    result.write("N")
    exit()
A=[]
for w in graf[2][:].split(" "):
    A.append(int(w))
X=[0]*k
for i in range(1,k+1): 
    X[i-1]=i
Y=[0]*l
for i in range(1,l+1): 
    Y[i-1]=i
xpair=[0]*l
ypair=[0]*k
T=X
for x in X:
    xpair[x-1]=None
for y in Y:
    ypair[y-1]=None
stack=[]
stack_dfs=[[0] * l for i in range(k)]
def search_(x):
    adr=A[x-1]
    dist=A[x]-A[x-1]
    for i in range(0,dist):
        y=A[adr-1+i]
        if xpair[x-1]!=y and stack_dfs[x-1][y-1]==0:
            stack_dfs[x-1][y-1]=1
            return y
    return None
while True:
    x_0=random.choice(T)
    stack.insert(0,x_0)
    tag=0
    while stack!=[] and tag==0:
        x=stack[0]
        y=search_(x)
        if y!=None:
            stack.insert(0,y)
            z=ypair[y-1]
            if z!=None:
                stack.insert(0,z)
            else: tag=1
        else:
            stack.pop(0)
            if stack!=[]:
                stack.pop(0)
    if tag==1:
        while stack!=[]:
            y=stack.pop(0)
            x=stack.pop(0)
            xpair[x-1]=y
            ypair[y-1]=x
            if T.count(x)!=0:
                T.remove(x)
    if tag==0 or T==[]:
        break
if tag==0:
    result.write("N"+"\n"+str(x_0))
else:
    result.write("Y"+"\n")
    res=" ".join(map(str,xpair))
    result.write(res)