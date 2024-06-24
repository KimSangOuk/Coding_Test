# 풀이시간 3분 시간제한 1초 메모리제한 128MB
# 1회차 정답
# 큰 동전이 작은 동전의 배수가 되기 때문에 나누었을 때, 나머지 돈이 나머지 돈의 배수가 되므로 단순히 동전 크기가 큰 순으로 나누어서 갯수를 구하면 된다. 원하는 것부터 찾는 대표적인 그리디 유형이다.

pay=int(input())
change=1000-pay

coins=[500,100,50,10,5,1]
result=0

for coin in coins:
  result+=change//coin
  change%=coin

print(result)