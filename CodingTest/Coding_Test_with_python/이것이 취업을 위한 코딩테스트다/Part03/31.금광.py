# 풀이시간 15분 시간제한 1초 메모리제한 128MB
# 2회차 풀이
# 단순히 전의 단계의 왼쪽 위, 왼쪽, 왼쪽 아래 중에서 큰 수를 현재의 수에 누적시키면서 나아가면 되는 다이나믹 프로그래밍이다. 보드의 크기는 최대 400이기 떄문에 문제가 되지 않고 아마 다시 푼 이유는 index를 다루는데 있어서 더 간편하게 다루는 방법을 적응하기 위해 다시 풀기로 했던 걸로 기억이 난다.

for tc in range(int(input())):
  n,m=map(int,input().split())
  array=list(map(int,input().split()))
  board=[]
  for i in range(n):
    arr=[]
    for j in range(m):
      arr.append(array[i*m+j])
    board.append(arr)

  dp=[[0]*m for _ in range(n)]
  for i in range(n):
    dp[i][0]=board[i][0]

  for i in range(1,m):
    for j in range(n):
      left=dp[j][i-1]
      if j-1<0:
        left_up=0
      else:
        left_up=dp[j-1][i-1]
      if j+1>=n:
        left_down=0
      else:
        left_down=dp[j+1][i-1]
      
      dp[j][i]=max(left_up,left,left_down)+board[j][i]
  answer=0
  for i in range(n):
    answer=max(answer,dp[i][m-1])
  print(answer)

# 풀이시간 30분/30분 시간제한 1초 메모리제한 128MB
# 1회차 정답 - 하지만 더 간단히 쓸 수 있다고 생각해서 한 번 더 풀이
# 단순히 문제를 살펴보면 앞에서의 반복이 뒤에서의 문제 답을 내는 것에 영향을 미치기 때문에 다이나믹 프로그래밍을 생각해볼 수 있는 문제이다.
# 문제 해답에서는 필요한 식을 한번만 쓰기 위해서 식을 더욱 간단하게 표현한 방법을 사용하였기에 이를 배우고자 한번 더 풀어보기로 하였다. 기본적인 풀이나 아이디어는 똑같다.
# 단순하게 인덱스를 구분하기 보다는 끝과 아닌 경우만 구분하면 된다는 생각이었다. 물론 줄이 하나일 때의 생각이 들긴했지만 간단한 조건만 붙인다면 풀 수 있을 것이라 생각했다. 결국, 없는 값을 0으로 둔다는 생각을 하지 못한 것이 잘못이었다.
# 왜 없는 값을 0으로 둔다는 생각을 하지 못했는가? 모든 케이스를 고려하는 경우, 공통된 결과를 도출해내는 것이 필요한데 어떤 경우라도, 그 경우를 만들려고 하지 않았다. 케이스를 계속해서 늘리는 것보다는 공통적으로 케이스를 규합하고 그 케이스에 맞게 만드는 것이 좋다는 것을 깨달았다.

# 1회차 풀이
# t=int(input())

# for _ in range(t):
#   n,m=map(int,input().split())
#   temp=list(map(int,input().split()))
#   array=[[0]*m for _ in range(n)]
#   for i in range(n):
#     for j in range(m):
#       array[i][j]=temp[i*m+j]

#   # 여기서 인덱스로 구분이 복잡해질 경우 인덱스로 먼저 들어갈 값을 구분한 후 그 값들을 받아놨다가
#   # 전체계산은 한번만 해도 된다는 것을 배울 수 있다.
#   for j in range(1,m):
#     for i in range(n):
#       # 여기서 끝인 경우와 아닌 경우를 구분해서 마지막 공식에 들어갈 값을 구분한다.
#       if i==0 and i!=n-1:
#         array[i][j]+=max(array[i][j-1],array[i+1][j-1])
#       elif i==n-1 and i!=0:
#         array[i][j]+=max(array[i][j-1],array[i-1][j-1])
#       else:
#         if i==n-1 and i==0:
#           array[i][j]+=array[i][j-1]
#         else:
#           array[i][j]+=max(array[i][j-1],array[i+1][j-1],array[i-1][j-1])
  
#   result=0
#   for i in range(n):
#     result=max(result,array[i][m-1])
#   print(result)

# # 풀이 방법
# # 테이스 케이스(Test Case) 입력
# for tc in range(int(input())):
#   # 금광 정보 입력
#   n,m=map(int,input().split())
#   array=list(map(int,input().split()))

#   # 다이나믹 프로그래밍을 위한 2차원 DP 테이블 초기화
#   dp = []
#   index = 0
#   for i in range(n):
#     dp.append(array[index:index+m])
#     index+=m

#   # 다이나믹 프로그래밍 진행
#   for j in range(1,m):
#     for i in range(n):
#       # 왼쪽 위에서 오는 경우
#       if i==0:
#         left_up=0
#       else:
#         left_up=dp[i-1][j-1]
#       # 왼쪽 아래에서 오는 경우
#       if i==n-1:
#         left_down=0
#       else:
#         left_down=dp[i+1][j-1]
#       # 왼쪽에서 오는 경우
#       left=dp[i][j-1]
#       dp[i][j]=dp[i][j]+max(left_up,left_down,left)

#   result=0
#   for i in range(n):
#     result=max(result,dp[i][m-1])

#   print(result)