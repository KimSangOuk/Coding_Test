# 풀이시간 5분 시간제한 1초 메모리제한 128MB
# 1회차 정답
# 방의 수까지 1부터 올려가면서 그 수가 올라갈 때마다 모든 방의 배수가 되는 수를 열었다 닫았다를 반복하고 마지막에 열려있는 방의 수를 세면 되는 문제이다.

for tc in range(int(input())):
  n=int(input())
  arr=[1]*(n+1)
  for i in range(1,n+1):
    for j in range(1,n+1):
      if j%i==0:
        arr[j]=int(not bool(arr[j]))
  
  count=0
  for i in range(1,n+1):
    if arr[i]==0:
      count+=1
  print(count)