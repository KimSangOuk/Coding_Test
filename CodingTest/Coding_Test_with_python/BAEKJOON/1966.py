# 풀이시간 30분 시간제한 2초 메모리제한 128MB
# 1회차 정답
# 식에서 index를 포함시키지 않으려고 하다가 조금 오래걸려버린 케이스이다. 필요하면 포함시켜야되는데 최대한 간단화 하려다보니 고집을 부리느라 시간이 걸렸다. 문제 자체는 그냥 2초대 시간에다가 크기도 100 이하이기 때문에 시간복잡도 보다는 순서대로 구현에 집중하는 시뮬레이션 유형이다.

import sys

t=int(input())

testcase=0
while testcase<t:
  testcase+=1
  n,m=map(int,sys.stdin.readline().split())
  arr=list(map(int,sys.stdin.readline().split()))
  new_arr=[]
  count=0
  result=0
  for i in range(n):
    new_arr.append((i,arr[i]))
  while len(new_arr)>0:
    max_num=0
    for i in range(len(new_arr)):
      max_num=max(max_num,new_arr[i][1])
    if new_arr[0][1]==max_num:
      count+=1
      find=new_arr.pop(0)
      if find[0]==m:
        result=count
        break
    else:
      new_arr.append(new_arr.pop(0))
  print(result)