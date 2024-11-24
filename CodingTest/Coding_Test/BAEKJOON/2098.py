import sys
input=sys.stdin.readline

INF=int(1e9)

n=int(input())
w=[list(map(int,input().split())) for _ in range(n)]
memo=[[-1]*(2**n) for _ in range(n)]

def TSP(here,visited_cities,n,w,memo):
    if visited_cities==(1<<n)-1:
        return w[here][0] if w[here][0]>0 else INF

    if memo[here][visited_cities]!=-1:
        return memo[here][visited_cities]

    answer=INF

    for next_city in range(n):
        if not (visited_cities&(1<<next_city)) and w[here][next_city]>0:
            new_cost=w[here][next_city]+TSP(next_city,visited_cities|(1<<next_city),n,w,memo)
            answer=min(answer,new_cost)

    memo[here][visited_cities]=answer
    return answer

print(TSP(0,1,n,w,memo))