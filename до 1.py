#В заданном лабиринте найти путь между двумя данными узлами. Метод решения: Поиск в глубину.

A = []
f = open(r'in.txt','r') 
for line in f: 
    row = [int(i) for i in line.split()] 
    A.append(row) 
length = A[0][0] 
result = open('out.txt', 'w')
result.write("0"+"\n")
# label[v] = 0 - v - не посещена	
# label[v] = 1 - v - посещена 
label = [0]*(length+1) #инициализация
k = 0 # количество компонент связности
def bfs(s): #описание поиска в ширину
    queue=[]
    queue = [s] # начальная вершина в очередь
    label[s] = 1 # отмечаем ее как посещенную
    while queue: # пока очередь не пуста 
        u = queue.pop(0) # извлекаем элемент из очереди
        need.append(u) # и добавляем в массив 
        i=0
        for w in A[u]: # продолжаем пороверку w
            i+=1
            if w!=0: 
                if label[i] == 0:  
                    queue.append(i) 
                    label[i] = 1 
for v in range(1,length+1):
    if label[v] == 0:
        need=[] # массив с вершинами одной компоненты связности
        bfs(v)
        k+=1
        need.sort()
        need.append(0)
        res=" ".join(map(str,need))
        result.write(res+"\n")
k=str(k)
result.seek(0) 
result.write(k+"\n") 
f.close() 
result.close()