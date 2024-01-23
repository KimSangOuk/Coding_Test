# 풀이시간 초과 시간제한 2초 메모리제한 512MB
# 1회차 오답 - 풀이방법에 접근하지 못함
# 먼저 풀이방법부터 보자면, 현재의 물건의 무게가 배낭의 최대 무게보다 크다면 넣지 못하기 때문에 전의 물건을 넣었을 때의 같은 최대 무게에서의 최대 가치를 가져오면 되고 만약 들어갈 수 있다면, 그 물건을 넣기 전의 하중에 그 물건을 넣기 전의 최대 가치에 지금의 가치를 더해준 값이나 위의 넣지 못한 경우에서의 값 중 큰 수를 넣으면 된다.
# 왜 이 방법을 생각하지 못했는가? 먼저 2차원 배열로 기록한다는 것으로 접근하지 못한 것이 제일 큰데 2차원 배열로 접근하지 못한 이유는? 우리가 전의 값에서 필요로 한 조건이 두가지 무게와 어떤 물건을 넣었는지이다. 이 2가지 조건이 있어도 접근하지 못하고 다른 set를 쓰는 식의 방식을 썼는데 이는 조건이 두가지 이상 일때, 이 조건을 dp의 조건으로 두어서 접근해본적이 없기 때문에 접근하지 못했다. 다른 2차원으로 비교하는 문제인 편집 거리같은 경우는 조건이 2가지 이상이라기 보다는 특정 문자열에서 다른 문자열로 변화한다는 느낌이 더 컸기 때문에 비교 이외에도 2차원 배열을 쓰는 케이스가 있다는 것을 배웠다.

n,k=map(int,input().split())

dp=[0]*(k+2)
dp_set=[set() for _ in range(k+2)]

w=[]
v=[]
for i in range(n):
    a,b=map(int,input().split())
    w.append(a)
    v.append(b)

for i in range(1,k+2):
    dp[i]=dp[i-1]
    for j in range(n):
        if i-w[j]>0 and w[j] not in dp_set[i-w[j]]:
            dp[i]=max(dp[i],dp[i-w[j]]+v[j])
    for j in range(n):
        if i-w[j]>0 and dp[i]==dp[i-w[j]]+v[j]:
            dp_set[i]=dp_set[i-w[j]].copy()
            dp_set[i].add(w[j])
    if dp[i]==dp[i-1]:
        dp_set[i]=dp_set[i-1].copy()

print(dp[k+1])
# for i in range(1,k+1):
    # print(i,dp_set[i])

# 답안지
import sys

N, K = map(int, input().split())
stuff = [[0,0]]
knapsack = [[0 for _ in range(K + 1)] for _ in range(N + 1)]

for _ in range(N):
    stuff.append(list(map(int, input().split())))


#냅색 문제 풀이
for i in range(1, N + 1):
    for j in range(1, K + 1):
        weight = stuff[i][0] 
        value = stuff[i][1]

        if j < weight:
            knapsack[i][j] = knapsack[i - 1][j] #weight보다 작으면 위의 값을 그대로 가져온다
        else:
            knapsack[i][j] = max(value + knapsack[i - 1][j - weight], knapsack[i - 1][j])

print(knapsack[N][K])
