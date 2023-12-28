# 풀이 시간 - 1시간 30분/40분 시간제한 1초 메모리제한 128MB
# 1회차 오답 - 풀이시간 초과
# n,m의 판 크기가 20을 넘지 않는것을 보고 엄청 여러번 for문을 중첩시켜도 되겠구나 생각이 들었음. 그리고 마침. 하나씩 맞춰보는 알고리즘을 써야할 것 같아서 완전탐색이라는 것도 알게됨.
# 결국 풀어냈지만 시간이 너무 오래걸렸고 더 배울 아이디어가 있음.

# 2회차 풀이



































# 1회차 풀이
# 회전까지도 괜찮게 생각했고 4번 돌리는 것과 판에서 이동시키는 것까지도 괜찮았으나 판위에서 열쇠를 이동시키고 그 이동한 자국을 표현하는데 애먹음. 여기서 막혀서 시간 초과가 나옴. 맨 처음에는 확장한 판에서 열쇠랑 비교대조를 하려고 하였으나 가운데만을 또 측정하지 않아서 오답이 나왔는지 않됨. 그래서 열쇠를 판에 완전히 끼어넣어 표현한 다음 그 판의 가운데가 맞는 확인하고자 함. 그러자 이제 열쇠를 더해서 끼어넣는 아이디어가 생각남. 하지만 끼워넣은 다음에 판을 리셋을 시켜야하는 문제에 다시 직면함. 이 문제를 나는 판을 새로 만들어서 구했지만 그냥 다시 빼는 방법도 존재했었고 이게 더 쉬웠음.
import copy

def solution(key,lock):
  answer=False

  # 자물쇠 확장을 위해 key-1 길이를 구함
  expand_size=len(key)-1
  # 양 사이드 확장한 크기의 lock, 어차피 외부부분은 돌기랑 충돌이 상관없으니 0으로
  expand_lock=[[0]*(expand_size*2+len(lock)) for _ in range(expand_size*2+len(lock))]

  # 확장한 락에 가운데에 기존의 락을 새겨넣음
  for i in range(expand_size,expand_size+len(lock)):
    for j in range(expand_size,expand_size+len(lock)):
      expand_lock[i][j]=lock[i-expand_size][j-expand_size]

  lock_count=len(lock)*len(lock)

  board=rotate_clock(key)
  # 키는 총 4번 확인 가능
  for _ in range(4):
    for i in range(expand_size+len(lock)):
      for j in range(expand_size+len(lock)):
        # 여기서 1차원적인 변화임에도 판이 새로필요하다고 계속 생각해서, 즉 해본적이 없어서 그냥 판을 새로 만들려고 함. 여기서 시간도 많이 잡아먹고 고정관념을 계속 사용함.
        new_lock=copy.deepcopy(expand_lock)
        for k in range(len(key)):
          for t in range(len(key)):
            # 이 부분을 생각하기 위해 비교대조가 아니라 끼워넣는 걸 표현하는 아이디어가 먼저 떠오른 다음에 생각남. 이 부분이 오래걸렸고 비교대조가 안되는 걸 깨닫느라 시간이 오래걸림.
            new_lock[i+k][j+t]+=board[k][t]
        # for k in range(len(new_lock)):
        #   print(new_lock[k])
        # print()
        # 여기서는 나쁘지 않았으나 정답지 방법이 더 마음에 듬. 그냥 아닌지 맞는지만 구할 꺼라면 함수를 써서 True, False만 잡아내는 게 더 좋아보임. 쓸데없이 식이 길어지기도 하고 변수가 계속 추가되어야 함. 일정부분에서도 구하고자 하는게 무엇인지 한다음에 그 무엇을 확실히 구할 빠른 방법이 있는지 생각해보야야 함.
        for k in range(expand_size,expand_size+len(lock)):
          for t in range(expand_size,expand_size+len(lock)):
            if new_lock[k][t]==1:
              lock_count-=1
        if lock_count==0:
          return True
        lock_count=len(lock)*len(lock)

    board=rotate_clock(board)
    


  return answer

# 유일하게 마음에 드는 부분, 난 답지보다 더 간단하게 표현하고 구했다고 본다. 답지의 아이디어는 어떻게 했는지 잘 모르겠음. 그리고 아이디어가 좀 어려움.
def rotate_clock(key):
  board=[]

  for j in range(len(key)):
    arr=[]
    for i in range(len(key)-1,-1,-1):
      arr.append(key[i][j])
    board.append(arr)

  return board

key=[[0,0,0],[1,0,0],[0,1,1]]
lock=[[1,1,1],[1,1,0],[1,0,1]]
solution(key,lock)

# # 답안지
# # 2차원 리스트 90도 회전
# def rotate_a_matrix_by_90_degree(a):
#   n=len(a) # 행 길이 계산
#   m=len(a[0])
#   result=[[0]*n for _ in range(m)] # 결과 리스트
#   for i in range(n):
#     for j in range(m):
#       result[j][n-i-1]=a[i][j]
#   return result

# # 자물쇠의 중간 부분이 모두 1인지 확인
# def check(new_lock):
#   lock_length=len(new_lock)//3
#   for i in range(lock_length,lock_length*2):
#     for j in range(lock_length,lock_length*2):
#       if new_lock[i][j]!=1:
#         return False
#   return True

# def solution(key,lock):
#   n=len(lock)
#   m=len(key)
#   # 자물쇠의 크기를 기존의 3배로 변환
#   new_lock=[[0]*(n*3) for _ in range(n*3)]
#   # 새로운 자물쇠의 중앙 부분에 기존의 자물쇠 넣기
#   for i in range(n):
#     for j in range(n):
#       new_lock[i+n][j+n]=lock[i][j]

#   # 4가지 방향에 대해서 확인
#   for rotation in range(4):
#     key=rotate_a_matrix_by_90_degree(key) # 열쇠 회전
#     for x in range(n*2):
#       for y in range(n*2):
#         # 자물쇠에 열쇠를 끼워 넣기
#         for i in range(m):
#           for j in range(m):
#             new_lock[x+i][y+i]+=key[i][j]
#         # 새로운 자물쇠에 열쇠가 정확히 들어맞는지 검사
#         if check(new_lock)==True:
#           return True
#         # 자물쇠에서 열쇠를 다시 빼기
#         for i in range(m):
#           for j in range(m):
#             new_lock[x+i][y+j]-=key[i][j]
  
#   return False