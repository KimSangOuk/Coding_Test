# 풀이시간 40분 시간제한 1초 메모리제한 512MB
# 1회차 정답
# 아무리 연산 횟수가 많아져도 드래곤 커브 횟수에 보드의 크기인 10,000이기 때문에 200,000회로 충분히 가능하다. 주어진 상황을 그대로 코드로 구현해 나가는 시뮬레이션 유형이다.

board=[[0]*101 for _ in range(101)]

n=int(input())

dx=[1,0,-1,0]
dy=[0,-1,0,1]

def curv(dir):
  return (dir+1)%4

def make_dragoncurv_dir(dir,gen):
  answer=[]
  answer.append(dir)
  for i in range(gen):
    for j in range(len(answer)-1,-1,-1):
      answer.append(curv(answer[j]))
  return answer

def make_dragoncurv(x,y,dirs):
  answer=[]
  answer.append((x,y))
  for i in dirs:
    nx=x+dx[i]
    ny=y+dy[i]
    answer.append((nx,ny))
    x,y=nx,ny
  return answer

def check_rect_cnt(board):
  count=0
  for i in range(100):
    for j in range(100):
      if board[i][j]==1 and board[i+1][j]==1 and board[i][j+1]==1 and board[i+1][j+1]==1:
        count+=1
  return count

dragoncurv=[]
for _ in range(n):
  x,y,d,g=map(int,input().split())
  directions=make_dragoncurv_dir(d,g)
  # print(directions)
  dragoncurv=make_dragoncurv(x,y,directions)

  for x,y in dragoncurv:
    board[x][y]=1

  # print(dragoncurv)

answer=check_rect_cnt(board)
print(answer)