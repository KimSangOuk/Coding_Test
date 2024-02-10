# 풀이시간 58분 시간제한 1초 메모리제한 512MB
# 1회차 정답
# 기준점과 경계의 길이에 대한 조건대로 좌표를 찾은 다음 그 가능한 모든 좌표에 대해서 시뮬레이션 대로 구획을 나누고 그 구획의 최대인원 수와 최소 인원 수가 되는 곳을 찾아 차의 최솟값을 구하면 되는 문제이다. 처음 문제를 접했을 때, 좌표에 대한 조건과 경계에 대한 좌표 조건이 복잡하고 구획을 나눌 때도 조건이 복잡해지기 때문에 다른 알고리즘을 적용하기 어렵다고 판단하여 좌표에서 시간복잡도가 줄어들 것이라 예상만 하고 브루트포스 알고리즘으로 풀었다. 좌표또한 주어진 조건에 따라 제한 하고 그 좌표에 따라 경계를 일일이 표시하였으며 나누어진 구획으로 일일이 인원수를 더해서 구했다.

n=int(input())

a=[[0]*(n+1) for _ in range(n+1)]
for i in range(1,n+1):
    arr=list(map(int,input().split()))
    for j in range(1,n+1):
        a[i][j]=arr[j-1]

def make_area(board,x,y,d1,d2):
    for k in range(0,d1+1):
        board[x+k][y-k]=5
        board[x+d2+k][y+d2-k]=5
    for k in range(0,d2+1):
        board[x+k][y+k]=5
        board[x+d1+k][y-d1+k]=5

    start=x
    end=x+d1+d2
    for r in range(1,n+1):
        boundary=False
        for c in range(1,n+1):
            if board[r][c]==5:
                if boundary:
                    boundary=False
                else:
                    boundary=True
                continue
            if boundary and r!=start and r!=end:
                board[r][c]=5
            else:
                if 1<=r<x+d1 and 1<=c<=y:
                    board[r][c]=1
                elif 1<=r<=x+d2 and y<c<=n:
                    board[r][c]=2
                elif x+d1<=r<=n and 1<=c<y-d1+d2:
                    board[r][c]=3
                elif x+d2<r<=n and y-d1+d2<=c<=n:
                    board[r][c]=4

def area_max_min(board,a):
    value=[0]*(6)
    for i in range(1,n+1):
        for j in range(1,n+1):
            value[board[i][j]]+=a[i][j]
    return max(value[1:])-min(value[1:])

result=int(1e9)
for d1 in range(1,n+1):
    for d2 in range(1,n+1):
        for x in range(1,n+1):
            if 1<=x<x+d1+d2 and x+d1+d2<=n:
                for y in range(1,n+1):
                    if 1<=y-d1<y and y<y+d2<=n:
                        board=[[0]*(n+1) for _ in range(n+1)]
                        make_area(board,x,y,d1,d2)
                        result=min(result,area_max_min(board,a))

print(result)