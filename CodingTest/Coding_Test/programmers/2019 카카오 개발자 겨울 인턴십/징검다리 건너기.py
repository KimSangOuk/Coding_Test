def func(stones,k,mid):
  stack=0
  for i in range(len(stones)):
      if stones[i]>=mid:
          stack=0
      else:
          stack+=1
      if stack==k:
          return False
  return True

def binary_search(stones,k):
  answer=0
  start=1
  end=max(stones)
  while start<=end:
      mid=(start+end)//2
      if func(stones,k,mid):
          answer=mid
          start=mid+1
      else:
          end=mid-1
  return answer


def solution(stones, k):
  answer = 0

  answer=binary_search(stones,k)

  return answer