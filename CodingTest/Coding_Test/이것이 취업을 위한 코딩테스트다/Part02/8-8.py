n,m=map(int,input().split())

coins=[]

for _ in range(n):
  coins.append(int(input()))

dp=[int(1e9)]*(m+1)
dp[0]=0
for i in range(1,m+1):
  for c in coins:
    if i-c>=0:
      dp[i]=min(dp[i],dp[i-c]+1)

if dp[m]==int(1e9):
  print(-1)
else:
  print(dp[m])

# 집중력이 흐트려지기 시작해서 집중이 안되서 원래 풀이대로 그냥 풀면되는걸 한참 돌아가서 품
# 그냥 변수 하나하나의 의미도 신경안쓰고 그냥 코드만 만지는 상태가 됨.
# 아이디어 적인 측면이나 전체적인 풀이는 대략 맞으니 다시 풀어보기로 함.

# import sys

# n,m=map(int,input().split())

# array=[]
# for _ in range(n):
#   array.append(int(sys.stdin.readline()))

# d=[10001]*(m+1)

# d[0]=0

# for i in range(1,m+1):
#   for k in array:
#     if i-k>=0 and d[i-k]!=10001:
#       d[i]=min(d[i],d[i-k]+1)

# if d[m]==10001:
#   print(-1)
# else:
#   print(d[m])