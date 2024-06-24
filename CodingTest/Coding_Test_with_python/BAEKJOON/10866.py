# - 파이썬의 경우, 덱큐를 가지고 활용할 수 있냐를 보는 문제. 덱의 각 함수를 알고만 있으면 쉽게 풀 수 있다.
# - 풀이시간 : 7분

from collections import deque
import sys

input=sys.stdin.readline

q=deque([])
n=int(input())
for i in range(n):
    arr=list(map(str,input().split()))
    if arr[0]=='push_back':
        q.append(arr[1])
    if arr[0]=='push_front':
        q.appendleft(arr[1])
    if arr[0]=='front':
        if len(q)==0:
            print(-1)
        else:
            print(q[0])
    if arr[0]=='back':
        if len(q)==0:
            print(-1)
        else:
            print(q[-1])
    if arr[0]=='size':
        print(len(q))
    if arr[0]=='empty':
        if len(q)==0:
            print(1)
        else:
            print(0)
    if arr[0]=='pop_front':
        if len(q)==0:
            print(-1)
        else:
            print(q.popleft())
    if arr[0]=='pop_back':
        if len(q)==0:
            print(-1)
        else:
            print(q.pop())