# 풀이시간 7분 시간제한 0.5초 메모리제한 128MB
# 1회차 정답
# 단순하게 두 포인터로 하나의 시작 점에서부터 끝까지로 두고 다른 포인터로 더해질 길이를 늘려가면서 m과 같아지는 비교하면서 답을 찾으면 되는 탐색문제이다.

n,m=map(int,input().split())

array=list(map(int,input().split()))

count=0
for i in range(n):
  tmp=0
  for j in range(i,n):
    tmp+=array[j]
    if tmp==m:
      count+=1
      break
    elif tmp>m:
      break

print(count)