# 풀이시간 30분 시간제한 1초 메모리제한 128MB
# 1회차 정답
# 각 노드로 들어오는 숫자의 크기에 따라 현재 노드의 결과 값이 달라지기 때문에, 한 노드의 모든 들어오는 값의 처리가 끝난 후, 현재 노드의 결과를 처리하는 편이 쉽다. 그렇기 때문에 화살표의 순서대로 정렬하는 위상정렬을 생각해 볼 수 있다. 노드의 크기는 1,000이기 때문에 시간복잡도도 가능하다. 이 때, 노드에 대해 들어갈 경우에 각 노드에 들어오는 노드들을 저장해놓고 한 노드에 대한 모든 유입이 끝났을 때, 이 값을 계산하면 된다.

from collections import deque

def topology_sort():
  q=deque()

  for i in range(1,m+1):
    if indegree[i]==0:
      q.append(i)
      result[i]=1

  while q:
    now=q.popleft()
    for i in graph[now]:
      put_node[i].append(now)
      indegree[i]-=1
      if indegree[i]==0:
        q.append(i)
        max_value=0
        count=0
        for j in put_node[i]:
          if max_value<result[j]:
            max_value=result[j]
            count=1
          elif max_value==result[j]:
            count+=1
        if count==1:
          result[i]=max_value
        elif count>1:
          result[i]=max_value+1
          
for tc in range(int(input())):
  k,m,p=map(int,input().split())
  graph=[[] for _ in range(m+1)]
  indegree=[0]*(m+1)
  for _ in range(p):
    a,b=map(int,input().split())
    graph[a].append(b)
    indegree[b]+=1

  result=[0]*(m+1)
  put_node=[[] for _ in range(m+1)]

  topology_sort()
  print(k,max(result))