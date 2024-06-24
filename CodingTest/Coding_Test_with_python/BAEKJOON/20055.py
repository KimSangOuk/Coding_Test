# 풀이시간 1시간 시간제한 1초 메모리제한 512MB
# 1회차 정답
# 문제를 이해하는데 한참 걸린 문제이다. 단순히 시뮬레이션을 돌리면 된다.

from collections import deque

n,k=map(int,input().split())

a=deque(list(map(int,input().split())))
robot=deque([False]*n)

answer=0
while True:
    answer+=1
    # 1.벨트가 각 칸 위에 있는 로봇과 함께 한 칸 회전
    a.appendleft(a.pop())
    robot.pop()
    robot.appendleft(False)
    robot[n-1]=False

    # 2. 가장 먼저 벨트에 올라간 로봇부터, 벨트가 회전하는 방향으로 한 칸 이동할 수 있다면 이동한다. 만약 이동할 수 없다면 가만히 있는다.
    for i in range(n-2,-1,-1):
        if robot[i] and not robot[i+1] and a[i+1]>0:
            robot[i+1]=robot[i]
            robot[i]=False
            a[i+1]-=1
    robot[n-1]=False

    # 3. 올리는 위치에 있는 칸의 내구도가 0이 아니면 올리는 위치에 로봇을 올린다.
    if a[0]!=0:
        robot[0]=True
        a[0]-=1

    count=0
    for i in range(2*n):
        if a[i]==0:
            count+=1
    if count>=k:
        break


print(answer)