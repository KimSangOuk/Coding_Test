# 풀이시간 초과/50분 시간제한 1초 메모리제한 128MB
# 1회차 오답 - 풀이시간 초과 + 풀이에 접근 못함
# 이 문제에서 BFS를 보았다는 사실에 시야가 많이 늘었다는 점은 알겠으나, 방향과 좌표를 다룰 때, 많이 부족한 점을 보였다.
# 풀이 방식은 BFS로 풀다가 움직일 수 있는 모든 케이스를 두고 똑같이 푸는 방식이다. 또한 시간을 큐에 같이 포함시켜서 진행 시간을 저장하는 것까지도 풀었다.
# 사실상 메인은 전부 맞게 생각하고 풀었으나, 좌표와 이동 가능성을 따지는 것에서 문제가 있었다.
# 가장 핵심은 set를 이용하지 못했다는 점이다. 위치를 표현하고 저장 할때, 순서 상관 관계를 없애야 하는데 방법이 없고 해본적이 없으니 튜플로 접근하니 경우의 수가 몇배로 늘어났다.
# 그리고 추가 적으로 복잡한 조건관계가 많을 때는, 다른 조건관계를 편하게 만들어주기 위해서 테두리를 맵에 추가한다는 점을 한번 더 상기시키는 문제가 되었다. 테두리를 다른 배열의 끝으로 따지면 다른 조건이 되기 때문에 훨씬 복잡해지기 때문이다.
# 테두리를 추가하는 방식은 알고 있었으나 이것도 사용경험의 부족이기도 하고 DFS/BFS 알고리즘을 다루면서 처음이다보니 내 지식에서 꺼내서 사용하기 힘들었다고 본다.

# 좌표나 모양, 회전을 다룰 때는, 케이스를 나누어서 자세히 그려보는게 좋은 것 같다. 이미지가 머리 속에 그려지니까 훨씬 접근하기 쉬워진다. 그리고 기준 단위별로 끊어서 행동을 생각하는게 좋아보인다.
# 그리고 기존 좌표에 너무 얽매여서 +, - 로만 움직이려고 하는 습관을 고쳐야된다.
# 좌표로 가로와 세로를 표현하는 방법도 익숙하지 않았다.

# 2회차 풀이



# 1회차 풀이
from collections import deque

def solution(board):
  answer = 0
  n=len(board)

  # 좌표를 +, -해서 이동시키는데 너무 집착하는 모습이 보인다.
  dx=[0,0,-1,1]
  dy=[-1,1,0,0]
  dsx=[-1,1,0,0]
  dsy=[1,1,0,0]
  d

  # 순서가 상관없는 경우, set를 이용하는 편이 더 편리하고 이 경우에는 거의 필수이다.
  visited_coordinate=[((0,0),(0,1),0)]
  q=deque([((0,0),(0,1),0,0)])
  while q:
    start,end,state,now=q.popleft()
    # 가로와 세로를 좌표로 표현하는데 익숙하지 않아서 변수가 더 길어지는 모습이 보인다.
    # 그림을 그리거나 자세히 나타내지 않아서 조건이 어떻게 나누어지고 어떻게 진행되는지 모습을 실패한 대표 적인 케이스이다.
    # 문제에서 주어진 단위 별로 상황을 나누어서 표현하고 그 표현을 어떻게 코드화 할지를 생각해야 한다.
    if state==0:
      print("가로")
      for i in range(4):
        nx_start=start[0]+dx[i]
        ny_start=start[1]+dy[i]
        nx_end=end[0]+dx[i]
        ny_end=end[0]+dy[i]
        # 테두리를 조건을 줄이기 위해 조건화 하지 못했다. 이러한 점은 이중 배열이나 맵에서 언제든지 확장하여 사용할 수 있다는 점을 생각해두자.
        if 0<=nx_start<n and 0<=ny_start<n and 0<=nx_end<n and 0<=ny_end<n:
          if board[nx_start][ny_start]==0 and board[nx_end][ny_end]==0:
            if ((nx_start,ny_start),(nx_end,ny_end),0) not in visited_coordinate or ((nx_end,ny_end),(nx_start,ny_start),0) not in visited_coordinate:
              q.append(((nx_start,ny_start),(nx_end,ny_end),0,now+1))
              visited_coordinate.append(((nx_start,ny_start),(nx_end,ny_end),0))
      for i in range(4):
        nx_start=start[0]+drx[i]
        ny_start=start[1]+dry[i]
        nx_end=end[0]+drx[i]
        ny_end=end[0]+dry[i]
      # 가능한 좌표 가짓 수 - 회전하면서 벽에 안 부딪치고
      # 로봇이 영역을 벗어나지 않고 and 벽에 안 닿고 and 처음 가보는 좌표이고
      # 위에 조건을 충족시키면 그 좌표를 큐에 넣고 가본 좌표에 기록하고, 카운트+=1
      # 만약 위의 조건을 만족시키는 좌표가 끝에 도달했다면 break
    elif state==1:
      print("세로")
      for i in range(4):
        nx_start=start[0]+dx[i]
        ny_start=start[1]+dy[i]
        nx_end=end[0]+dx[i]
        ny_end=end[0]+dy[i]
        if 0<=nx_start<n and 0<=ny_start<n and 0<=nx_end<n and 0<=ny_end<n:
          if board[nx_start][ny_start]==0 and board[nx_end][ny_end]==0:
            if ((nx_start,ny_start),(nx_end,ny_end),1) not in visited_coordinate or ((nx_end,ny_end),(nx_start,ny_start),1) not in visited_coordinate:
              q.append(((nx_start,ny_start),(nx_end,ny_end),1,now+1))
              visited_coordinate.append(((nx_start,ny_start),(nx_end,ny_end),1))
      # 가능한 좌표 가짓 수 - 벽에 부딪치지 않게

  answer=count
  return answer

