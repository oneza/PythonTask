#Построить минимальный остов связного неориентированного взвешенного графа. 
#Метод решения: алгоритм Борувки-Краскла. 
#Файл входных данных: Граф, заданный массивом смежности.

import random 
A = []
f = open(r'in3.txt','r') 
for line in f: 
    row = [int(i) for i in line.split()] 
    A.append(row) 
length = A[0][0]
result = open('out3.txt', 'w')
T=[]
mT=0
F=[0]*(length)
for i in range(1,length+1): 
    F[i-1]=i
near=[0]*(length+1)
d=[0]*(length+1)
w=random.choice(F)
F.remove(w)
for v in F:
    near[v]=w
    d[v]=A[v][w-1]
while (len(T)<length-1):
    min_=32767
    min_F=32767
    for v in F:
        if d[v]<min_:
            min_=d[v]
            min_F=v
    v=min_F
    mT=mT+min_
    T.append(([v, near[v]]))
    F.remove(v)
    for u in F:
        if d[u]>A[u][v-1]:
            near[u]=v
            d[u]=A[u][v-1]
for a in range(1,length+1):
    R=[]
    for i in range(0, len(T)):
        if a==T[i][0]:
            R.append(T[i][1]) 
        if a==T[i][1]:
            R.append(T[i][0])
    R.sort()
    R.append(0)
    res=" ".join(map(str,R))
    result.write(res+"\n")
result.write(str(mT))
