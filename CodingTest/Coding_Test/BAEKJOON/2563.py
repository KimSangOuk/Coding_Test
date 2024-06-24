# - 전체 영역을 다 0이라 두었을 때, 겹치는 여러개의 영역의 넓이를 구하는 것이기 때문에 전체를 배열로 두고 칠해진 영역을 다른 수로 두고 숫자를 세면 된다. 각 변에서 떨어진 길이는 시작점이고 길이와 높이는 10인 정사각형이 된다. 이 때, 겹치는 것이 상관없이 칠하면 된다.
# - 풀이시간 : 5분

board=[[0]*100 for _ in range(100)]
n=int(input())
for i in range(n):
    a,b=map(int,input().split())
    for j in range(10):
        for k in range(10):
            board[a+j][b+k]=1

answer=0
for i in range(100):
    for j in range(100):
        if board[i][j]==1:
            answer+=1
print(answer)