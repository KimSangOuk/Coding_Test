# 풀이시간 10분 시간제한 1초 메모리제한 128MB
# 1회차 정답
# 모든 그 수보다 작거나 같은 자연수를 돌면서 탐색하는 완전탐색, 브루트 포스 문제이다.

n,k=map(int,input().split())
answer=[]

for i in range(1,n+1):
  if n%i==0:
    answer.append(i)

if k<=len(answer):
  print(answer[k-1])
else:
  print(0)