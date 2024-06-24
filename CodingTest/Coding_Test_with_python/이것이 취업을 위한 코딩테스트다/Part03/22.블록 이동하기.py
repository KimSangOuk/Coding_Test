# 3회차 풀이












# 풀이시간 초과/50분 시간제한 1초 메모리제한 128MB
# 2회차 오답
# 대강 풀이는 맞았으나 시간이 오래걸리기도 했고, 시간초과가 한문제 발생하였다.
# 시간 초과 원인의 추정 이유는 여러가지가 있다.
# 1) 좌표의 순서가 상관없기 때문에 다 처리하고 비교할 때 두 개의 좌표를 집합으로 묶는다면 비교할 때, 같은 집합으로 비교되기 때문에 문제가 되지 않는다. 또한 visited를 2차원 배열로 해서 처리하는 것보다는, 좌표의 두개씩 처리하고 이를 순서상관 없이 비교하기 때문에 집합들의 리스트로 만들면 비교 면에서 가능해진다.
# 2) 맵의 크기를 문제에서 주어진 좌표에 맞추기 위해서, 그리고 비교 연산을 줄이기 위해서 늘린 것도 이유가 될 수 있다고 생각한다.
# 왜 그렇다면 1번에서 순서를 신경쓰지 못했는가? 습관적으로 튜플로 묶는게 습관이 되어있기도 하고 순서가 상관이 없는 경우의 비교 연산등을 해본적이 없어서 생각조차 하지 못했다. 새로운 지식의 부족이며 순서를 염두해두지 않는 습관때문이라고 할 수 있다.
# 왜 맵의 크기를 조절하지 않았는가? 보드의 크기를 늘리고 줄이는 연산을 귀찮아 하기도 하고 그냥 풀려는 습관이 있기 때문이다. 만약 문제에서 좌표를 조절해준다고 힌트를 주거나 연산의 이동범위가 1이 넘지 않으면 벽을 세워주는게 좋아보인다.

from collections import deque

