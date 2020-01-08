#Построить минимальный остов связного неориентированного взвешенного графа.
#Метод решения: алгоритм Ярника-Прима-Дейкстры.

with open(r'in1.txt','r') as file:
    graf = [row.strip() for row in file]
result = open('out1.txt', 'w')
length = int(graf[0])
A=[]
dist=0
for v in range(1,length+1):
    d=[]
    for w in graf[v][:].split(" "):
        d.append(int(w))
    A.append(d)
name_=[0]*length
trace_=[0]*length
size_=[0]*length
def sort_(array): # сортировка выбором (сложность о(n^2)
    for i in range(len(array)):
        indxMin = i
        for j in range(i+1, len(array)):
            if array[j][0] < array[indxMin][0]:
                indxMin = j
        tmp = array[indxMin]
        array[indxMin] = array[i]
        array[i] = tmp
    return array
for v in range(1,length+1):
    name_[v-1]=v
    trace_[v-1]=v
    size_[v-1]=1
T=[]
queue=[]
for i in range(0,length):
    j=0
    while j<len(A[i])-1:
        queue.append([A[i][j+1],i+1,A[i][j]])
        j+=2
sort_(queue)
for i in range(0, len(queue)):
    queue[i].pop(0)
    queue[i].sort()
b = []
for sublist in queue:
    if sublist not in b:
        b.append(sublist)
queue=b
while len(T)!=length-1: #основной цикл
    u=queue.pop(0)
    v=u[0]
    w=u[1]
    p=name_[v-1]
    q=name_[w-1]
    if p!=q:
        if size_[p-1]<size_[q-1]: #слияние деревьев v и w
            name_[v-1]=q
            u=trace_[v-1]
            while name_[u-1]!=q:
                name_[u-1]=q
                u=trace_[u-1]
            size_[q-1]=size_[q-1]+size_[p-1]
            v_=trace_[v-1]
            w_=trace_[w-1]
            trace_[v-1]=w_
            trace_[w-1]=v_
        else: #слияние деревьев w и v
            name_[w-1]=p
            u=trace_[w-1]
            while name_[u-1]!=p:
                name_[u-1]=p
                u=trace_[u-1]
            size_[p-1]=size_[p-1]+size_[q-1]
            v_=trace_[v-1]
            w_=trace_[w-1]
            trace_[v-1]=w_
            trace_[w-1]=v_
        T.append([v,w])
        i=0
        while i<=len(A[v-1]):
            if A[v-1][i]==w:
                dist+=A[v-1][i+1]
                break
            i+=2
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
result.write(str(dist))