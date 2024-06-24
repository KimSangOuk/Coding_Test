# 풀이시간 20분 시간제한 2초 메모리제한 128MB
# 1회차 정답
# 주어진 상황을 코드로 풀어내는 시뮬레이션 유형이다. 이 때 주어진 스위치 상태를 성별에 따라 다른 방식으로 뒤집으면 된다.

n=int(input())

switch_arr=[0]+list(map(int,input().split()))

def turn_switch(arr,sex,num):
  if sex==1:
    for i in range(num,len(arr)):
      if i%num==0:
        arr[i]=int(not bool(arr[i]))
  else:
    start=num
    end=num
    while True:
      d_s=start-1
      d_e=end+1
      if d_s<1 or d_e>len(arr)-1 or arr[d_s]!=arr[d_e]:
        break
      start-=1
      end+=1
    for i in range(start,end+1):
      arr[i]=int(not bool(arr[i]))
    

s=int(input())
for _ in range(s):
  sex,num=map(int,input().split())

  turn_switch(switch_arr,sex,num)

for i in range(1,n+1):
  print(switch_arr[i],end=" ")
  if i%20==0:
    print()
