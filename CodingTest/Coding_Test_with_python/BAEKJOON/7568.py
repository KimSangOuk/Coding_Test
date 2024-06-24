# 풀이시간 10분 시간제한 1초 메모리제한 128MB
# 1회차 정답
# 알고리즘 아이디어를 생각했을 때, 인원수를 전체 탐색하는 완전탐색의 형태가 나오기도 하고, 최대 인원이 50이라 찾더라도 O(N^3)까지 시간복잡도가 가능하기 때문에 시간복잡도보다는 구현을 고려하고 전체 인원을 일일이 탐색하는 브루트 포스 알고리즘을 사용했다.

n=int(input())
arr=[]
for _ in range(n):
  x,y=map(int,input().split())
  arr.append((x,y))

result=[0]*n
for i in range(n):
  count=0
  for j in range(n):
    if i==j:
      continue
    elif arr[i][0]<arr[j][0] and arr[i][1]<arr[j][1]:
      count+=1
  result[i]=count+1

for i in range(n):
  print(result[i],end=' ')