# 풀이시간 20분 시간제한 1초 메모리제한 512MB
# 1회차 정답
# 각 주어진 이름들이 그래프를 이루고 그 그래프의 위상 관계에 따라 출력들을 정리해서 출력하는 문제이다. 그렇기에 위상정렬을 사용하였고 시간복잡도 O(N+M)또한 가능하다.
# 가문의 첫 조상의 이름과 수는 맨 처음 유입이 0인 것들을 찾을때 저장하면 된다. 나머지는 각 이름의 순으로 자식을 찾는 것이기 때문에 유입이 새롭게 0이 되는 것이 있을 때마다 처리하면 된다.

from collections import deque

def topology_sort():
  q=deque([])

  for i in range(n):
    if indegree[i]==0:
      q.append(i)
      droughty.append(i)

  while q:
    now=q.popleft()
    for i in graph[now]:
      indegree[i]-=1
      if indegree[i]==0:
        q.append(i)
        children[now].append(i)

n=int(input())
people=list(map(str,input().split()))
people.sort()
graph=[[] for _ in range(n)]
indegree=[0]*n

m=int(input())
for _ in range(m):
  s1,s2=map(str,input().split())
  graph[people.index(s2)].append(people.index(s1))
  indegree[people.index(s1)]+=1

droughty=[]
children=[[] for _ in range(n)]

topology_sort()
print(len(droughty))
for i in droughty:
  print(people[i],end=' ')
print()
for i in range(n):
  print(people[i],len(children[i]),end=' ')
  for j in sorted(children[i]):
    print(people[j],end=' ')
  print()
  
  