# 보드 자체를 늘려놨다면 불필요한 비교 연산을 줄여 코드가 더 간단해지고 시간도 줄어들 듯 싶다.
def solution(board):
  answer = 0

  n=len(board)

  dx=[0,0,-1,1]
  dy=[-1,1,0,0]

  # 단순 리스트로 집합으로 두개의 좌표를 묶어 넣어놓았다면 순서에 상관없이 비교가 되어 더 간단해씅ㄹ 것이다.
  visited=[[0]*n for _ in range(n)]

  q=deque([])
  # 좌표가 여러개이고 순서가 상관 없다면 집합으로 묶는게 좋아보인다. 비교를 할때에도 집합끼리 비교한다면 순서가 상관없이 비교되기 때문에 가능하다.
  q.append(((0,0),(0,1)))
  visited[0][0],visited[0][1]=1,1
  while True:
    q=deque(q)
    for _ in range(len(q)):
      pos1,pos2=q.popleft()
      # print(pos1,pos2)
      # 둘 중 한칸이 목적지에 도착하면 종료
      # 다음의 부분도 집합이었다면 in으로 비교 가능하다.
      if pos1==(n-1,n-1) or pos2==(n-1,n-1):
        return answer

      # 기본 이동(상, 하, 좌, 우)
      for i in range(4):
        nx_pos1,ny_pos1=pos1[0]+dx[i],pos1[1]+dy[i]
        nx_pos2,ny_pos2=pos2[0]+dx[i],pos2[1]+dy[i]
        if 0<=nx_pos1<n and 0<=ny_pos1<n and 0<=nx_pos2<n and 0<=ny_pos2<n:
          if board[nx_pos1][ny_pos1]==0 and board[nx_pos2][ny_pos2]==0:
            # if (nx_pos1,ny_pos1)==(2,0) and (nx_pos2,ny_pos2)==(3,0):
              # print("범인")
            if visited[nx_pos1][ny_pos1]==0 or visited[nx_pos2][ny_pos2]==0:
              q.append(((nx_pos1,ny_pos1),(nx_pos2,ny_pos2)))
              
      # 회전
      # 세로일 경우
      if pos1[1]==pos2[1]:
        # 여기서 회전시에는 순서가 상관이 없는데, 위 아래 / 좌, 우만 따져주면 되기 때문에 빈칸 확보 비교만 필요하다. 순서를 염두해 두었다면 이 부분까지 줄일 수 있었을 것이다.
        if pos1[0]>pos2[0]:
          pos1,pos2=pos2,pos1
        if pos1[1]-1>=0 and board[pos1[0]][pos1[1]-1]==0 and pos2[1]-1>=0 and board[pos2[0]][pos2[1]-1]==0:
          if visited[pos1[0]][pos1[1]]==0 or visited[pos2[0]-1][pos2[1]-1]==0:
            q.append((pos1,(pos2[0]-1,pos2[1]-1)))
          if visited[pos1[0]+1][pos1[1]-1]==0 or visited[pos2[0]][pos2[1]]==0:
            q.append(((pos1[0]+1,pos1[1]-1),pos2))
        if pos1[1]+1<n and board[pos1[0]][pos1[1]+1]==0 and pos2[1]+1<n and board[pos2[0]][pos2[1]+1]==0:
          if visited[pos1[0]][pos1[1]]==0 or visited[pos2[0]-1][pos2[1]+1]==0:
            q.append((pos1,(pos2[0]-1,pos2[1]+1)))
          if visited[pos1[0]+1][pos1[1]+1]==0 or visited[pos2[0]][pos2[1]]==0:
            q.append(((pos1[0]+1,pos1[1]+1),pos2))
      # 가로일 경우
      elif pos1[0]==pos2[0]:
        if pos1[1]>pos2[1]:
          pos1,pos2=pos2,pos1
        if pos1[0]-1>=0 and board[pos1[0]-1][pos1[1]]==0 and pos2[0]-1>=0 and board[pos2[0]-1][pos2[1]]==0:
          if visited[pos1[0]][pos1[1]]==0 or visited[pos2[0]-1][pos2[1]-1]==0:
            q.append((pos1,(pos2[0]-1,pos2[1]-1)))
          if visited[pos1[0]-1][pos1[1]+1]==0 or visited[pos2[0]][pos2[1]]==0:
            q.append(((pos1[0]-1,pos1[1]+1),pos2))
        if pos1[0]+1<n and board[pos1[0]+1][pos1[1]]==0 and pos2[0]+1<n and board[pos2[0]+1][pos2[1]]==0:
          if visited[pos1[0]][pos1[1]]==0 or visited[pos2[0]+1][pos2[1]-1]==0:
            q.append((pos1,(pos2[0]+1,pos2[1]-1)))
          if visited[pos1[0]+1][pos1[1]+1]==0 or visited[pos2[0]][pos2[1]]==0:
            q.append(((pos1[0]+1,pos1[1]+1),pos2))

    q=set(q)
    q=list(q)
    for pos1,pos2 in q:
      visited[pos1[0]][pos1[1]]=1
      visited[pos2[0]][pos2[1]]=1

    answer+=1
    # if answer<10:
    #   print(answer) 


  return answer

