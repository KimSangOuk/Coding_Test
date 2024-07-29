from collections import deque

exp=list(input())

ans=[]
stack=deque()
for c in exp:
    if c.isalpha():
        ans.append(c)
    elif c=='(':
        stack.append(c)
    elif c==')':
        while stack and stack[-1]!='(':
            ans.append(stack.pop())
        stack.pop()
    elif c=='+' or c=='-':
        while stack and stack[-1]!='(':
            ans.append(stack.pop())
        stack.append(c)
    elif c=='*' or c=='/':
        while stack and stack[-1]!='(' and stack[-1]!='+' and stack[-1]!='-':
            ans.append(stack.pop())
        stack.append(c)
while stack:
    ans.append(stack.pop())
answer=""
for a in ans:
    answer+=a
print(answer)