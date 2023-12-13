import sys

# 떡의 개수(N)와 요청한 떡의 길이(M)을 입력받기
n,m=map(int,input().split())
# 각 떡의 개별 높이 정보를 입력받기
arr=list(map(int,sys.stdin.readline().split()))

answer=0
# 이진 탐색을 위한 시작점과 끝점 설정
start=0
end=max(arr)
# 이진 탐색 수행(반복적)
while start<=end:
  mid=(start+end)//2
  sum=0
  for i in arr:
    # 잘랐을 때의 떡의 양 계산
    if i>mid:
      sum+=i-mid
  # 떡의 양이 충분한 경우 덜 자르기(오른쪽 부분 탐색)
  if sum>=m:
    start=mid+1
    answer=mid # 최대한 덜 잘랐을 때가 정답이므로, 여기에서 result에 기록
  # 떡의 양이 부족한 경우 더 많이 자르기(오른쪽 부분 탐색)
  else:
    end=mid-1

# 정답 출력
print(answer)