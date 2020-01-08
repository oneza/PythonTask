#Определить, является ли данный связный  неориентированный  граф  двудольным. Метод решения: Поиск в ширину.

with open(r'in.txt','r') as file:
    graf = [row.strip() for row in file]
result = open('out.txt', 'w')
result.write("0"+"\n")
# label[v] = 0 - вершина v не посещена
# label[v] = 1 - вершина v посещена
length = int(graf[0]) # количество вершин
label = [0]*(length+1) #инициализация 
k = 0 # кол-во компонент связности
def bfs(s):
    queue=[]
    queue = [s] # добавляем начальную вершину в очередь
    label[s] = 1 # вершина s посещена
    while queue: # пока там что-то есть
        u = queue.pop(0) # извлекаем вершину из очереди, этот элемент из очереди удаляется
        need.append(u)
        for w in graf[u][:-2].split(" "): # запускаем обход из вершины v
            w = int(w)
            if label[w] == 0: # проверка на посещенность
                queue.append(w) # добавление вершины в очередь
                label[w] = 1 # вершина посещена
for v in range(1,length+1):
    if len(graf[v][:].split(" "))==1:
            k+=1
            result.write(str(v)+" 0"+"\n")
    else:
        if label[v] == 0: 
            need=[] # задаем массив, в который будем класть вершины из одной компоненты связности
            bfs(v)
            k+=1
            need.sort()
            need.append(0)
            res=" ".join(map(str,need))
            result.write(res+"\n")
k=str(k)
result.seek(0) # возвращаемся в начало файла
result.write(k+"\n") # записываем количество компонент связности
file.close() 
result.close()
