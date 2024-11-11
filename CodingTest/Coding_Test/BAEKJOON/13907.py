import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

N, M, K = map(int, input().split())
S, D = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
tax = [0]
for _ in range(K):
    tax.append(int(input())+tax[-1])

def dijkstra(start):
    distance = [[INF] * N for _ in range(N + 1)]
    q = [(0, 0, start)]
    distance[start][0] = 0
    while q:
        dist, edgeCnt, now = heapq.heappop(q)
        flag = False
        for i in range(edgeCnt):
            if distance[now][i] < dist:
                flag = True
                break
        if edgeCnt == N - 1 or flag:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if distance[i[0]][edgeCnt + 1] > cost:
                distance[i[0]][edgeCnt + 1] = cost
                heapq.heappush(q, (cost, edgeCnt + 1, i[0]))
    return distance

distance = dijkstra(S)[D]
answer=[]

for k in tax:
    min_cost=INF
    for i in range(len(distance)):
        if distance[i]<INF:
            min_cost=min(min_cost,distance[i]+i*k)
    answer.append(min_cost)

print(*answer, sep='\n')
