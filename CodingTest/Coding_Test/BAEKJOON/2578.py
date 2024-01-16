# 풀이시간 15분 시간제한 1초 메모리제한 128MB
# 1회차 정답
# 빙고판에서 하나씩 주어진 숫자들을 체크하며 그 체크한 판이 빙고를 몇개나 가지고 있는지 확인하면 되는 문제이다. 즉, 주어진 상황을 코드로 처리하는 시뮬레이션 문제이다.

board=[]
for i in range(5):
  board.append(list(map(int,input().split())))

call_num=[]
for i in range(5):
  call_num+=list(map(int,input().split()))

def check_bingo(board,num):
  for i in range(5):
    for j in range(5):
      if board[i][j]==num:
        board[i][j]=0

  total_count=0
  count_xy=0
  count_yx=0
  for i in range(5):
    count_x=0
    count_y=0
    for j in range(5):
      if board[i][j]==0:
        count_x+=1
      if board[j][i]==0:
        count_y+=1
      if i==j and board[i][j]==0:
        count_xy+=1
      if i==4-j and board[i][j]==0:
        count_yx+=1
    if count_x==5:
      total_count+=1
    if count_y==5:
      total_count+=1
  if count_xy==5:
    total_count+=1
  if count_yx==5:
    total_count+=1
  if total_count>=3:
    return True
  return False

for i in range(1,len(call_num)+1):
  if check_bingo(board,call_num[i-1]):
    print(i)
    break