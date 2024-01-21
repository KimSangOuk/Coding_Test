# 풀이시간 10분 시간제한 1초 메모리제한 256MB
# 1회차 정답
# 과자를 각 나누어주는 최대 길이를 구하는 문제이다. 목표가 길이이기 때문에 10억에서 탐색하기 때문에 이진 탐색을 사용한다고 생각할 수 있다. 이 때 목표를 조카의 수로 두고 불가능한 경우는 조카의 수가 과자의 모든 길이의 합보다 많을 경우 1만큼씩도 못주기 때문에 그 때를 0인 경우로 두면 된다. 나머지 경우에서는 각 과자당 조카에게 나누어줄 수 있는 개수를 구하여 더한 다음 그 값이 조카의 수보다 크거나 같으면 가능한 경우이므로 답으로 두고 과자의 수를 줄여보기 위해 값을 늘린다.

m,n=map(int,input().split())

array=list(map(int,input().split()))

def binary_search(array,target,start,end):
  if m>sum(array):
    return 0
  while start<=end:
    mid=(start+end)//2
    count=0
    for i in range(len(array)):
      count+=array[i]//mid
    if count>=target:
      result=mid
      start=mid+1
    else:
      end=mid-1
  return result

result=binary_search(array,m,1,max(array))
print(result)