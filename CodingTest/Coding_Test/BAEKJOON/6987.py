```python
def check_possible(results, matches, idx):
    if idx == 15:
        for team_result in results:
            if team_result != [0, 0, 0]:
                return False
        return True

    t1, t2 = matches[idx]

    # t1 승리, t2 패배
    if results[t1][0] > 0 and results[t2][2] > 0:
        results[t1][0] -= 1
        results[t2][2] -= 1
        if check_possible(results, matches, idx + 1):
            return True
        results[t1][0] += 1
        results[t2][2] += 1

    # t1 무승부, t2 무승부
    if results[t1][1] > 0 and results[t2][1] > 0:
        results[t1][1] -= 1
        results[t2][1] -= 1
        if check_possible(results, matches, idx + 1):
            return True
        results[t1][1] += 1
        results[t2][1] += 1

    # t1 패배, t2 승리
    if results[t1][2] > 0 and results[t2][0] > 0:
        results[t1][2] -= 1
        results[t2][0] -= 1
        if check_possible(results, matches, idx + 1):
            return True
        results[t1][2] += 1
        results[t2][0] += 1

    return False

def solve():
    teams = 6
    matches = [(i, j) for i in range(teams) for j in range(i + 1, teams)]

    results = []
    for _ in range(4):
        input_data = list(map(int, input().split()))
        results.append([input_data[i:i+3] for i in range(0, 18, 3)])

    for result in results:
        if check_possible(result, matches, 0):
            print(1, end=" ")
        else:
            print(0, end=" ")

if __name__ == "__main__":
    solve()