# 풀이시간 30분 시간제한 2초 메모리제한 128MB
# 1회차 정답
# 단순하게 체스판을 그린 후 각 부분에서 추출해서 비교하는 브루트 포스 알고리즘이다. 이 때, 시간 복잡도는 50*50*8*8 이 최대 이기 때문에 O(N)일 때 가능하다.

n,m=map(int,input().split())
board=[]

for i in range(n):
  k=input()
  arr=[]
  for j in range(m):
    arr.append(k[j])
  board.append(arr)

one_chess=[['W']*8 for _ in range(8)]
two_chess=[['B']*8 for _ in range(8)]

for i in range(8):
  for j in range(8):
    if i%2==0 and j%2!=0:
      one_chess[i][j]='B'
      two_chess[i][j]='W'
    elif i%2!=0 and j%2==0:
      one_chess[i][j]='B'
      two_chess[i][j]='W'

def check_chess_board(chess,one_chess,two_chess):
  one=0
  two=0
  for i in range(8):
    for j in range(8):
      if chess[i][j]!=one_chess[i][j]:
        one+=1
      if chess[i][j]!=two_chess[i][j]:
        two+=1
  return min(one,two)

chess=[['']*8 for _ in range(8)]
answer=int(1e9)
for i in range(n-8+1):
  for j in range(m-8+1):
    for a in range(8):
      for b in range(8):
        chess[a][b]=board[i+a][j+b]
    answer=min(check_chess_board(chess,one_chess,two_chess),answer)

print(answer)