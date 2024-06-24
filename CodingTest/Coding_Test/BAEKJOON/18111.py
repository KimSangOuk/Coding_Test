# 풀이시간 50분/30분 시간제한 1초 메모리제한 1024MB
# 1회차 오답 - 시간이 너무 오래 걸림, 시간초과를 해결하지 못함
# 단순히 3차원으로 돌려도 시간복잡도 상으로 가능한 문제이다. 하지만 시간초과를 해결하지 못했는데 처음 보는 지식이었다. 2차원 배열에 깊이 접근할 때 따로 2차원 배열 중 1차원을 끊어서 받아서 접근하면 시간복잡도가 획기적으로 줄어든다는 것이다.

import sys
input=sys.stdin.readline

n,m,B=map(int,input().split())
board=[]
sum_value=0
for _ in range(n):
    board.append(list(map(int,input().split())))

min_value=int(1e9)
result=0
for k in range(0,257):
    b=B
    time=0
    for i in range(n):
        sub=board[i]
        for j in range(m):  
            if sub[j]<k:
                b-=k-sub[j]
                time+=k-sub[j]
            else:
                b+=sub[j]-k
                time+=2*(sub[j]-k)
    if b<0:
        continue
    if min_value>=time:
        result=k
        min_value=time

print(min_value,result)
