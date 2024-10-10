INF = int(1e9)
 
for tc in range(1, int(input()) + 1):
    inputArr = list(map(int, input().split()))
    n = inputArr[0]  # 사람 수
    graph = [[INF] * n for _ in range(n)]
 
    # 인접 행렬 초기화
    idx = 1
    for i in range(n):
        for j in range(n):
            if inputArr[idx] == 1:
                graph[i][j] = 1  # 연결된 경우 거리 1
            if i == j:
                graph[i][j] = 0  # 자기 자신은 거리 0
            idx += 1
 
    # 플로이드-워셜 알고리즘 적용
    for k in range(n):
        for i in range(n):
            for j in range(n):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
 
    # 각 사람의 최소 거리 합을 구하고, 그 중 가장 작은 값 찾기
    answer = INF
    for i in range(n):
        sumValue = sum(graph[i][j] for j in range(n) if graph[i][j] != INF)
        answer = min(answer, sumValue)
 
    # 결과 출력
    print(f"#{tc} {answer}")
