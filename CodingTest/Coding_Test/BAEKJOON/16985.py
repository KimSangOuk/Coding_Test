import sys
from collections import deque
input = sys.stdin.readline

dx = [0, 0, -1, 1, 0, 0]
dy = [-1, 1, 0, 0, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

mazeBlocks = []
for _ in range(5):
    block = [list(map(int, input().split())) for _ in range(5)]
    mazeBlocks.append(block)

def get_rotations(layer):
    rotations = [layer]
    for _ in range(3):
        layer = [list(reversed(col)) for col in zip(*layer)]
        rotations.append(layer)
    return rotations

rotations = [get_rotations(layer) for layer in mazeBlocks]

answer = float('inf')

def bfs(board):
    global answer
    if board[0][0][0] == 0 or board[4][4][4] == 0:
        return
    visited = [[[False]*5 for _ in range(5)] for _ in range(5)]
    q = deque()
    q.append((0, 0, 0, 0))
    visited[0][0][0] = True
    while q:
        x, y, z, dist = q.popleft()
        if dist >= answer:
            continue
        if x == 4 and y == 4 and z == 4:
            answer = dist
            return
        for i in range(6):
            nx, ny, nz = x + dx[i], y + dy[i], z + dz[i]
            if 0 <= nx < 5 and 0 <= ny < 5 and 0 <= nz < 5:
                if not visited[nx][ny][nz] and board[nx][ny][nz] == 1:
                    visited[nx][ny][nz] = True
                    q.append((nx, ny, nz, dist + 1))

from itertools import permutations, product

for perm in permutations(range(5)):
    for rotation_indices in product(range(4), repeat=5):
        board = []
        for idx, rot_idx in zip(perm, rotation_indices):
            board.append(rotations[idx][rot_idx])
        maze = [[[board[k][i][j] for k in range(5)] for j in range(5)] for i in range(5)]
        if maze[0][0][0] == 0 or maze[4][4][4] == 0:
            continue
        bfs(maze)
        if answer == 12:
            print(12)
            sys.exit(0)

print(-1 if answer == float('inf') else answer)
