#Пусть {A1,...,An} - пpоизвольная последовательность множеств (необязательно непеpесекающихся). 
#Системой pазличных  пpедставителей  для   {A1,...,An}   называется последовательность  попаpно pазличных элементов {a1,...,an} такая,  что ai пpинадлежит Ai. 
#Найти систему pазличных пpедставителей для заданной последовательности множеств, если она существует

import queue
from math import ceil

class Edge:
    def __init__(self, v, to, capacity):
        self.v = v
        self.to = to
        self.capacity = capacity
        self.flow = 0
        self.back_edge = None

    def __repr__(self):
        return '{} -> {} = {}'.format(self.v, self.to, self.flow)

def read_input():
    with open(r'in1.txt','r') as file:
        graf = [row.strip() for row in file]
    k = int(graf[0][0])
    l = int(graf[0][2])
    A=[]
    X=[0]*k
    for i in range(1,k+1): 
        X[i-1]=i
    Y=[0]*l
    for i in range(1,l+1): 
        Y[i-1]=i
    for v in X:
        d=[]
        for w in graf[v][:].split(" "):
            d.append(int(w))
        A.append(d)
    graph = {}
    for i in range(k + l + 2):
        graph[i] = []
    for i in range(0,k):
        for j in range(0,l):
            if A[i][j] == 1:
                p = j + k
                graph[i + 1].append(p + 1)
                graph[p + 1].append(i + 1)
                graph[0].append(i + 1)
                graph[k + l + 1].append(p + 1)
    graph[0] = sorted(list(set(graph[0])))
    graph[k + l + 1] = sorted(list(set(graph[k + l + 1])))
    for i in range(l):
        graph[k + i + 1].append(k + l + 1)
    for i in range(k):
        graph[i + 1].append(0)
    return k, l, graph, 0, k + l + 1

def write_output(res):
    with open('out.txt', 'w') as file:
        for point in res:
            print(point, end=' ', file=file)

def get_graph(temp_graph):
    graph = {}
    for s in temp_graph.keys():
        for t in temp_graph[s]:
            if s not in graph:
                graph[s] = []
            if t not in graph:
                graph[t] = []
            add_edge(graph, s, t)
    return graph

def add_edge(graph, s, t):
    first = Edge(s, t, 1)
    second = Edge(t, s, 0)
    first.back_edge = second
    second.back_edge = first
    graph[s].append(first)
    graph[t].append(second)

def bfs(graph, start):
    q = queue.Queue()
    visited = [start]
    q.put(start)
    traceback = {}
    while not q.empty():
        cur = q.get()
        for e in graph[cur]:
            if e.to not in visited and e.flow < e.capacity:
                traceback[e.to] = e
                q.put(e.to)
                visited.append(e.to)
    return visited, traceback

def Ford_Fulkerson(graph, s, t):
    max_flow = 0
    while True:
        visited, traceback = bfs(graph, s)
        if t in visited:
            path = get_path(traceback, s, t)
            min_d = 100 * 1000
            for e in path:
                d = e.capacity - e.flow
                if d < min_d:
                    min_d = d
            max_flow += min_d
            for e in path:
                e.flow += min_d
                e.back_edge.flow -= min_d
                #e.flow += min_d
                #if e.back_edge.flow > 0:
                #    e.back_edge.flow = -1
                #    e.flow += min_d
                #else: 
                #    e.back_edge.flow -= min_d
                #    e.flow += min_d
        else:
            return max_flow

def get_path(path, start, end):
    res = []
    cur = end
    while cur != start:
        res.insert(0,path[cur])
        cur = path[cur].v
    return res

if __name__ == '__main__':
    k, l, temp_graph, s, t = read_input()
    graph = get_graph(temp_graph)
    flow = Ford_Fulkerson(graph, s, t)
    res = []
    for i in range(1, k + 1):
        edges = graph[i]
        good_edge = list(filter(lambda e: e.flow > 0, edges))
        if not good_edge:
            res.append(0)
        else:
            res.append(good_edge[0].to - k)

    write_output(res)