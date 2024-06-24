# - 처음에는 set 연산으로 접근 했다가 메모리의 벽에 막혔다. 4MB의 만을 사용하려면 다른 방법을 사용하여야 했고 질문게시판을 보다가 비트마스크(BitMask)라는 방법을 사용해야 한다는 것을 알고 공부하였다.
# - 비트마스크 관련된 내용은 아래 링크에 있다. 관련 내용을 제외하고는 집합의 구현과 같다.
# - 풀이시간 : 30분
# 부족한 부분
# https://velog.io/@ouk/%EB%B9%84%ED%8A%B8%EB%A7%88%EC%8A%A4%ED%8A%B8BitMask-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98

import sys
input=sys.stdin.readline

s=0

n=int(input())
for i in range(n):
    arr=list(map(str,input().split()))
    if arr[0]=='add':
        s|=(1<<int(arr[1]))
    elif arr[0]=='remove':
        if s&(1<<int(arr[1])):
            s&=~(1<<int(arr[1]))
    elif arr[0]=='check':
        if s&(1<<int(arr[1])):
            print(1)
        else:
            print(0)
    elif arr[0]=='toggle':
        s^=(1<<int(arr[1]))
    elif arr[0]=='all':
        s=(1<<21)-1
    elif arr[0]=='empty':
        s=0