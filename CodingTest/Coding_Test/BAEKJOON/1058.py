# 풀이시간 30분 시간제한 2초 메모리제한 128MB
# 1회차 정답
# 플로이드 워셜의 결과물을 사실상 표로 준것과 다름이 없다. 각 친구사이의 관계를 주고 두 관계를 보았을 때, 두 친구가 친구이거나, 중간에 친구 한명이상으로 연결되어 있으면 친구를 세는 식으로 역으로 플로이드 워셜의 결과를 분석하는 식으로 풀어내면 된다. 친구는 50명 이하이기 때문에 플로이드 워셜인 3중 for문이 가능하다.

n=int(input())

INF=int(1e9)
graph=[[INF]*(n+1) for _ in range(n+1)]

for i in range(1,n+1):
  arr=[0]+list(input())
  for j in range(1,n+1):
    if i==j and arr[j]=='N':
      graph[i][j]=0
    elif i!=j:
      if arr[j]=='Y':
        graph[i][j]=1
      else:
        graph[i][j]=INF

answer=[0]*(n+1)
for i in range(1,n+1):
  count=0
  for j in range(1,n+1):
    isTrue=False
    if graph[i][j]==1:
      isTrue=True
    else:
      for k in range(1,n+1):
        if i!=j and i!=k and j!=k:
          if graph[i][k]==1 and graph[k][j]==1:
            isTrue=True
            break
    if isTrue:
      count+=1
  answer[i]=count

print(max(answer[1:]))