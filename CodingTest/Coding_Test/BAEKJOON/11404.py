# 이것이 취업을 위한 코딩테스트다 part03 '37. 플로이드'와 동일

import sys

input=sys.stdin.readline

INF=int(1e9) # 무한을 의미하는 값으로 10억을 설정

# 노드의 개수 및 간선의 개수를 입력받기
n=int(input())
m=int(input())
# 2차원 리스트(그래프 표현)를 만들고, 모든 값을 무한으로 초기화
graph=[[INF]*(n+1) for _ in range(n+1)]

# 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
for i in range(1,n+1):
  for j in range(1,n+1):
    if i==j:
      graph[i][j]=0

# 각 간선에 대한 정보를 입력받아, 그 값으로 초기화
for _ in range(m):
  # A에서 B로 가는 비용은 C라고 설정
  a,b,c=map(int,input().split())
  # 가장 짧은 간선의 정보만 저장
  graph[a][b]=min(graph[a][b],c)

# 점화식에 따라 플로이드 워셜 알고리즘을 수행
for k in range(1,n+1):
  for i in range(1,n+1):
    for j in range(1,n+1):
      graph[i][j]=min(graph[i][j],graph[i][k]+graph[k][j])

# 수행된 결과를 출력
for i in range(1,n+1):
  for j in range(1,n+1):
    # 도달할 수 없는 경우, 0을 출력
    if graph[i][j]==INF:
      print(0,end=' ')
    # 도달할 수 있는 경우 거리를 출력
    else:
      print(graph[i][j],end=' ')
  print()