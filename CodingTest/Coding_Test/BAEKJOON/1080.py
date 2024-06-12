# - 왼쪽 위에서 부터 비교하면서 틀리면 뒤집고, 그 뒤집은 것을 반영한 상태에서 계속해서 탐색하면서 다른게 있으면 뒤집으면 된다. 결과적으로 1,0의 상태밖에 없기 때문에 목표의 행렬처럼 만들기 위해서는 뒤집어야하기 때문이다. 그렇기 때문에 현 상태에서 다른 것만을 보고 탐색으로 찾아나가는 그리디 유형이라고 할 수 있다.
# - 3*3이 최대 크기 이기 때문에 이 부분에 유의하면서 범위를 나타내주면 되며 이 범위내에서도 다른게 있는지 없는지 확인해주어야 한다.
# - 풀이시간 : 25분

n,m=map(int,input().split())
main_board=[]
for i in range(n):
    main_board.append(list(input()))
target_board=[]
for i in range(n):
    target_board.append(list(input()))

def make_main_to_target(main_board,target_board,n,m):
    cnt=0
    for i in range(n-2):
        for j in range(m-2):
            if main_board[i][j]!=target_board[i][j]:
                cnt+=1
                for k in range(3):
                    for t in range(3):
                        main_board[i+k][j+t]=str(int(not bool(int(main_board[i+k][j+t]))))
    for i in range(n):
        for j in range(m):
            if main_board[i][j]!=target_board[i][j]:
                return False
    return cnt

if n<3 or m<3:
    possible=True
    for i in range(n):
        for j in range(m):
            if main_board[i][j]!=target_board[i][j]:
                possible=False
                break
    if not possible:
        print(-1)
    else:
        print(0)
else:
    answer=make_main_to_target(main_board,target_board,n,m)
    if not answer:
        print(-1)
    else:
        print(answer)