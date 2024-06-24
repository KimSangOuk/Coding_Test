# 풀이시간 10분 시간제한 0.5초 메모리제한 256MB
# 1회차 정답
# 스택을 구현해서 실행명령대로 출력하는 문제이다. 이때, 덱을 이용해서 스택을 풀었는데 시간초과가 나오길래 len()을 int로 바꾸어주었으나 시간복잡도가 똑같이 O(1)이라는 점을 알았고 입력을 sys.stdin.readline으로 바꾸어주었더니 풀렸다.

from collections import deque
import sys

input=sys.stdin.readline

n=int(input())
q=deque([])
q_len=0

for _ in range(n):
    oper=list(map(str,input().split()))
    if oper[0]=='push' and len(oper)>1:
        q.append(int(oper[1]))
        q_len+=1
    elif oper[0]=='top':
        print(-1 if q_len==0 else q[-1])
    elif oper[0]=='size':
        print(q_len)
    elif oper[0]=='empty':
        print(1 if q_len==0 else 0)
    elif oper[0]=='pop':
        print(-1 if q_len==0 else q.pop())
        if q_len>0:
            q_len-=1