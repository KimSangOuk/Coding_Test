# 풀이시간 10분 시간제한 1초 메모리제한 128MB
# 1회차 정답
# 플로이드 워셜 알고리즘으로 그래프 형태로 2차원 배열의 값으로 답을 낸 다음, 한 지점으로 들어오는게 가능한 개수와 갈 수 있는 개수의 합이 나머지 지점의 개수의 합과 같을 경우 비교가 완전히 가능하다는 것을 알 수 있는 문제이다.

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