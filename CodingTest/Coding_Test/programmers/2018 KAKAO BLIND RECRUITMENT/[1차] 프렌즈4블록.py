# - 블록을 지우고 지워진 블록의 위에 있던 블록들이 내려오는 함수를 나누어서 구현하였다. 그리고 해당 블록이 지워지는 함수에서 지워지는 갯수를 return 하게 하여서 값이 0이면 반복문을 종료하였다.
# - clear() 함수에서는 동시에 지워질 수 있기에 지워지는 블록들을 전부 찾은 후에, 지워지는 것을 후에 처리하였다.
# - reset_board() 함수에서는 세로줄에서의 빈칸이 아닌 값을 모은 다음 빈칸의 수만큼 앞에 추가해서 다시 보드에 세팅해 주었다.
# - 풀이시간 : 25분

def clear(m,n,board):
  clear_block=set()
  for i in range(m-1):
      for j in range(n-1):
          if board[i][j]==board[i+1][j+1] and board[i][j]==board[i+1][j] and board[i][j]==board[i][j+1] and board[i][j]!=' ':
              clear_block.add((i,j))
              clear_block.add((i+1,j))
              clear_block.add((i,j+1))
              clear_block.add((i+1,j+1))
  clear_block=list(clear_block)
  for i in range(len(clear_block)):
      board[clear_block[i][0]][clear_block[i][1]]=' '

  return len(clear_block)

def reset_board(m,n,board):
  for j in range(n):
      arr=[]
      for i in range(m):
          if board[i][j]!=' ':
              arr.append(board[i][j])
      arr=[' ']*(m-len(arr))+arr
      for i in range(m):
          board[i][j]=arr[i]
def solution(m, n, board):
  answer = 0

  new_board=[]
  for i in range(len(board)):
      new_board.append(list(board[i]))

  while True:
      k=clear(m,n,new_board)
      if k==0:
          break
      answer+=k
      reset_board(m,n,new_board)
  return answer