# 답안 예시
from collections import deque

def get_next_pos(pos,board):

  pos=list(pos) # 현재 위치 정보를 리스트로 변환(집합 -> 리스트)
  pos1_x,pos1_y,pos2_x,pos2_y=pos[0][0],pos[0][1],pos[1][0],pos[1][1]

  next_pos=[] # 반환 결과(이동 가능한 위치들)

  # (상, 하, 좌, 우)로 이동하는 경우에 대해서 처리
  dx=[0,0,-1,1]
  dy=[-1,1,0,0]
  
  for i in range(4):
    nx_pos1_x,ny_pos1_y,nx_pos2_x,ny_pos2_y=pos1_x+dx[i],pos1_y+dy[i],pos2_x+dx[i],pos2_y+dy[i]
    # 이동하고자 하는 두 칸이 모두 비어 있다면
    if board[nx_pos1_x][ny_pos1_y]==0 and board[nx_pos2_x][ny_pos2_y]==0:
      next_pos.append({(nx_pos1_x,ny_pos1_y),(nx_pos2_x,ny_pos2_y)})
  # 현재 로봇이 가로로 놓여 있는 경우
  if pos1_x==pos2_x:
    for i in [-1,1]: # 위쪽으로 회전가거나, 아래쪽으로 회전
      if board[pos1_x+i][pos1_y]==0 and board[pos2_x+i][pos2_y]==0: # 위쪽 혹은 아래쪽 두 칸이 모두 비어 있다면
        next_pos.append({(pos1_x,pos1_y),(pos1_x+i,pos1_y)})
        next_pos.append({(pos2_x,pos2_y),(pos2_x+i,pos2_y)})
  elif pos1_y==pos2_y:
    for i in [-1,1]: # 왼쪽으로 회전하거나, 오른쪽으로 회전
      if board[pos1_x][pos1_y+i]==0 and board[pos2_x][pos2_y+i]==0: # 왼쪽 혹은 오른쪽 두 칸이 모두 비어 있다면
        next_pos.append({(pos1_x,pos1_y),(pos1_x,pos1_y+i)})
        next_pos.append({(pos2_x,pos2_y),(pos2_x,pos2_y+i)})
  # 현재 위치에서 이동할 수 있는 위치를 반환
  return next_pos

def solution(board):
  # 맵의 외곽에 벽을 두는 형태로 맵 변경
  n=len(board)
  answer=0

  new_board=[[0]*(n+2) for _ in range(n+2)]
  for i in range(n):
    for j in range(n):
      new_board[i+1][j+1]=board[i][j]

  # 너비 우선 탐색(BFS) 수행
  pos={(1,1),(1,2)} # 시작 위치 설정
  visited_coordinate=[] 
  visited_coordinate.append(pos) # 방문 처리
  q=deque()
  s=0
  q.append((pos,s)) # 큐에 삽입한 뒤에
  # 큐가 빌 때까지 반복
  while q:
    pos,s=q.popleft()
    # (n, n) 위치에 로봇이 도달했다면, 최단 거리이므로 반환
    if (n,n) in pos:
      return s
    # 현재 위치에서 이동할 수 있는 위치 확인
    for next_pos in get_next_pos(pos,new_board):
      # 아직 방문하지 않은 위치라면 큐에 삽입하고 방문 처리
      if next_pos not in visited_coordinate:
        visited_coordinate.append(next_pos)
        q.append((next_pos,s+1))
  return 0