# 풀이시간 5분 시간제한 1초 메모리제한 256MB
# 1회차 정답
# m회차에 걸쳐서 푸는 알고리즘이기 최대 100회라 걱정할게 없었다. 그저 상황을 순서대로 구현해 나가는 시뮬레이션 유형이다.
n,m=map(int,input().split())
arr=[0]
for k in range(1,n+1):
  arr.append(k)
for _ in range(m):
  i,j=map(int,input().split())
  arr[i],arr[j]=arr[j],arr[i]

for k in range(1,n+1):
  print(arr[k],end=' ')