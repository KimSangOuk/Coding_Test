from collections import deque

for tc in range(1,int(input())+1):
    n=4
    oper_cnt=int(input())
    gears=[deque(list(map(str,input().split()))) for _ in range(n)]
    opers=[tuple(map(int,input().split())) for _ in range(oper_cnt)]

    for oper in opers:
        num,dir=oper
        move=[0]*n
        move[num-1]=dir
        left=num-1
        while left>0 and gears[left][6]!=gears[left-1][2]:
            left-=1
            move[left]=-move[left+1]
        right=num-1
        while right<n-1 and gears[right][2]!=gears[right+1][6]:
            right+=1
            move[right]=-move[right-1]
        for i in range(n):
            if move[i]==-1:
                gears[i].append(gears[i].popleft())
            elif move[i]==1:
                gears[i].appendleft(gears[i].pop())

    score=0
    for i in range(n):
        if gears[i][0]=='1':
            score+=2**i
    print("#"+str(tc)+" "+str(score))