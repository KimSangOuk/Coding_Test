def create_pi_table(pattern):
    table = [0] * len(pattern)
    i = 0
    for j in range(1, len(pattern)):
        while i > 0 and pattern[i] != pattern[j]:
            i = table[i-1]
        if pattern[i] == pattern[j]:
            i += 1
            table[j] = i
    return table

while True:
    s = input().strip()
    if s == '.':
        break
    table = create_pi_table(s)
    n = len(s)
    # 주기 계산
    period = n - table[n - 1]
    if n % period == 0:
        print(n // period)
    else:
        print(1)
