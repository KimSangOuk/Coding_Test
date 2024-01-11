# 풀이시간 10분 시간제한 1초 메모리제한 128MB
# 1회차 정답
# 동전 문제처럼 각 단위가 배수관계를 이루진 않지만 정렬해서 큰 수부터 나누었을 때, 갯수의 합이 큰 수로 나누었을 때 작기 때문에 가능하다. 즉, 나머지 수들로 충분히 제일 큰 수를 만들 수 있기 때문에 가능한 것이다. 만약 만들지 못한다면 갯수가 달라질 수도 있다.

t=int(input())
coins=[25,10,5,1]


for i in range(t):
  n=int(input())
  count=[0]*4
  for coin in coins:
    count[coins.index(coin)]+=n//coin
    n%=coin

  for k in count:
    print(k,end=' ')
  print()