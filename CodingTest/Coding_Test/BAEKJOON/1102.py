import sys

input = sys.stdin.readline

N = int(input())
costs = [list(map(int, input().split())) for _ in range(N)]
ofoff = list(input().strip())
P = int(input())

INF = 36 * 16

max_mask = 1 << N
dp = [-1] * max_mask

initial_mask = 0
initial_num = 0
for i in range(N):
    if ofoff[i] == 'Y':
        initial_mask |= (1 << i)
        initial_num += 1

def dfs(mask):
    if dp[mask] != -1:
        return dp[mask]

    num = bin(mask).count('1')

    if num >= P:
        dp[mask] = 0
        return 0

    min_cost = INF

    for i in range(N):
        if not (mask & (1 << i)):
            min_next_cost = INF

            for j in range(N):
                if mask & (1 << j):
                    min_next_cost = min(min_next_cost, costs[j][i])

            if min_next_cost == INF:
                continue

            new_mask = mask | (1 << i)
            cost_i = min_next_cost + dfs(new_mask)

            min_cost = min(min_cost, cost_i)

    dp[mask] = min_cost
    return dp[mask]

if initial_num >= P:
    print(0)
else:
    result = dfs(initial_mask)

    print(result if result < INF else -1)

