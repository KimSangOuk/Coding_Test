# 풀이시간 7분 시간제한 1초 메모리제한 256MB
# 1회차 정답
# m의 크기가 엄청 작아서 O(N^3)까지 봐도 되는 정도였다. 그렇기에 구현에 더 집중하는 상황을 있는그대로 만들어내는 시뮬레이션 유형이다.
# 배열을 슬라이싱한 부분에 바로 그 부분에 대입이 되는지 처음알았다.

n,m=map(int,input().split())
arr=[0]
for i in range(1,n+1):
  arr.append(i)
for _ in range(m):
  i,j=map(int,input().split())
  new_arr=arr[i:j+1]
  new_arr.reverse()
  arr[i:j+1]=new_arr
for i in range(1,n+1):
  print(arr[i],end=' ')