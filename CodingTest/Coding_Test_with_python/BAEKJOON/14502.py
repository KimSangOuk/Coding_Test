# 이것이 취업을 위한 코딩테스트다 part03 '16. 연구소'와 동일

for i in range(n):
  for j in range(m):
    if board[i][j]==0:
      empty_scope.append((i,j))
    elif board[i][j]==2:
      virus_scope.append((i,j))
      board[i][j]=0

all_case=list(combinations(empty_scope,3))

def dfs(y,x):
  if x<=-1 or x>=m or y<=-1 or y>=n:
    return False
  if new_board[y][x]==0:
    new_board[y][x]=2
    dfs(y-1,x)
    dfs(y,x-1)
    dfs(y+1,x)
    dfs(y,x+1)
    return True
  return False

answer=0
for case in all_case:
  new_board=copy.deepcopy(board)
  scope1,scope2,scope3=case
  new_board[scope1[0]][scope1[1]]+=1
  new_board[scope2[0]][scope2[1]]+=1
  new_board[scope3[0]][scope3[1]]+=1

  for y,x in virus_scope:
    dfs(y,x)

  count=0
  for i in range(n):
    for j in range(m):
      if new_board[i][j]==0:
        count+=1

  answer=max(count,answer)

print(answer)