board=[[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]
print(solution(board))

# # 풀이시간 초과/50분 시간제한 1초 메모리제한 128MB
# # 1회차 오답 - 풀이시간 초과 + 풀이에 접근 못함
# # 이 문제에서 BFS를 보았다는 사실에 시야가 많이 늘었다는 점은 알겠으나, 방향과 좌표를 다룰 때, 많이 부족한 점을 보였다.
# # 풀이 방식은 BFS로 풀다가 움직일 수 있는 모든 케이스를 두고 똑같이 푸는 방식이다. 또한 시간을 큐에 같이 포함시켜서 진행 시간을 저장하는 것까지도 풀었다.
# # 사실상 메인은 전부 맞게 생각하고 풀었으나, 좌표와 이동 가능성을 따지는 것에서 문제가 있었다.
# # 가장 핵심은 set를 이용하지 못했다는 점이다. 위치를 표현하고 저장 할때, 순서 상관 관계를 없애야 하는데 방법이 없고 해본적이 없으니 튜플로 접근하니 경우의 수가 몇배로 늘어났다.
# # 그리고 추가 적으로 복잡한 조건관계가 많을 때는, 다른 조건관계를 편하게 만들어주기 위해서 테두리를 맵에 추가한다는 점을 한번 더 상기시키는 문제가 되었다. 테두리를 다른 배열의 끝으로 따지면 다른 조건이 되기 때문에 훨씬 복잡해지기 때문이다.
# # 테두리를 추가하는 방식은 알고 있었으나 이것도 사용경험의 부족이기도 하고 DFS/BFS 알고리즘을 다루면서 처음이다보니 내 지식에서 꺼내서 사용하기 힘들었다고 본다.

# # 좌표나 모양, 회전을 다룰 때는, 케이스를 나누어서 자세히 그려보는게 좋은 것 같다. 이미지가 머리 속에 그려지니까 훨씬 접근하기 쉬워진다. 그리고 기준 단위별로 끊어서 행동을 생각하는게 좋아보인다.
# # 그리고 기존 좌표에 너무 얽매여서 +, - 로만 움직이려고 하는 습관을 고쳐야된다.
# # 좌표로 가로와 세로를 표현하는 방법도 익숙하지 않았다.

# # 1회차 풀이
# from collections import deque

# def solution(board):
#   answer = 0
#   n=len(board)

#   # 좌표를 +, -해서 이동시키는데 너무 집착하는 모습이 보인다.
#   dx=[0,0,-1,1]
#   dy=[-1,1,0,0]
#   dsx=[-1,1,0,0]
#   dsy=[1,1,0,0]
#   d

#   # 순서가 상관없는 경우, set를 이용하는 편이 더 편리하고 이 경우에는 거의 필수이다.
#   visited_coordinate=[((0,0),(0,1),0)]
#   q=deque([((0,0),(0,1),0,0)])
#   while q:
#     start,end,state,now=q.popleft()
#     # 가로와 세로를 좌표로 표현하는데 익숙하지 않아서 변수가 더 길어지는 모습이 보인다.
#     # 그림을 그리거나 자세히 나타내지 않아서 조건이 어떻게 나누어지고 어떻게 진행되는지 모습을 실패한 대표 적인 케이스이다.
#     # 문제에서 주어진 단위 별로 상황을 나누어서 표현하고 그 표현을 어떻게 코드화 할지를 생각해야 한다.
#     if state==0:
#       print("가로")
#       for i in range(4):
#         nx_start=start[0]+dx[i]
#         ny_start=start[1]+dy[i]
#         nx_end=end[0]+dx[i]
#         ny_end=end[0]+dy[i]
#         # 테두리를 조건을 줄이기 위해 조건화 하지 못했다. 이러한 점은 이중 배열이나 맵에서 언제든지 확장하여 사용할 수 있다는 점을 생각해두자.
#         if 0<=nx_start<n and 0<=ny_start<n and 0<=nx_end<n and 0<=ny_end<n:
#           if board[nx_start][ny_start]==0 and board[nx_end][ny_end]==0:
#             if ((nx_start,ny_start),(nx_end,ny_end),0) not in visited_coordinate or ((nx_end,ny_end),(nx_start,ny_start),0) not in visited_coordinate:
#               q.append(((nx_start,ny_start),(nx_end,ny_end),0,now+1))
#               visited_coordinate.append(((nx_start,ny_start),(nx_end,ny_end),0))
#       for i in range(4):
#         nx_start=start[0]+drx[i]
#         ny_start=start[1]+dry[i]
#         nx_end=end[0]+drx[i]
#         ny_end=end[0]+dry[i]
#       # 가능한 좌표 가짓 수 - 회전하면서 벽에 안 부딪치고
#       # 로봇이 영역을 벗어나지 않고 and 벽에 안 닿고 and 처음 가보는 좌표이고
#       # 위에 조건을 충족시키면 그 좌표를 큐에 넣고 가본 좌표에 기록하고, 카운트+=1
#       # 만약 위의 조건을 만족시키는 좌표가 끝에 도달했다면 break
#     elif state==1:
#       print("세로")
#       for i in range(4):
#         nx_start=start[0]+dx[i]
#         ny_start=start[1]+dy[i]
#         nx_end=end[0]+dx[i]
#         ny_end=end[0]+dy[i]
#         if 0<=nx_start<n and 0<=ny_start<n and 0<=nx_end<n and 0<=ny_end<n:
#           if board[nx_start][ny_start]==0 and board[nx_end][ny_end]==0:
#             if ((nx_start,ny_start),(nx_end,ny_end),1) not in visited_coordinate or ((nx_end,ny_end),(nx_start,ny_start),1) not in visited_coordinate:
#               q.append(((nx_start,ny_start),(nx_end,ny_end),1,now+1))
#               visited_coordinate.append(((nx_start,ny_start),(nx_end,ny_end),1))
#       # 가능한 좌표 가짓 수 - 벽에 부딪치지 않게

#   answer=count
#   return answer

# 답안 예시
# from collections import deque

# def get_next_pos(pos,board):

#   pos=list(pos) # 현재 위치 정보를 리스트로 변환(집합 -> 리스트)
#   pos1_x,pos1_y,pos2_x,pos2_y=pos[0][0],pos[0][1],pos[1][0],pos[1][1]

#   next_pos=[] # 반환 결과(이동 가능한 위치들)

#   # (상, 하, 좌, 우)로 이동하는 경우에 대해서 처리
#   dx=[0,0,-1,1]
#   dy=[-1,1,0,0]
  
#   for i in range(4):
#     nx_pos1_x,ny_pos1_y,nx_pos2_x,ny_pos2_y=pos1_x+dx[i],pos1_y+dy[i],pos2_x+dx[i],pos2_y+dy[i]
#     # 이동하고자 하는 두 칸이 모두 비어 있다면
#     if board[nx_pos1_x][ny_pos1_y]==0 and board[nx_pos2_x][ny_pos2_y]==0:
#       next_pos.append({(nx_pos1_x,ny_pos1_y),(nx_pos2_x,ny_pos2_y)})
#   # 현재 로봇이 가로로 놓여 있는 경우
#   if pos1_x==pos2_x:
#     for i in [-1,1]: # 위쪽으로 회전가거나, 아래쪽으로 회전
#       if board[pos1_x+i][pos1_y]==0 and board[pos2_x+i][pos2_y]==0: # 위쪽 혹은 아래쪽 두 칸이 모두 비어 있다면
#         next_pos.append({(pos1_x,pos1_y),(pos1_x+i,pos1_y)})
#         next_pos.append({(pos2_x,pos2_y),(pos2_x+i,pos2_y)})
#   elif pos1_y==pos2_y:
#     for i in [-1,1]: # 왼쪽으로 회전하거나, 오른쪽으로 회전
#       if board[pos1_x][pos1_y+i]==0 and board[pos2_x][pos2_y+i]==0: # 왼쪽 혹은 오른쪽 두 칸이 모두 비어 있다면
#         next_pos.append({(pos1_x,pos1_y),(pos1_x,pos1_y+i)})
#         next_pos.append({(pos2_x,pos2_y),(pos2_x,pos2_y+i)})
#   # 현재 위치에서 이동할 수 있는 위치를 반환
#   return next_pos

# def solution(board):
#   # 맵의 외곽에 벽을 두는 형태로 맵 변경
#   n=len(board)
#   answer=0

#   new_board=[[1]*(n+2) for _ in range(n+2)]
#   for i in range(n):
#     for j in range(n):
#       new_board[i+1][j+1]=board[i][j]

#   # 너비 우선 탐색(BFS) 수행
#   pos={(1,1),(1,2)} # 시작 위치 설정
#   visited_coordinate=[] 
#   visited_coordinate.append(pos) # 방문 처리
#   q=deque()
#   s=0
#   q.append((pos,s)) # 큐에 삽입한 뒤에
#   # 큐가 빌 때까지 반복
#   while q:
#     pos,s=q.popleft()
#     # (n, n) 위치에 로봇이 도달했다면, 최단 거리이므로 반환
#     if (n,n) in pos:
#       return s
#     # 현재 위치에서 이동할 수 있는 위치 확인
#     for next_pos in get_next_pos(pos,new_board):
#       # 아직 방문하지 않은 위치라면 큐에 삽입하고 방문 처리
#       if next_pos not in visited_coordinate:
#         visited_coordinate.append(next_pos)
#         q.append((next_pos,s+1))
#   return 0

# board=[[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]
# print(solution(board))