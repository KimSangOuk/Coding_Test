N = int(input())
coins = [[0] * N for _ in range(N)]
inputArr = [list(input()) for _ in range(N)]

# 초기 입력 값으로 coins 배열 초기화
for i in range(N):
    for j in range(N):
        if inputArr[i][j] == 'H':
            coins[i][j] = 1

# 행 반전 함수
def reverse_row(arr, i):
    for j in range(N):
        arr[i][j] = 1 - arr[i][j]

# 열의 뒤집힌 비트 카운트
def count_column_flips(arr):
    total_flips = 0
    for j in range(N):
        cnt = sum(arr[i][j] for i in range(N))
        total_flips += min(cnt, N - cnt)  # 최적의 열 반전 횟수 선택
    return total_flips

answer = float('inf')

# 모든 행 반전 조합 시도
for mask in range(1 << N):
    # 원본 배열의 복사본 생성
    tmp = [row[:] for row in coins]

    # 비트마스크를 이용해 각 행을 반전
    for i in range(N):
        if mask & (1 << i):
            reverse_row(tmp, i)

    # 최소 열 반전을 계산
    flips = count_column_flips(tmp)
    answer = min(answer, flips)

print(answer)
