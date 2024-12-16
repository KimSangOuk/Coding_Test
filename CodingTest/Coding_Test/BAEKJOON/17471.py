import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

numOfPeople = dict()
total = 0
arr = list(map(int, input().split()))
for i in range(N):
    numOfPeople[i] = arr[i]
    total += arr[i]

graph = [[] for _ in range(N)]

for i in range(N):
    arr = list(map(int, input().split()))
    num = arr[0]
    for k in arr[1:]:
        graph[i].append(k - 1)

def checkedConnect(visited):
    if visited == 0:
        return False
    q = deque()
    start = -1
    for i in range(N):
        if visited & (1 << i):
            start = i
            break
    q.append(start)
    connected = 0
    connected |= (1 << start)
    while q:
        now = q.popleft()
        for k in graph[now]:
            if not (visited & (1 << k)):
                continue
            if connected & (1 << k):
                continue
            q.append(k)
            connected |= (1 << k)
    return connected == visited

def dfs(visited, sum, candidates):
    global answer
    if visited != 0:
        if checkedConnect(visited):
            unVisited = ((1 << N) - 1) ^ visited
            if unVisited != 0 and checkedConnect(unVisited):
                answer = min(answer, abs(total - 2 * sum))
    for i in range(candidates, N):
        if not (visited & (1 << i)):
            dfs(visited | (1 << i), sum + numOfPeople[i], i + 1)

answer = int(1e9)
dfs(0, 0, 0)

if answer == 1e9:
    print(-1)
else:
    print(answer)
