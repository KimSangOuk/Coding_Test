# 풀이시간 15분 시간제한 1초 메모리제한 128MB
# 1회차 정답
# 제일 큰 예산 100,000까지 중에 적절한 값을 찾아야하므로 우리는 이진탐색의 매개변수탐색을 통해 범위를 좁혀가며 구할 수 있다.

def binary_search(array,target,start,end):
  while start<=end:
    mid=(start+end)//2
    total=0
    for money in array:
      if money<=mid:
        total+=money
      else:
        total+=mid
    if total<=target:
      result=mid
      start=mid+1
    else:
      end=mid-1
  return result

n=int(input())
array=list(map(int,input().split()))

total=int(input())

print(binary_search(array,total,0,max(array)))