# 풀이시간 50분 시간제한 2초 메모리제한 512MB
# 1회차 정답
# 조건에 맞춰서 가로열과 세로열을 뽑아낸 후 조건을 따져가면서 높아질 경우와 낮아질 경우, 같을 경우를 한칸 씩 진행해가면서 가능여부를 구하면 된다. 구현의 달린 조건이 복잡한 문제이다.

import copy

n,l=map(int,input().split())

board=[]
for _ in range(n):
    board.append(list(map(int,input().split())))

def check(arr):
    now=arr[0]
    can=[True]*len(arr)
    for i in range(1,n):
        if now==arr[i]:
            now=arr[i]
            continue
        elif abs(now-arr[i])==1:
            # 한칸 높아지는 경우
            if now<arr[i]:
                # 경사로를 설치할 공간이 부족해서 맵을 벗어날 경우
                if i-l<0:
                    return False
                # 이미 사용한 공간일 경우
                k=arr[i-l:i]
                for j in range(i-l,i):
                    if can[j]==False:
                        return False
                # 경사로를 설치할 곳에 높이가 다른 경우
                for t in k:
                    if t!=now:
                        return False
                # 사용한 지점은 다시 설치할 수 없도록 표시
                for j in range(i-l,i):
                    can[j]=False
            # 한칸 낮아지는 경우
            else:
                # 경사로를 설치할 공간이 부족해서 맵을 벗어나거나
                if i+l-1>=len(arr):
                    return False
                # 한칸 내려진 지점이 경사로를 설치할 공간만큼 없으면
                k=arr[i:i+l]
                for t in k:
                    if t!=arr[i]:
                        return False
                # 사용한 지점은 다시 설치할 수 없도록 표시
                for j in range(i,i+l):
                    can[j]=False
            now=arr[i]
        else:
            return False
    return True

count=0
for i in range(n):
    arr=copy.deepcopy(board[i])
    if check(arr):
        count+=1

for j in range(n):
    arr=[]
    for i in range(n):
        arr.append(board[i][j])
    if check(arr):
        count+=1

print(count)