# 풀이시간 1시간/1시간 시간제한 1초 메모리제한 512MB
# 1회차 정답
# cctv별로 각 가능한 경우를 나누어 중복 순열을 한다음, 즉 1번 cctv가 2개라면 총 16가지 경우가 나올 수 있다.
# 그 다음 cctv의 가능한 경우를 중복 순열로 한 번 더 합쳐서, 각 cctv가 할당되는 경우, 한 케이스를 구해낼 수 있다.
# 그렇게 된다면 이 경우에서 감시하는 걸 찾은 다음 답을 찾아내면 되는 시뮬레이션 문제이다.
# 중복순열은 처음 사용해보면서 사용법을 깨달았다.

from itertools import product

n,m=map(int,input().split())

board=[]
cctv_number=[0]*6
cctvs=[[] for _ in range(6)]
for i in range(n):
  arr=list(map(int,input().split()))
  for j in range(m):
    if 1<=arr[j]<=5:
      cctvs[arr[j]].append((i,j))
      cctv_number[arr[j]]+=1
  board.append(arr)

case=[0,4,2,4,4,1]
cases_cctv=[[] for _ in range(6)]
for i in range(1,6):
  if cctv_number[i]<0:
    continue
  cases_cctv[i]=list(product(range(case[i]),repeat=cctv_number[i]))
  # print(cases_cctv[i])

cases=list(product(cases_cctv[1],cases_cctv[2],cases_cctv[3],cases_cctv[4],cases_cctv[5]))

tmp=[[0]*m for _ in range(n)]
for i in range(n):
  for j in range(m):
    tmp[i][j]=board[i][j]

dx=[0,0,-1,1]
dy=[1,-1,0,0]

def see(board,cctv_xy,dir):
  x,y=cctv_xy
  while True:
    nx=x+dx[dir]
    ny=y+dy[dir]
    if ny<0 or ny>=m or nx<0 or nx>=n or board[nx][ny]==6:
      break
    board[nx][ny]=7
    x,y=nx,ny

def see_cctv(board,cctv_num,cctv_xy,dir):
  x,y=cctv_xy
  if cctv_num==1:
    see(board,cctv_xy,dir)
  elif cctv_num==2:
    if dir==0:
      see(board,cctv_xy,0)
      see(board,cctv_xy,1)
    elif dir==1:
      see(board,cctv_xy,2)
      see(board,cctv_xy,3)
  elif cctv_num==3:
    if dir==0:
      see(board,cctv_xy,0)
      see(board,cctv_xy,2)
    elif dir==1:
      see(board,cctv_xy,0)
      see(board,cctv_xy,3)
    elif dir==2:
      see(board,cctv_xy,1)
      see(board,cctv_xy,2)
    elif dir==3:
      see(board,cctv_xy,1)
      see(board,cctv_xy,3)
  elif cctv_num==4:
    for i in range(4):
      if dir!=i:
        see(board,cctv_xy,i)
  elif cctv_num==5:
    for i in range(4):
      see(board,cctv_xy,i)
        
      
      

answer=int(1e9)
for case in cases:
  count=0
  for num in range(5):
    for how in range(len(case[num])):
      see_cctv(tmp,num+1,cctvs[num+1][how],case[num][how])

  # for i in range(n):
  #   print(tmp[i])
  # print()
  
  
  for i in range(n):
    for j in range(m):
      if tmp[i][j]==0:
        count+=1
      else:
        tmp[i][j]=board[i][j]
  # print(count)
  answer=min(answer,count)

print(answer)