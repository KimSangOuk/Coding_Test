def check_board(board,people):
  # print(board,people)
  numOfPeople=len(people)
  tf=True
  for i in range(0,numOfPeople-1):
      for j in range(i+1,numOfPeople):
          x1,y1=people[i]
          x2,y2=people[j]
          dist=abs(x1-x2)+abs(y1-y2)
          if dist>2:
              continue
          else:
              # 가로와 세로로 먼 경우
              if abs(x1-x2)==0 or abs(y1-y2)==0:
                  if abs(x1-x2)==0 and abs(y1-y2)<2:
                      return False
                  elif abs(x1-x2)==0 and abs(y1-y2)==2:
                      if board[x1][(y1+y2)//2]=='X':
                          continue
                      else:
                          return False
                  elif abs(y1-y2)==0 and abs(x1-x2)<2:
                      return False
                  elif abs(y1-y2)==0 and abs(x1-x2)==2:
                      if board[(x1+x2)//2][y1]=='X':
                          continue
                      else:
                          return False
              elif abs(x1-x2)==1 and abs(y1-y2)==1:
                  if board[x1][y2]=='X' and board[x2][y1]=='X':
                      continue
                  else:
                      return False
              else:
                  return False

  return tf

def solution(places):
  answer = []

  for tc in range(5):
      case=places[tc]
      board=[]
      people=[]
      for i in range(5):
          tmp=case[i]
          for j in range(5):
              if tmp[j]=='P':
                  people.append((i,j))
          board.append(list(tmp))
      if check_board(board,people):
          answer.append(1)
      else:
          answer.append(0)

  return answer