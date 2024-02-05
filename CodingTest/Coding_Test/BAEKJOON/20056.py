# 풀이시간 1시간 시간제한 1초 메모리제한 512MB
# 1회차 오답 - 틀린 이유를 찾지 못함
# GPT랑 대화를 나눠본 결과 방향 처리 부분에서 문제가 발생한다는 것까지는 알았지만 왜 발생하는지는 찾지 못했다. 처음에 방향 처리를 하면서 이동시키면서 방향을 지속적으로 홀수, 짝수가 이어지는지 테스트하면 오류가 나오고 그렇지 않고 방향을 전부 담아서 실행하면 답이 나온다.
# 틀린 이유는 결국에 찾지는 못했지만 배열이 복잡해질 때, 딕테이션을 사용하는 것도 그렇고, all 함수를 사용하는 방법도 그렇고 코드를 간단화 할 수 있는 방법들이 몇가지 배울 점들이 있다고 생각했다.

N, M, K = map(int, input().split())

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

fireball = []
board = [[{'count': 0, 'mass': 0, 'speed': 0, 'directions': []} for _ in range(N)] for _ in range(N)]

for _ in range(M):
    r, c, m, s, d = map(int, input().split())
    fireball.append((r-1, c-1, m, s, d))

while K > 0:
    K -= 1
    # 보드 초기화 및 방향 리스트 초기화
    board = [[{'count': 0, 'mass': 0, 'speed': 0, 'directions': []} for _ in range(N)] for _ in range(N)]

    # 파이어볼 이동
    for r, c, m, s, d in fireball:
        nx = (r + s * dx[d]) % N
        ny = (c + s * dy[d]) % N
        board[nx][ny]['count'] += 1
        board[nx][ny]['mass'] += m
        board[nx][ny]['speed'] += s
        board[nx][ny]['directions'].append(d)

    fireball = []
    # 파이어볼 분할 및 방향 처리
    for i in range(N):
        for j in range(N):
            if board[i][j]['count'] > 1:
                if board[i][j]['mass'] // 5 > 0:  # 질량이 0 이상일 때만 처리
                    m, s, d_list = board[i][j]['mass'] // 5, board[i][j]['speed'] // board[i][j]['count'], board[i][j]['directions']
                    even = all(d % 2 == 0 for d in d_list)
                    odd = all(d % 2 != 0 for d in d_list)
                    new_directions = [0, 2, 4, 6] if even or odd else [1, 3, 5, 7]
                    for d in new_directions:
                        fireball.append((i, j, m, s, d))
            elif board[i][j]['count'] == 1:
                fireball.append((i, j, board[i][j]['mass'], board[i][j]['speed'], board[i][j]['directions'][0]))

result = sum(fb[2] for fb in fireball)
print(result)