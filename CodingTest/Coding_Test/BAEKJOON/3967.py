import sys
from bisect import bisect_left

input=sys.stdin.readline

board=[list(input().strip()) for _ in range(5)]

deep=0
visited=0
index=0
alphaList=[-1]*12
for i in range(5):
    for j in range(9):
        if board[i][j].isalpha():
            if board[i][j]=='x':
                index+=1
                continue
            deep+=1
            visited|=(1<<(ord(board[i][j])-ord('A')))
            alphaList[index]=ord(board[i][j])-ord('A')+1
            index+=1

def dfs(deep,alphaList,visited):
    # print(alphaList)
    if not check(alphaList):
        return
    if deep==12:
        return True
    for i in range(12):
        if visited&(1<<i):
            continue
        index=-1
        for k in range(12):
            if alphaList[k]==-1:
                index=k
                break
        alphaList[index]=i+1
        if dfs(deep+1,alphaList,visited|(1<<i)):
            return True
        alphaList[index]=-1

def check(alphaList):
    arr=alphaList
    if arr[0]!=-1 and arr[2]!=-1 and arr[5]!=-1 and arr[7]!=-1:
        if arr[0]+arr[2]+arr[5]+arr[7]!=26:
            return False
    if arr[1]!=-1 and arr[2]!=-1 and arr[3]!=-1 and arr[4]!=-1:
        if arr[1]+arr[2]+arr[3]+arr[4]!=26:
            return False
    if arr[0]!=-1 and arr[3]!=-1 and arr[6]!=-1 and arr[10]!=-1:
        if arr[0]+arr[3]+arr[6]+arr[10]!=26:
            return False
    if arr[1]!=-1 and arr[5]!=-1 and arr[8]!=-1 and arr[11]!=-1:
        if arr[1]+arr[5]+arr[8]+arr[11]!=26:
            return False
    if arr[4]!=-1 and arr[6]!=-1 and arr[9]!=-1 and arr[11]!=-1:
        if arr[4]+arr[6]+arr[9]+arr[11]!=26:
            return False
    if arr[7]!=-1 and arr[8]!=-1 and arr[9]!=-1 and arr[10]!=-1:
        if arr[7]+arr[8]+arr[9]+arr[10]!=26:
            return False
    return True

dfs(deep,alphaList,visited)
# print(alphaList)
printIndex=0
for i in range(5):
    for j in range(9):
        if board[i][j].isalpha():
            print(chr(alphaList[printIndex]-1+ord('A')),end='')
            printIndex+=1
        else:
            print(board[i][j],end='')
    print()