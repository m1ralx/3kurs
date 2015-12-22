from math import sqrt as sqrt
from math import pow as pow
from math import fabs
graph = []
INF = 9999999999
with open('in.txt', 'r') as file:
    lines = file.readlines()
    num = int(lines[0])
    for i in range(1, num+1):
        graph.append([])
        info = [int(x) for x in lines[i].split()]
        for j in range(0, len(info), 2):
            if info[j] == 0:
                break
            graph[i-1].append((info[j], info[j + 1]))


def out(save):
    with open("out.txt", 'w') as f:
        f.write(save)


matr = []
for i in graph:
    matr.append([])
    for j in graph:
        matr[graph.index(i)].append(fabs(j[0][0]-i[0][0])+fabs(j[0][1]-i[0][1]))

"""
def find_min(matr):
    min = []
    min = [INF for i in range(0, len(matr))]
    for i in range(0, len(matr)):
        for k in range(0, len(matr)):
            if matr[k][i] < min[i] and i != k:
                min[i] = matr[k][i]
    return min


def mst_prim(matr):
    min = find_min(matr)
    result = []
    visited = []
    for i in range(0, len(matr)):
        result.append([])
        for k in matr[i]:
            if i not in visited:
                result[i].append(matr[i].index(k))

        visited.append(matr[i].index(k))
    return result
"""

for i in matr:
    print(i)


def search_min(tr, vizited):
    index2 = 0
    min = INF
    for ind in vizited:
        for index, elem in enumerate(tr[ind]):
            if elem < min and index not in vizited:
                min = elem
                index2 = index
    return [min, index2]


def prim(matr):
    toVisit=[i for i in range(1, len(matr))]
    vizited=[0]
    result=[0]
    res = []
    for i in range(1, len(matr)):
        res.append([])
    for index in toVisit:
        weight, ind = search_min(matr, vizited)

        #res[ind].append(vizited.index(index))
        result.append(weight)
        vizited.append(ind)
    res[ind].append(ind)
    return vizited

res = prim(matr)
print(res)
