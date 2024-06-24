# 풀이시간 25분/40분 시간제한 5초 메모리제한 128MB
# 1회차 정답
# 문제의 비교 형태를 그려봤을 때, 그래프 모양이 나온다는 점에서 그래프 관련 문제로 추측할 수 있다. 이러한 점에서, 각 비교가 가능한 경우 유효한 값이 나오고, 불가능한 경우 INF값이 나오는 플로이드 워셜 알고리즘으로 풀 수 있다는 것을 알 수 있다. 즉, 각 지점으로 이어지는 값이 존재하고 각 점에서 출발하는 값이 모두 존재할 때, 그 수의 순위를 알 수 있다는 결론이 나온다. 시간복잡도 측면에서도 5초이기 때문에 O(N^3)을 했을 때, 가능하다.
# 답안지와 풀이가 같기 때문에 주석을 달면서 복습했다.

import sys

input=sys.stdin.readline

INF=int(1e9) # 무한을 의미하는 값으로 10억을 설정

# 노드의 개수, 간선의 개수를 입력받기
n,m=map(int,input().split())
# 2차원 리스트(그래프 표현)를 만들고, 모든 값을 무한으로 초기화
graph=[[INF]*(n+1) for _ in range(n+1)]

# 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
for i in range(1,n+1):
  for j in range(1,n+1):
    if i==j:
      graph[i][j]=0

# 각 간선에 대한 정보를 입력받아, 그 값으로 초기화
for _ in range(m):
  # A에서 B로 가는 비용을 1로 설정
  a,b=map(int,input().split())
  graph[a][b]=1

# 점화식에 따라 플로이드 워셜 알고리즘을 수행
for k in range(1,n+1):
  for i in range(1,n+1):
    for j in range(1,n+1):
      graph[i][j]=min(graph[i][j],graph[i][k]+graph[k][j])

answer=0
# 각 학생을 번호에 따라 한 명씩 확인하며 도달 가능한지 체크
for i in range(1,n+1):
  count=0
  for j in range(1,n+1):
    if i!=j and min(graph[i][j],graph[j][i])<INF:
      count+=1
  if count==n-1:
    answer+=1

print(answer)