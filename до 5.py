#Найти v-w путь в сети с неотрицательными весами,  решающий MAXMIN задачу о кратчайшем пути. 
#Метод решения: модификация алгоритма Дейкстры.

with open(r'in2.txt','r') as file:
    graf = [row.strip() for row in file]
result = open('out2.txt', 'w')
length = int(graf[0])
s=int(graf[length+1])
t=int(graf[length+2])
V=[0]*length
father=[0]*length
for i in range(1,length+1):
    V[i-1]=i
A=[]
for v in V:
    d=[]
    for w in graf[v][:].split(" "):
        d.append(int(w))
    A.append(d)
D=[23767]*length
D[t-1]=23768
D[s-1]=-23767
S=[s]
V.remove(s)
for v in V:
    i=0
    while i<len(A[s-1]):
        if A[s-1][i]==v:
            D[v-1]=A[s-1][i+1]
        i+=2
        father[v-1]=s
while (S.count(t)==0):
    Dv=[]
    for v in V:
        Dv.append(D[v-1])
    for v in V:
        if D[v-1]==min(Dv):
           w=v
    V.remove(w)
    S.append(w)
    for v in V:
        i=0
        while i<len(A[w-1]):
            if A[w-1][i]==v:
                if D[v-1]>max(D[w-1],A[w-1][i+1]):
                    D[v-1]=max(D[w-1],A[w-1][i+1])
                    father[v-1]=w
            i+=2
if D[t-1]==-23767 or D[t-1]==23768:
    result.write("N"+"\n")
    exit()
else:
    stack=[]
    stack.insert(0,t)
    v=t
    while (v!=s):
        w=father[v-1]
        stack.insert(0,w)
        v=w
result.write("Y"+"\n")
result.write(" ".join(map(str,stack))+"\n")
result.write(str(D[t-1]))