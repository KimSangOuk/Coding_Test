import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

cur = ['A'] * n
ans = set()

def dq():
    q = deque([(0, n)])

    while q:
        for _ in range(len(q)):
            start, end = q.popleft()

            if end - start <= 1:
                continue
            mid = (start + end) // 2

            for i in range(start, mid):
                cur[i] = 'A'
            for i in range(mid, end):
                cur[i] = 'B'

            q.append((start, mid))
            q.append((mid, end))

        ans.add(''.join(cur))

dq()

for a in ans:
    print(a)

for _ in range(7 - len(ans)):
    print('A' + ('B' * (n - 1)))