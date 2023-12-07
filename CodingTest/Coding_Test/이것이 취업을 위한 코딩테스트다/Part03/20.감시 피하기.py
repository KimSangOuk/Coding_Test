# 풀이시간 60분/60분 시간제한 2초 메모리제한 256MB
# 1회차 정답 - 하지만 코드를 짜면서 더 단축시키고 배울 부분이 있다고 생각해서 한번 더 풀어볼 것
# 내 코드가 더 짧고 효율적이긴 함. 하지만 다른 부분에서 효율적으로 작성할 수 있었음.
# 얼마나 정답을 낼 경우, 출력의 형식을 유의해야되는지 깨닫게 한 문제. 2시간을 날렸다.
# 남은 칸 중에서 3개의 칸을 조합으로 고른 후, 그 벽을 설치했을 때, 선생님에 따라서 좌,우,상,하로 탐색해보면 되는 문제이다. 조합의 횟수 정도가 10,000이하 이므로 조합을 이용해도 괜찮다.


# 1회차 풀이
from itertools import combinations

n=int(input())

graph=[]
for _ in range(n):
  graph.append(list(map(str,input().split())))

# 탐색을 할 때, 맵에 기록하는 등의 많은 기록을 하지 않는다면 굳이 예비 맵을 만들어서 메모리를 낭비하지 않고 넣었다 뺏다로 할 수 있음.
temp=[['']*n for _ in range(n)]

empty_space=[]

for i in range(n):
  for j in range(n):
    if graph[i][j]=='X':
      empty_space.append((i,j))

case_list=list(combinations(empty_space,3))

answer='Yes'

# 여기는 개인적으로 잘했다고 생각함.
def watch(y,x,d):
  global answer
  if y<0 or y>=n or x<0 or x>=n or temp[y][x]=='O':
    return
  if temp[y][x]=='S':
    answer='No'
  else:
    if d==0:
      watch(y,x+1,0)
    if d==1:
      watch(y,x-1,1)
    if d==2:
      watch(y+1,x,2)
    if d==3:
      watch(y-1,x,3)

def main():
  global answer
  # case를 굳이 이렇게 나눌 필요 없이 콤비네이션에서 바로 받아서 쓸 수도 있다는 것을 깨달음. 코드를 더 단순화 시킬 수 있음.
  for case in case_list:
    for i in range(n):
      for j in range(n):
        # 여기서도 벽을 +, -하는게 더 효율적으로 보인다. 탐색을 할 때, 맵을 건들지 않기 때문
        if (i,j) in case: 
          temp[i][j]='O'
        else:
          temp[i][j]=graph[i][j]
    answer='Yes'
    # 여기서도 선생님의 수랑 위치는 고정되어 있어서 변하지 않기 때문에 케이스마다 찾을 필요가 있을 때에는 전체에서 한번 확인해서 사용하는게 더 좋아보임.
    for i in range(n):
      for j in range(n):
        if temp[i][j]=='T':
          for d in range(4):
            watch(i,j,d)
    
    if answer!='No':
      return 'Yes'

answer=main()
if answer=='Yes':
  print("YES")
else:
  print("NO")

# 답안 예시
from itertools import combinations

n=int(input())
board=[]
teachers=[] # 모든 선생님 위치 정보
spaces=[] # 모든 빈 공간 위치 정보

for i in range(n):
  board.append(list(input().split()))
  for j in range(n):
    # 선생님이 존재하는 위치 저장
    if board[i][j]=='T':
      teachers.append((i,j))
    # 장애물을 설치할 수 있는 (빈 공간) 위치 저장
    if board[i][j]=='X':
      spaces.append((i,j))

# 특정 방향으로 감시를 진행(학생 발견: True, 학생 미발견: False)
def watch(x,y,direction):
  # 왼쪽 방향으로 감시
  if direction==0:
    while y>=0:
      if board[x][y]=='S': # 학생이 있는 경우
        return True
      if board[x][y]=='O': # 장애물이 있는 경우
        return False
      y-=1
  # 오른쪽 방향으로 감시
  if direction==1:
    while y<n:
      if board[x][y]=='S': # 학생이 있는 경우
        return True
      if board[x][y]=='O': # 장애물이 있는 경우
        return False
      y+=1
  if direction==2:
    while x>=0:
      if board[x][y]=='S': # 학생이 있는 경우
        return True
      if board[x][y]=='O': # 장애물이 있는 경우
        return False
      x-=1
  if direction==3:
    while x<n:
      if board[x][y]=='S': # 학생이 있는 경우
        return True
      if board[x][y]=='O': # 장애물이 있는 경우
        return False
      x+=1
  return False

# 장애물 설치 이후에, 한 명이라도 학생이 감지되는지 검사
def process():
  # 모든 선생님의 위치를 하나씩 확인
  for x,y in teachers:
    # 4가지 방향으로 학생을 감지할 수 있는지 확인
    for i in range(4):
      if watch(x,y,i):
        return True
  return False

find = False # 학생이 한 명도 감지되지 않도록 설치할 수 있는지의 여부

# 빈 공간에서 3개를 뽑는 모든 조합을 확인
for data in combinations(spaces,3):
  # 장애물 설치해보기
  for x,y in data:
    board[x][y]='0'
  # 학생이 한 명도 감지되지 않는 경우
  if not process():
    # 원하는 경우를 발견한 것임
    find = True
    break
  # 설치된 장애물을 다시 없애기
  for x,y in data:
    board[x][y]='X'

if find:
  print('YES')
else:
  print('NO')