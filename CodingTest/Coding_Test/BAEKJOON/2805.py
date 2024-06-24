# 풀이시간 5분 시간제한 1초 메모리제한 256MB
# 1회차 정답
# Parametric Search 유형의 대표적인 케이스이다. 이진탐색으로 푼다. 그렇기에 탐색할 수 있는 10억까지도 주어질 수 있다. 시간복잡도는 logN이기 때문에 충분히 가능하다. 조건을 맞추어 범위를 줄여가면서 풀어나가면 된다.

def binary_search(array,target,start,end):
  answer=0
  while start<=end:
    mid=(start+end)//2
    sum=0
    for i in array:
      if i>mid:
        sum+=i-mid
    if sum>=target:
      start=mid+1
      answer=mid
    else:
      end=mid-1
  return answer

n,m=map(int,input().split())
arr=list(map(int,input().split()))

print(binary_search(arr,m,0,max(arr)))