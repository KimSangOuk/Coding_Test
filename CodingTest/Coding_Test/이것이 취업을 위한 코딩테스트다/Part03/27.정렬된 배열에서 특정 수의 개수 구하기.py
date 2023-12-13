# 풀이시간 10분/30분 시간제한 1초 메모리제한 128MB
# 1회차 정답 - but 복잡한 bisect 함수의 구현은 풀어볼만 하다고 판단
# 시간복잡도가 logN이 무조건 나와야 하기 때문에 이진탐색을 사용해야만 한다.
# 나같은 경우 기존 구현되어 있는 함수를 사용했으나 풀이에서 이 함수들의 구현방식을 설명하고 있어 직접 한번 구현해보고 다시 풀어보기로 하였다.

from bisect import bisect_left,bisect_right

n,x=map(int,input().split())
arr=list(map(int,input().split()))

count=bisect_right(arr,x)-bisect_left(arr,x)

if count==0:
  print(-1)
else:
  print(count)

# 답안 예시
# 정렬된 수열에서 값이 x인 원소의 개수를 세는 메서드
def count_by_value(array,x):
  # 데이터의 개수
  n = len(array)

  # x가 처음 등장한 인덱스 계산
  a=first(array,x,0,n-1)

  # 수열에 x가 존재하지 않는 경우
  if a==None:
    return 0 # 값인 원소의 개수는 0개이므로 0 반환

  # x가 마지막으로 등장한 인덱스 계산
  b=last(array,x,0,n-1)

  # 개수를 반환
  return b-a+1

# 처음 위치를 찾는 이진 탐색 메서드
def first(array,target,start,end):
  if start>end:
    return None
  mid=(start+end)//2
  # 해당 값을 가지는 원소 중에서 가장 왼쪽에 있는 경우에만 인덱스 반환
  if (mid==0 or target>array[mid-1]) and array[mid]==target:
    return mid
  # 중간점의 값 보다 찾고자 하는 값이 작거나 같은 경우 왼쪽 확인
  elif target<=array[mid]:
    return first(array,target,start,mid-1)
  # 중간점의 값 보다 찾고자 하는 값이 큰 경우 오른쪽 확인
  else:
    return first(array,target,mid+1,end)

# 마지막 위치를 찾는 이진 탐색 메서드
def last(array,target,start,end):
  if start>end:
    return None
  mid=(start+end)//2
  # 해당값을 가지는 원소 중에서 가장 오른쪽에 있는 경우에만 인덱스 반환
  if (mid==len(array)-1 or target<array[mid+1]) and array[mid]==target:
    return mid
  # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
  elif target<array[mid]:
    return last(array,target,start,mid-1)
    # 중간점의 값 보다 찾고자 하는 값이 크거나 같은 경우 오른쪽 확인
  else:
    return last(array,target,mid+1,end)

n,x=map(int,input().split()) # 데이터의 개수 N, 찾고자 하는 값 x를 입력받기
array =list(map(int,input().split())) # 전체 데이터 입력받기

# 값이 x인 데이터의 개수 계산
count=count_by_value(array,x)

# 값이 x인 원소가 존재하지 않는다면
if count==0:
  print(-1)
# 값인 x인 원소가 존재한다면
else:
  print(count)