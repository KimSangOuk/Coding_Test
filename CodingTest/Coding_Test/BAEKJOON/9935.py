from collections import deque

s = input()
bomb = input()
bomb_len = len(bomb)

stack = deque()

for k in s:
    stack.append(k)
    if len(stack) >= bomb_len:
        if ''.join([stack[-bomb_len + i] for i in range(bomb_len)]) == bomb:
            for _ in range(bomb_len):
                stack.pop()

# 결과 출력
if not stack:
    print("FRULA")
else:
    print(''.join(stack))
