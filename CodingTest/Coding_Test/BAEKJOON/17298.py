from collections import deque

n=int(input())
answer=[]
stackOrigin=list(map(int,input().split()))

stack=deque()

while stackOrigin:
    peek=stackOrigin.pop()
    if len(stack)==0:
        answer.append(-1)
        stack.append(peek)
        continue
    while stack and stack[-1]<=peek:
        stack.pop()
    if len(stack)==0:
        answer.append(-1)
    else:
        answer.append(stack[-1])
    stack.append(peek)

print(*answer[::-1])