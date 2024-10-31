from collections import deque

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs(x, y, resultVisited):
    visited = [[-1] * (w + 2) for _ in range(h + 2)]
    q = deque()
    q.append((x, y))
    visited[x][y] = 0
    while q:
        now = q.popleft()
        for i in range(4):
            nx = now[0] + dx[i]
            ny = now[1] + dy[i]
            if nx < 0 or ny < 0 or nx >= h + 2 or ny >= w + 2:
                continue
            if visited[nx][ny] != -1:
                continue
            if board[nx][ny] == '*':
                continue
            if board[nx][ny] != '#':
                visited[nx][ny] = visited[now[0]][now[1]]
                q.appendleft((nx, ny))
            else:
                visited[nx][ny] = visited[now[0]][now[1]] + 1
                q.append((nx, ny))
    for i in range(h + 2):
        for j in range(w + 2):
            resultVisited[i][j] += visited[i][j]

for tc in range(int(input())):
    h, w = map(int, input().split())
    prisoners = []
    board = [['.'] * (w + 2) for _ in range(h + 2)]

    for i in range(1, h + 1):
        arr = list(input())
        for j in range(1, w + 1):
            if arr[j - 1] == '$':
                prisoners.append((i, j))
            board[i][j] = arr[j - 1]

    # 누적 합산용 resultVisited 초기화
    resultVisited = [[0] * (w + 2) for _ in range(h + 2)]
    prisoners.append((0, 0))
    for x, y in prisoners:
        bfs(x, y, resultVisited)

    # 최소 비용 계산
    result = 1e9
    for i in range(h + 2):
        for j in range(w + 2):
            if board[i][j] == '*':  # 벽인 경우 무시
                continue
            total_cost = resultVisited[i][j]
            if board[i][j] == '#':  # 문인 경우 중복되는 비용 -2 처리
                total_cost -= 2
            if total_cost >= 0:  # 유효한 경로만 고려
                result = min(result, total_cost)

    print(result)
