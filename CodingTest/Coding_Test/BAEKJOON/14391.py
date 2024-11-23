n,m=map(int,input().split())
board=[list(map(int,list(input()))) for _ in range(n)]

answer=0
visited_set=set()

def dfs(visited,midSum):
    global answer

    if (visited, midSum) in visited_set:
        return
    visited_set.add((visited, midSum))
    if visited == (1 << (n * m)) - 1:
        answer = max(answer, midSum)
        return
    for i in range(n):
        for j in range(m):
            if visited&(1<<(m*i+j)):
                continue
            tempNum = 0
            tempVisited = visited
            for a in range(j, m):
                if tempVisited & (1 << (m * i + a)):
                    break
                tempVisited |= (1 << (m * i + a))
                tempNum = tempNum * 10 + board[i][a]
                dfs(tempVisited, midSum + tempNum)

            tempNum = 0
            tempVisited = visited
            for b in range(i, n):
                if tempVisited & (1 << (m * b + j)):
                    break
                tempVisited |= (1 << (m * b + j))
                tempNum = tempNum * 10 + board[b][j]
                dfs(tempVisited, midSum + tempNum)

dfs(0,0)
print(answer)