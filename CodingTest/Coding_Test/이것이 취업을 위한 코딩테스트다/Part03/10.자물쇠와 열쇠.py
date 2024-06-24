# 풀이시간 25분/40분 시간제한 1초 메모리제한 128MB
# 3회차 풀이
# 자물쇠의 크기를 확장해서 열쇠의 회전의 경우를 모두 고려해서 끼워맞춘 다음 전부 자물쇠가 1로 만들어지는 순간이 있다면 True 없다면 False를 출력하는 문제이다. 모든 경우를 고려하는 완전 탐색 문제라고 할 수 있다.
# 이 때, 핵심 내가 놓쳤던 아이디어들은 자물쇠 크기의 여유로운 확장과 인덱스를 고려한 확장 / 그리고 키를 끼우고 뺄때 새롭게 만들어서 메모리 공간을 절약하는 +, - / 2차원 배열의 회전 시에는 대칭을 이용하는 법 이렇게 3가지가 있다.

def rotate_key(key):
  new_board=[[0]*len(key) for _ in range(len(key))]
  for i in range(len(key)):
    for j in range(len(key)):
      new_board[j][len(key)-1-i]=key[i][j]

  return new_board

def check(lock,key,start):
  n=len(lock)//3
  start_x,start_y=start
  answer=True
  for i in range(start_x,start_x+len(key)):
    for j in range(start_y,start_y+len(key)):
      lock[i][j]+=key[i-start_x][j-start_y]

  for i in range(n,2*n):
    for j in range(n,2*n):
      if lock[i][j]!=1:
        answer=False

  for i in range(start_x,start_x+len(key)):
    for j in range(start_y,start_y+len(key)):
      lock[i][j]-=key[i-start_x][j-start_y]

  return answer

def solution(key, lock):
  answer = False

  n=len(lock)
  m=len(key)
  expand_lock=[[0]*(3*n) for _ in range(3*n)]

  for i in range(n,2*n):
    for j in range(n,2*n):
      expand_lock[i][j]=lock[i-n][j-n]

  for i in range(4):
    key=rotate_key(key)
    for i in range(2*n):
      for j in range(2*n):
        if check(expand_lock,key,(i,j)):
          return True
          
  return answer


# 2회차 풀이
# 1시간 정도로 정답을 도출해내긴 했으나 시간을 더 단축시키고 풀이를 단순화할 수 있다고 생각해서 추가적으로 풀기로 함. 1회차에서 깨달은 점이기도 하지만, 무시하지 못한거 같음.
# 단순히 3배로 확장해서 풀어내면 인덱스에서 더 단순함을 얻을 수 있음. 딱 이부분만 더 얻을 점이 있고 추가적으로 시간이 열쇠를 돌리는데에서도 또 좀 걸렸는데, 단순히 원하는 모양이 될때까지 반전시키면 된다는 것을 기억하면 다음에 회전이 아닌 다른 모양을 만들 때도 도움이 된다고 생각함.
# 즉, 크기를 보았을 때, 시간복잡도에 영향을 끼치지 않을 정도면 단순하게 확장하는 것이 인덱스를 다루는데 더 쉬움.
# 내가 약간, 모든 것을 최소로 다루어야된다고 생각하는 경향이 있는데, 이게 잘못된거 만은 아니지만, 시간복잡도에 영향을 끼치지 않을 때만 그래서 위의 방법을 써야함.

# def check_all(lock,lock_size,key_size):
#   for i in range(key_size-1,key_size+lock_size-1):
#     for j in range(key_size-1,key_size+lock_size-1):
#       if lock[i][j]!=1:
#         return False

#   return True

# def rotate_key(key):
#   key_size=len(key)
#   new_key=[[0]*key_size for i in range(key_size)]

#   for i in range(key_size):
#     for j in range(key_size):
#       new_key[j][key_size-1-i]=key[i][j]
#   return new_key

# def solution(key, lock):
#   answer = True

#   key_size=len(key)
#   lock_size=len(lock)
#   new_lock=[[0]*(lock_size+(key_size)*2-2) for i in range(lock_size+key_size*2-2)]

#   for i in range(key_size-1,key_size-1+lock_size):
#     for j in range(key_size-1,key_size-1+lock_size):
#       new_lock[i][j]=lock[i-key_size+1][j-key_size+1]

#   for _ in range(4):
#     key=rotate_key(key)

#     for j in range(0,key_size+lock_size-1):
#       for k in range(0,key_size+lock_size-1):
#         for a in range(key_size):
#           for b in range(key_size):
#             new_lock[j+a][k+b]+=key[a][b]

#         # for c in range(len(new_lock)):
#         #   for d in range(len(new_lock)):
#         #     print(new_lock[c][d],end=" ")
#         #   print()
          
#         if check_all(new_lock,lock_size,key_size):
#           return True
        
