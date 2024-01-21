# 풀이시간 30분 시간제한 1초 메모리제한 128MB
# 1회차 정답
# 각 보석의 종류를 나누어 갯수를 구한 다음, 그 갯수가 목표의 갯수보다 작은지 큰지를 따지며 최솟값이 되도록 하는 문제이다. 이때 탐색을 해야하기 때문에 이진탐색을 사용하였다.

n,m=map(int,input().split())
array=[]
for _ in range(m):
  array.append(int(input()))

def binary_search(array,target,start,end):
  while start<=end:
    mid=(start+end)//2
    count=0
    for i in range(0,len(array)):
      if array[i]%mid==0:
        count+=array[i]//mid
      else:
        count+=array[i]//mid+1
    if count<=target:
      result=mid
      end=mid-1
    else:
      start=mid+1
  return result

result=binary_search(array,n,1,max(array))
print(result)