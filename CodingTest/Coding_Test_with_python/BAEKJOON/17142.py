# 풀이시간 1시간 시간제한 0.25초 메모리제한 512MB
# 1회차 정답
# 완전탐색으로 경우의 수를 찾은 다음 그 경우 대로 BFS를 처리하는 문제이다. 각 바이러스가 M개 만큼 선택되는 경우의 수마다 바이러스를 퍼트려서 시간이 최소 얼마나 걸리는지 처리하는 문제이다. 최소 시간을 구해서 답으로 출력하면 된다. 시간복잡도는 10개중 고르는 조합에 배열의 규모가 BFS의 연산횟수와 같기 때문에 조합의 최대 수인 252에 2500을 곱해도 500만이 되지 않아서 충분히 가능하다.

from itertools import combinations
from collections import deque
import copy

dx=[0,0,-1,1]
dy=[1,-1,0,0]

n,m=map(int,input().split())

board=[]
virus=[]
count_empty=0
for i in range(n):
    arr=list(map(int,input().split()))
    for j in range(n):
        if arr[j]==0:
            count_empty+=1
            arr[j]=-1
        if arr[j]==2:
            virus.append((i,j))
            arr[j]='*'
        if arr[j]==1:
            arr[j]='-'
    board.append(arr)


min_time=2500
for case in combinations(virus,m):
    empty=count_empty
    board_tmp=copy.deepcopy(board)
    result=0
    q=deque()
    for x,y in case:
        board_tmp[x][y]=0
        q.append((0,x,y))
    while q:
        time,a,b=q.popleft()
        for i in range(4):
            nx=a+dx[i]
            ny=b+dy[i]
            if nx<0 or ny<0 or nx>=n or ny>=n:
                continue
            if board_tmp[nx][ny]==-1:
                board_tmp[nx][ny]=time+1
                result=time+1
                empty-=1
                q.append((time+1,nx,ny))
            elif board_tmp[nx][ny]=='*':
                board_tmp[nx][ny]=time+1
                q.append((time+1,nx,ny))
    # print(empty)
    # for i in range(n):
    #     print(board_tmp[i])
    if empty>0:
        continue
    min_time=min(min_time,result)

if min_time==2500:
    print(-1)
else:
    print(min_time)