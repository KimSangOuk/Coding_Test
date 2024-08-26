n,m=map(int,input().split())

def dfs(h,deep):
    global answer, visited
    if h<0 or deep<0 or h>=n or deep>=m:
        return False
    if board[h][deep]=='x':
        return False
    if visited[h][deep]:
        return False
    if deep==m-1:
        answer+=1
        visited[h][deep]=True
        return True
    visited[h][deep]=True
    if dfs(h-1,deep+1):
        return True
    if dfs(h,deep+1):
        return True
    if dfs(h+1,deep+1):
        return True
    return False


board=[list(input()) for _ in range(n)]
answer=0
visited=[[False]*m for _ in range(n)]
for h in range(n):
    dfs(h,0)

print(answer)