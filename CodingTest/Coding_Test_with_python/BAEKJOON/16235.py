# 풀이시간 30분 시간제한 0.3초 메모리제한 512MB
# 2회차 정답
# 이하 생략

from collections import deque

dx=[-1,-1,0,1,1,1,0,-1]
dy=[0,-1,-1,-1,0,1,1,1]

n,m,k=map(int,input().split())

trees=[[deque() for _ in range(n)] for _ in range(n)]
food=[[5]*n for _ in range(n)]

A=[]
for _ in range(n):
    A.append(list(map(int,input().split())))

for _ in range(m):
    x,y,z=map(int,input().split())
    trees[x-1][y-1].append(z)

while k>0:
    for i in range(n):
        for j in range(n):
            tree_list=list(trees[i][j])
            plus_food_in_fall=0
            index=-1
            for t in range(len(tree_list)):
                if food[i][j]>=tree_list[t]:
                    food[i][j]-=tree_list[t]
                    tree_list[t]+=1
                    index=t
                else:
                    plus_food_in_fall+=tree_list[t]//2
            trees[i][j]=deque(tree_list[:index+1])
            food[i][j]+=(plus_food_in_fall+A[i][j])

    for i in range(n):
        for j in range(n):
            tree_list=trees[i][j]
            for tree in tree_list:
                if tree%5==0:
                    x,y=i,j
                    for d in range(8):
                        nx=x+dx[d]
                        ny=y+dy[d]
                        if nx<0 or ny<0 or nx>=n or ny>=n:
                            continue
                        trees[nx][ny].appendleft(1)

    k-=1

cnt=0
for i in range(n):
    for j in range(n):
        cnt+=len(trees[i][j])

print(cnt)

# 풀이시간 1시간 45분/60분 시간제한 0.3초 메모리제한 512MB
# 1회차 정답 - but, 풀이시간 초과 및 시간초과를 해결하지 못함
# 주어진대로 구현하는 시뮬레이션 유형이나 주어진 시간이 적기 때문에 최대한 압축해서 풀어야 했다. 각 계절별로 나무의 성장 및 양분 관리를 하는 문제인데 시간초과가 걸렸다.
# 계절별로, 즉 단계별로 나누어진 과정을 하나의 과정에 합치자 시간초과가 사라졌다. 여러개의 과정을 각자 구현해보고 그 것들을 합칠 수 있는지 고려해보는 태도가 필요하다. 즉, 나같은 경우는 단계별로 풀고 나서 마치는 경향이 있는데 이 단계들을 하나의 반복문 흐름에 넣을 수 있는지 생각해보는 것이 좋다.

from collections import deque

dx=[0,0,-1,1,-1,-1,1,1]
dy=[-1,1,0,0,-1,1,-1,1]

n,m,k=map(int,input().split())

trees=[[deque([]) for i in range(n)] for _ in range(n)]

food=[[0]*n for _ in range(n)]

a=[]
for i in range(n):
    a.append(list(map(int,input().split())))
    for j in range(n):
        food[i][j]=5

for _ in range(m):
    x,y,age=map(int,input().split())
    trees[x-1][y-1].append(age)

while k>0:
    k-=1
    # 봄
    # 나무가 자신의 나이만큼 양분
    breeding=[]
    for i in range(n):
        for j in range(n):
            # 그 칸에 나무가 있으면
            if len(trees[i][j])!=0:
                tree_list=trees[i][j]
                dead=0
                life_index=-1 # 죽은 나무 인덱스
                tmp=deque()
                # 가장 어린 나무부터
                for t in range(len(tree_list)):
                    # 땅의 양분이 자신의 나이만큼 있으면 양분 먹고 나이 1 증가
                    if tree_list[t]<=food[i][j]:
                        food[i][j]-=tree_list[t]
                        tree_list[t]+=1
                        # 번식하는 나무들 찾아놓기
                        if tree_list[t]%5==0:
                            breeding.append((i,j))
                        tmp.append(tree_list[t])
                    # 땅의 자신의 나이만큼 없으면 그 뒤에 양분 다 부족한 걸로 취급해서 즉사
                    else:
                        dead+=tree_list[t]//2
                trees[i][j]=tmp
                # 여름 - 죽은 나무들이 양분으로
                food[i][j]+=dead
            # 겨울에 양분 주기
            food[i][j]+=a[i][j]

    # 가을에 나무 번식 - 5의 배수가 되는 나무들, 인접한 8칸에 번식
    for x,y in breeding:
        for d in range(8):
            nx=x+dx[d]
            ny=y+dy[d]
            if nx<0 or ny<0 or nx>=n or ny>=n:
                continue
            trees[nx][ny].appendleft(1)

# 최종적으로 살아있는 나무의 개수
count=0
for i in range(n):
    for j in range(n):
        count+=len(trees[i][j])

print(count)