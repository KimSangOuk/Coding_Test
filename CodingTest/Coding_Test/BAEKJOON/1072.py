# 풀이시간 45분 시간제한 2초 메모리제한 128MB
# 1회차 정답
# 단순히 승률을 계산하면서 데이터의 최대 크기가 10억이기 때문에 그 중에서 이진탐색으로 답을 찾으며 O(logN)으로 풀어주면 되는 문제이다.
# 여기서 한가지 깨달았다. 실수로 연산을 할 경우 오차가 발생할 수 있기 때문에 가능한 소수점까지로 내려가지 않도록 계산을 해주어야 한다는 점이다.

x,y=map(int,input().split())

z=y*100//x

def binary_search(x,y,target,start,end):
  result=-1
  while start<=end:
    mid=(start+end)//2
    win=(y+mid)*100//(x+mid)
    if target>=win:
      start=mid+1
    else:
      result=mid
      end=mid-1
  return result

if x==y:
  print(-1)
else:
  print(binary_search(x,y,z,0,int(1e9)))