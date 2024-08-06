from collections import deque

t=int(input())

gears=[]
for i in range(t):
    gears.append(deque(list(input())))

k=int(input())
# print(gears)
commands=[]
for _ in range(k):
    num,dir=map(int,input().split())

    states=deque([dir])
    left=num-1
    right=num-1
    while left>0:
        if states[0]!=0 and gears[left][6]!=gears[left-1][2]:
            states.appendleft(-states[0])
        else:
            states.appendleft(0)
        left-=1
    while right<t-1:
        if states[-1]!=0 and gears[right][2]!=gears[right+1][6]:
            states.append(-states[-1])
        else:
            states.append(0)
        right+=1
    for i in range(t):
        if states[i]==-1:
            gears[i].append(gears[i].popleft())
        elif states[i]==1:
            gears[i].appendleft(gears[i].pop())
    # print(gears)

cnt=0
for gear in gears:
    if gear[0]=='1':
        cnt+=1
print(cnt)
