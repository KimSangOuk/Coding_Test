# 풀이시간 15분 시간제한 2초 메모리제한 512MB
# 1회차 정답
# 한 도시에서 다른 도시로 갈 때, 그 한 구간에서의 최소값이 될 수 있는 경우를 찾아서 누적시켜서 출력하면 된다. 그렇기 때문에, 지금 순간에 필요한 값만 찾아나가는 그리디 알고리즘이라고 볼 수 있다. 시간복잡도는 N-1번 연산이 실행되므로 O(N)이기 때문에 데이터의 수100,000으로 가능하다.

n=int(input())

road=list(map(int,input().split()))

price=list(map(int,input().split()))

result=0
min_price=int(1e9)
for i in range(n-1):
  min_price=min(price[i],min_price)
  result+=road[i]*min_price

print(result)