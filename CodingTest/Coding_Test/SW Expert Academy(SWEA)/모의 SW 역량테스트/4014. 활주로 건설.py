import math

def check(arr):
    stack=0
    prev=arr[0]
    for i in range(n):
        if prev!=arr[i]:
            if arr[i]-prev==1 and stack>=l:
                stack=0
            elif prev-arr[i]==1:
                t=arr[i:i+l]
                if len(t)<l:
                    return False
                if len(set(t))!=1:
                    return False
                stack=-l
            else:
                return False
            
            
        stack+=1
        prev=arr[i]
    return True

for tc in range(1,int(input())+1):
    n,l=map(int,input().split())

    board=[list(map(int,input().split())) for _ in range(n)]

    answer=0
    for i in range(n):
        tmp1=[]
        tmp2=[]
        for j in range(n):
            tmp1.append(board[i][j])
            tmp2.append(board[j][i])
        if check(tmp1):
            answer+=1
        if check(tmp2):
            answer+=1
    print("#"+str(tc)+" "+str(answer))
