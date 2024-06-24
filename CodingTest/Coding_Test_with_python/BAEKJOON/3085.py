# 풀이시간 20분 시간제한 1초 메모리제한 128MB
# 1회차 정답
# 두개씩 가로와 세로로 바꿀 수 있는 모든 경우를 바꿔가면서 그 때의 가로와 세로의 이어지는 길이중 가장 긴 길이를 구하면 되는 완전탐색 문제이다. 이 때의 시간복잡도를 위한 횟수를 계산하면 n=50이 최대이기 때문에 약 1300만 정도가 되기 때문에 충분히 가능하다.

n=int(input())

board=[]
for _ in range(n):
    board.append(list(input()))

result=0
for i in range(n):
    for j in range(n-1):
        board[i][j],board[i][j+1]=board[i][j+1],board[i][j]
        for t in range(n):
            now1=board[t][0]
            count1=1
            now2=board[0][t]
            count2=1
            for f in range(1,n):
                if now1==board[t][f]:
                    count1+=1
                    result=max(result,count1)
                else:
                    now1=board[t][f]
                    count1=1
                if now2==board[f][t]:
                    count2+=1
                    result=max(result,count2)
                else:
                    now2=board[f][t]
                    count2=1
        board[i][j+1],board[i][j]=board[i][j],board[i][j+1]
        board[j][i],board[j+1][i]=board[j+1][i],board[j][i]
        for t in range(n):
            now1=board[t][0]
            count1=1
            now2=board[0][t]
            count2=1
            for f in range(1,n):
                if now1==board[t][f]:
                    count1+=1
                    result=max(result,count1)
                else:
                    now1=board[t][f]
                    count1=1
                if now2==board[f][t]:
                    count2+=1
                    result=max(result,count2)
                else:
                    now2=board[f][t]
                    count2=1
        board[j][i],board[j+1][i]=board[j+1][i],board[j][i]

print(result)