#         for a in range(key_size):
#           for b in range(key_size):
#             new_lock[j+a][k+b]-=key[a][b]

  
#   return False


# 풀이 시간 - 1시간 30분/40분 시간제한 1초 메모리제한 128MB
# 1회차 오답 - 풀이시간 초과
# n,m의 판 크기가 20을 넘지 않는것을 보고 엄청 여러번 for문을 중첩시켜도 되겠구나 생각이 들었음. 그리고 마침. 하나씩 맞춰보는 알고리즘을 써야할 것 같아서 완전탐색이라는 것도 알게됨.
# 결국 풀어냈지만 시간이 너무 오래걸렸고 더 배울 아이디어가 있음.

# # 1회차 풀이
# # 회전까지도 괜찮게 생각했고 4번 돌리는 것과 판에서 이동시키는 것까지도 괜찮았으나 판위에서 열쇠를 이동시키고 그 이동한 자국을 표현하는데 애먹음. 여기서 막혀서 시간 초과가 나옴. 맨 처음에는 확장한 판에서 열쇠랑 비교대조를 하려고 하였으나 가운데만을 또 측정하지 않아서 오답이 나왔는지 않됨. 그래서 열쇠를 판에 완전히 끼어넣어 표현한 다음 그 판의 가운데가 맞는 확인하고자 함. 그러자 이제 열쇠를 더해서 끼어넣는 아이디어가 생각남. 하지만 끼워넣은 다음에 판을 리셋을 시켜야하는 문제에 다시 직면함. 이 문제를 나는 판을 새로 만들어서 구했지만 그냥 다시 빼는 방법도 존재했었고 이게 더 쉬웠음.
# import copy

# def solution(key,lock):
#   answer=False

#   # 자물쇠 확장을 위해 key-1 길이를 구함
#   expand_size=len(key)-1
#   # 양 사이드 확장한 크기의 lock, 어차피 외부부분은 돌기랑 충돌이 상관없으니 0으로
#   expand_lock=[[0]*(expand_size*2+len(lock)) for _ in range(expand_size*2+len(lock))]

#   # 확장한 락에 가운데에 기존의 락을 새겨넣음
#   for i in range(expand_size,expand_size+len(lock)):
#     for j in range(expand_size,expand_size+len(lock)):
#       expand_lock[i][j]=lock[i-expand_size][j-expand_size]

#   lock_count=len(lock)*len(lock)

#   board=rotate_clock(key)
#   # 키는 총 4번 확인 가능
#   for _ in range(4):
#     for i in range(expand_size+len(lock)):
#       for j in range(expand_size+len(lock)):
#         # 여기서 1차원적인 변화임에도 판이 새로필요하다고 계속 생각해서, 즉 해본적이 없어서 그냥 판을 새로 만들려고 함. 여기서 시간도 많이 잡아먹고 고정관념을 계속 사용함.
#         new_lock=copy.deepcopy(expand_lock)
#         for k in range(len(key)):
#           for t in range(len(key)):
#             # 이 부분을 생각하기 위해 비교대조가 아니라 끼워넣는 걸 표현하는 아이디어가 먼저 떠오른 다음에 생각남. 이 부분이 오래걸렸고 비교대조가 안되는 걸 깨닫느라 시간이 오래걸림.
#             new_lock[i+k][j+t]+=board[k][t]
#         # for k in range(len(new_lock)):
#         #   print(new_lock[k])
#         # print()
#         # 여기서는 나쁘지 않았으나 정답지 방법이 더 마음에 듬. 그냥 아닌지 맞는지만 구할 꺼라면 함수를 써서 True, False만 잡아내는 게 더 좋아보임. 쓸데없이 식이 길어지기도 하고 변수가 계속 추가되어야 함. 일정부분에서도 구하고자 하는게 무엇인지 한다음에 그 무엇을 확실히 구할 빠른 방법이 있는지 생각해보야야 함.
#         for k in range(expand_size,expand_size+len(lock)):
#           for t in range(expand_size,expand_size+len(lock)):
#             if new_lock[k][t]==1:
#               lock_count-=1
#         if lock_count==0:
#           return True
#         lock_count=len(lock)*len(lock)

#     board=rotate_clock(board)
    


#   return answer

# # 유일하게 마음에 드는 부분, 난 답지보다 더 간단하게 표현하고 구했다고 본다. 답지의 아이디어는 어떻게 했는지 잘 모르겠음. 그리고 아이디어가 좀 어려움.
# def rotate_clock(key):
#   board=[]

#   for j in range(len(key)):
#     arr=[]
#     for i in range(len(key)-1,-1,-1):
#       arr.append(key[i][j])
#     board.append(arr)

#   return board

key=[[0,0,0],[1,0,0],[0,1,1]]
lock=[[1,1,1],[1,1,0],[1,0,1]]
print(solution(key,lock))

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