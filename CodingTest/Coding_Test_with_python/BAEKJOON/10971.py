# 풀이시간 20분 시간제한 2초 메모리제한 256MB
# 1회차 정답
# 모든 도시를 들렸다가 다시 돌아오는 최단경로를 구하는 문제이기 때문에 최단경로 알고리즘이나 DFS/BFS를 풀어보려고 했으나 다시 돌아오는 경로를 확인할 수가 없었기 때문에 모든 도시를 들려보는 경우의 수를 계산해보았다. 약 360만이므로 각 도시를 다시 순회하면 *10이되어 약 3600만으로 2초 내로 풀어질 수 있었다. 각 케이스를 순열로 구해서 마지막에 다시 처음 도시로 돌아오게 해주고 그 경로의 합의 최솟값을 구해주면 된다.

from itertools import permutations

n=int(input())

graph=[]
for i in range(1,n+1):
    graph.append(list(map(int,input().split())))

result=int(1e9)
for case in list(permutations(range(0,n),n)):
    case=list(case)
    case+=[case[0]]
    cost=0
    value=True
    for i in range(n):
        if graph[case[i]][case[i+1]]==0:
            value=False
        else:
            cost+=graph[case[i]][case[i+1]]
    if not value:
        continue
    result=min(result,cost)

print(result)