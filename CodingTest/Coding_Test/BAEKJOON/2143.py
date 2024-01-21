# 풀이시간 60분/60분 시간제한 2초 메모리제한 64MB
# 1회차 정답
# 각 배열에서 부분합이 되는 모든 경우를 구해서 다른 배열에서의 부분합의 모든 경우를 맞춰보아야 가지 수를 찾을 수 있다고 생각을 하였다. 그렇게 하기 위해서는 모두 찾아서 모두 비교하는 완전탐색 방법이 있는데 시간복잡도 상 불가능하다고 생각이 들었다. 그러던 중 우리에게 필요한 것은 각 배열의 시작점이 다를 때마다 누적이 되는 '값'이 필요한 것이기 때문에 각 시작점에서 끝점까지 모든 경우를 구해서 그 배열의 넣고 다른 배열에서의 누적합을 구해서 합이 T가 되는 갯수만을 구해내면 되기 때문에, bisect를 이용해서 갯수를 각 구해내었다. 총 2초의 시간이 걸리기 때문에 약 4000만 회의 연산이 이루어져야 하는데 하나의 모든 배열의 가짓수를 탐색하는데 100만/2, 그 배열을 정렬하는데 NlogN 또 새롭게 탐색에 똑같이 50만, 그리고 50만의 배열에서 탐색하는데 2logN이 든다. 그렇기에 다 합쳐보면 가능하다는 결론이 나온다.

import bisect

t=int(input())
n=int(input())
array_a=list(map(int,input().split()))
m=int(input())
array_b=list(map(int,input().split()))

count=0
array_sum_b=[]
for i in range(m):
  tmp_sum=0
  for j in range(i,m):
    array_sum_b.append(tmp_sum+array_b[j])
    tmp_sum+=array_b[j]
array_sum_b.sort()

for i in range(n):
  tmp_sum=0
  for j in range(i,n):
    k=tmp_sum+array_a[j]
    tmp_sum+=array_a[j]
    count+=bisect.bisect_right(array_sum_b,t-k)-bisect.bisect_left(array_sum_b,t-k)

print(count)
