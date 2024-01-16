# 풀이시간 5분 시간제한 1초 메모리제한 128MB
# 1회차 정답
# 각 수의 조합 중 합이 x가 되는 조합의 개수를 구하는데 모든 수를 탐색할 경우 시간이 오래 걸리기 때문에 그 범위를 줄이기 위해 제약을 걸어주면 된다.

n=int(input())
array=list(map(int,input().split()))
x=int(input())
array.sort()

count=0
for i in range(0,n-1):
  if array[i]>=x:
    continue
  for j in range(i+1,n):
    if array[i]+array[j]==x:
      count+=1
    elif array[i]+array[j]>x:
      break
print(count)