# 풀이시간 40분 시간제한 1초 메모리제한 1024MB
# 1회차 정답
# 먼저 우리는 학생들의 자리를 배치하기 위해 각 학생들의 선호 학생을 받으면서 이를 진행할 수 있다. 이 때, 현재 앉은 학생은 뒤에 순서의 학생이 좋아하는 학생을 고려할 필요는 없기 때문에 입력받는 대로 진행해도 된다. 나중에 점수계산을 위해 선호 학생을 학생의 번호대로 저장해두고, 각 학생이 앉을 자리를 완전탐색한다. 모든 빈자리를 보면서 우리는 좋아하는 학생의 수, 빈칸의 수, 각 행과 열의 위치를 고려해야하므로 빈칸마다 4개의 변수를 저장해둔다. 그러고 난 후 한꺼번에 우리가 원하는 순서대로 정렬하면 가장 앞에 있는 자리가 우리가 원하는 자리가 되므로 그 자리에 학생을 앉히면 된다.
# 그러고 난 후 모든 자리를 탐색하며 각 학생마다 주위에 좋아하는 학생이 몇명인지를 세어가며 점수를 합산하면 된다. 즉, 시뮬레이션 문제이자 브루트포스 유형이라고도 할 수 있겠다.

n=int(input())

dx=[0,0,1,-1]
dy=[1,-1,0,0]

board=[[0]*(n+1) for i in range(n+1)]
like_friend=[set() for _ in range(n*n+1)]
for i in range(n*n):
    t,a,b,c,d=map(int,input().split())
    arr=set([a,b,c,d])
    empty_list=[]
    for j in range(1,n+1):
        for k in range(1,n+1):
            if board[j][k]==0:
                like_count=0
                empty_count=0
                for d in range(4):
                    nx=j+dx[d]
                    ny=k+dy[d]
                    if nx<1 or ny<1 or nx>n or ny>n:
                        continue
                    if board[nx][ny]==0:
                        empty_count+=1
                    if board[nx][ny] in arr:
                        like_count+=1
                empty_list.append((like_count,empty_count,j,k))
    empty_list.sort(key=lambda x:(-x[0],-x[1],x[2],x[3]))
    board[empty_list[0][2]][empty_list[0][3]]=t
    like_friend[t]=arr

result=0
for i in range(1,n+1):
    for j in range(1,n+1):
        my=board[i][j]
        count=0
        for t in range(4):
            nx=i+dx[t]
            ny=j+dy[t]
            if nx<1 or ny<1 or nx>n or ny>n:
                continue
            if board[nx][ny] in like_friend[my]:
                count+=1
        if count==1:
            result+=1
        elif count==2:
            result+=10
        elif count==3:
            result+=100
        elif count==4:
            result+=1000

print(result)