# 풀이시간 10분/20분 시간제한 1초 메모리제한 128Mb
# 1회차 정답
# 문제에서 시간복잡도 자체를 logN으로 주고 있기 때문에 이진 탐색으로 푸는 문제이다. 찾는 것은 인덱스와 그 인덱스의 값이 같은 경우이기 때문에 그 값을 반영해서 이진탐색 함수를 설계하면 되는 간단한 문제이다.

def binary_search(array,start, end):
  while start<=end:
    mid=(start+end)//2
    if array[mid]==mid:
      return mid
    elif array[mid]<mid:
      start=mid+1
    else:
      end=mid-1
  return None

n=int(input())
arr=list(map(int,input().split()))

answer=binary_search(arr,0,len(arr))

if answer==None:
  print(-1)
else:
  print(answer)