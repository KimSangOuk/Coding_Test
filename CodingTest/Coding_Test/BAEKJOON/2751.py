# 풀이시간 10분 시간제한 2초 메모리제한 256MB
# 1회차 정답
# 처음에는 단순 정렬문제 인줄 알았으나, 데이터의 수가 1,000,000가 된다는 것을 알았다. 그렇기 때문에 O(N) 정도가 되어야 되고 계수 정렬 O(N+K)를 이용해서 풀어내면 된다. 그렇게 되면 많아도 음수까지 포함이기 때문에 4,000,000이 때문에 정답 치를 구해낼 수 있음을 알 수 있다.

n=int(input())
count=[0]*2000001
for i in range(n):
  count[int(input())+1000000]+=1

for i in range(0,len(count)):
  if count[i]!=0:
    print(i-1000000)