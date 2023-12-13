# 풀이시간 10분 시간제한 5초 메모리제한 8MB
# 1회차 정답
# 메모리제한을 최소화 시킨 문제로써 데이터의 갯수를 확인하고 최소한으로 배열의 크기를 주어야되는 문제이다. 문제에서는 8MB이므로 최대 2,000,000의 크기까지만 줄 수 있는데 처음에는 수의 갯수와 착각해서 주었다가 틀리길래 깨달았다.

import sys
n=int(input())

count=[0]*10001

for _ in range(n):
  count[int(sys.stdin.readline())]+=1

for i in range(1,len(count)):
  for j in range(count[i]):
    print(i)