# 풀이시간 5분 시간제한 2초 메모리제한 256MB
# 1회차 정답
# 데이터의 크기가 500,000이기 때문에 NlogN보다 빠른 N이나 logN으로 접근하는 것이 맞는 풀이이다. 그렇기에 이진탐색을 이용하거나 계수정렬, set in을 사용하는 것이 적당하다. 이 풀이에서는 set에 익숙해지기 위해 set in으로 풀었다.

n=int(input())
arr=set(map(int,input().split()))

m=int(input())
check_list=list(map(int,input().split()))

for k in check_list:
  if k in arr:
    print('1',end=' ')
  else:
    print('0',end=' ')