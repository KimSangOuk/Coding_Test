# 풀이시간 5분 시간제한 1초 메모리제한 256MB
# 1회차 정답
# 단순히 M 만큼 작업을 해야되는게 눈에 보이고 그 M당 작업의 범위는 M 범위와 같아서 대략 10,000회 정도의 작업이 최대이다. 그래서 시간복잡도는 괜찮고 그냥 조건을 주어진대로 따라 구현하는 시뮬레이션 유형이다.

n,m=map(int,input().split())
arr=[0]*n
for i in range(m):
  a,b,c=map(int,input().split())
  for j in range(a-1,b):
    arr[j]=c

for i in range(n):
  print(arr[i])