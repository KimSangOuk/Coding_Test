# 풀이시간 15분 시간제한 1초 메모리제한 128MB
# 1회차 정답
# 정수를 나타내는 범위로 보았을 때, 계수정렬을 사용하지 못하며 시간복잡도로 보았을 때는 데이터양이 500,000이기 때문에 집합이나 이진탐색을 사용해야 한다.

def binary_search(array,target,start,end):
  if start>end:
    return 0
  mid=(start+end)//2
  if array[mid]==target:
    return 1
  elif array[mid]>target:
    return binary_search(array,target,start,mid-1)
  else:
    return binary_search(array,target,mid+1,end)

n=int(input())
arr=list(map(int,input().split()))
arr.sort()
m=int(input())
check_list=list(map(int,input().split()))

for k in check_list:
  print(binary_search(arr,k,0,n-1))