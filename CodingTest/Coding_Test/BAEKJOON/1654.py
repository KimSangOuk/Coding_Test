# 풀이시간 20분 시간제한 2초 메모리제한 128MB
# 1회차 정답
# 랜선의 길이가 무지막지하게 크기 때문에 이 중에서 자르는 값을 찾기 위해서는 이진 탐색을 사용해야 하고 크거나 같은 값을 찾는 문제이기 때문에 Parametic search 알고리즘이므로 이진탐색을 사용하기도 한다.
# 문제에서 잠시 헷갈렸던 것이 어떤 전선이든 잘라서 전체 갯수를 맞추면 되었는데 나는 k개만 기준으로 보다보니 헷갈렸다.

import sys

def binary_search(array,target,start,end):
  answer=0
  while start<=end:
    mid=(start+end)//2
    value=0
    for i in array:
      value+=i//mid
    if value>=target:
      start=mid+1
      answer=mid
    else:
      end=mid-1
  return answer

k,n=map(int,input().split())
array=[]
for _ in range(k):
  array.append(int(sys.stdin.readline()))

print(binary_search(array,n,1,max(array)))