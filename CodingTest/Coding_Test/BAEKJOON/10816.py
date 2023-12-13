# 풀이시간 10분 시간제한 1초 메모리제한 128MB
# 1회차 정답
# 데이터가 500,000이기 때문에 계수정렬, 이진탐색을 이용하여 구할 수 있지만 정렬과정에서 계수정렬이 숫자를 세기 때문에 계수정렬로 풀었다. 최대 크기가 20,000,000 즉 80MB가 되기 때문에 가능하다. 아마 이진탐색으로 정렬 후 풀 수 있겠지만 NlogN의 sort()함수를 먼저 이용하므로 자제했다.

count=[0]*20000001

n=int(input())
arr=list(map(int,input().split()))

for k in arr:
  count[k+10000000]+=1

m=int(input())
check_list=list(map(int,input().split()))

for k in check_list:
  print(count[k+10000000])