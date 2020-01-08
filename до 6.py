#Найти  кратчайший v-w путь в сети с произвольными весами. 
#Метод решения: алгоритм Форда-Беллмана.

with open(r'in5.txt','r') as file:
    graf = [row.strip() for row in file]
result = open('out5.txt', 'w')
length = int(graf[0])
s=int(graf[length+1])
t=int(graf[length+2])
mST=0
V=[0]*length
for i in range(1,length+1): 
    V[i-1]=i
A=[]
for v in V:
    d=[]
    for w in graf[v][:].split(" "):
        d.append(int(w))
    A.append(d)
D=[23767]*(length)
D[s-1]=0
V.remove(s)
for v in V:   
    i=0
    while i<len(A[s-1]):
        if A[s-1][i]==v:
            D[v-1]=A[s-1][i+1]
        i+=2
for k in range(2,length-1):
    for v in V:
        for w in range(1,length+1):
            i=0
            while i<len(A[w-1]):
                if A[w-1][i]==v:
                    D[v-1]=min(D[v-1],D[w-1]+A[w-1][i+1])
                i+=2
stack=[]
stack.append(t)
v=t
while (v!=s):
    for w in range(1,length+1):
        i=0
        while i<len(A[w-1]):
            if A[w-1][i]==v:
                if D[v-1]==D[w-1]+A[w-1][i+1]:
                    mST+=A[w-1][i+1]
                    v=w
                    stack.insert(0,v)
            i+=2
    if len(stack)==1:
        result.write("N"+"\n")
        exit()
result.write("Y"+"\n")
result.write(" ".join(map(str,stack))+"\n")
result.write(str(mST))
