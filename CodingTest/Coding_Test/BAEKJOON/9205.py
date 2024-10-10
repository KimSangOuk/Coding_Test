from collections import deque
def bfs(pos):
    visited=[False]*(len(pos))
    visited[0]=True
    q=deque()
    q.append(0)
    while q:
        now=q.popleft()
        for i in range(1,n+2):
            dist=abs(pos[i][0]-pos[now][0])+abs(pos[i][1]-pos[now][1])
            if dist<=1000 and not visited[i]:
                if i==n+1:
                    return True
                visited[i]=True
                q.append(i)
    return False

for _ in range(int(input())):
    n=int(input())
    pos=[]
    for _ in range(n+2):
        pos.append(tuple(map(int,input().split())))
    if bfs(pos):
        print("happy")
    else:
        print("sad")
