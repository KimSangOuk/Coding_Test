# 2회차 풀이










# 풀이시간 시간초과/60분 시간제한 1초 메모리제한 256MB
# 1회차 오답 - 풀이방법에 접근하지 못함
# 이진탐색보다는 풀이가 투 포인터에 가까웠다. 나같은 경우는 하나를 찾고 다른 하나를 이진탐색으로 찾은 다음, 또 다른 하나 또한 이진 탐색으로 찾아가는 아이디어를 사용하였다. 이렇게 할 경우, 문제가 뭔지는 모르겠지만 답에 도달할 수 없었다. 아무래도 특이케이스가 존재하는 모양이다.
# 하나를 정해두고 범위를 줄이면서 나머지 두개를 찾아가는 문제이다. 단순 투 포인터 문제라고 할 수 있을것 같다. 이분탐색 문제라고 생각하고 풀었다가 결국 풀지 못하여서 다시 한번 풀어보기로 하였다.

import copy

INF=int(3e9)

n=int(input())
array=list(map(int,input().split()))
array.sort()

def binary_search(array,one,start,end):
  result=INF
  answer=[]
  while start<=end:
    mid=(start+end)//2
    two=array[mid]
    t=abs(one+two)
    if result==t:
      answer.append(two)
    elif result>t:
      result=t
      answer=[]
      answer.append(two)
    if -one==two:
      return answer
    if -one>two:
      start=mid+1
    else:
      end=mid-1
  return answer

min_result=INF
answer=[]
for i in range(0,n):
  tmp=copy.deepcopy(array)
  tmp.remove(array[i])
  first=array[i]
  seconds=binary_search(tmp,first,0,len(tmp)-1)
  for second in seconds:
    # print(second)
    tmp.remove(second)
    third=binary_search(tmp,first+second,0,len(tmp)-1)[0]
    if abs(first+second+third)<min_result:
      min_result=abs(first+second+third)
      answer=[first,second,third]
    tmp.append(second)
    tmp.sort()
  

answer.sort()
for i in range(3):
  print(answer[i],end=' ')

# 답안지
import sys

n = int(input())
array = list(map(int, input().split()))

array.sort()
minTake = sys.maxsize

for i in range(n-2):
    start = i + 1
    end = n - 1
    while start < end:
        take = array[i] + array[start] + array[end]
        if abs(take) < minTake:
            minTake = abs(take)
            result = [array[i], array[start], array[end]]
        if take < 0:
            start += 1
        elif take > 0:
            end -= 1
        else:
            break

print(result[0], result[1], result[2])