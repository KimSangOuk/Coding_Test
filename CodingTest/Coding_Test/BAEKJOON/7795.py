# 풀이시간 8분 시간제한 1초 메모리제한 256MB
# 1회차 정답
# 문제에서 한 배열에서의 특정 수보다 작은 수의 갯수를 구하는 문제이다. 데이터의 크기가 20,000이기 때문에 모든 수를 비교하는 N^2의 시간복잡도는 불가능하다. 그렇다면 각 수를 O(N)으로 비교해 나가거나 특정 위치를 찾아내야 하는데 그러기 위한 방법으로 정렬 후 이진탐색으로 인덱스를 찾을 수 있는 방법이 있다. 정렬과 이진탐색모두 시간복잡도가 NlogN으로 가능하다.

import bisect

for tc in range(int(input())):
  n,m=map(int,input().split())
  array1=list(map(int,input().split()))
  array2=list(map(int,input().split()))
  array2.sort()
  answer=0
  for x in array1:
    answer+=bisect.bisect_left(array2,x)
  print(answer)