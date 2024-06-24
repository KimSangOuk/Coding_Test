# 한 지점으로 부터 시작하면서 갯수를 샌다고 가정하면서 그 지점 전체를 덮기 때문에 배열로 두고 덮이는 지점과 끝나는 점을 생각하면 된다고 생각했다. 즉, 1부터 시작했을 때 2면 1과 2 이렇게 세면 된다는 것이다. 그렇기 때문에 구멍난 지점을 기록해두고 길이를 늘려가면서 전체 구간을 순회하면서 덮을 테이프의 갯수를 구하면 된다. 앞에서부터 필요한 지점을 찾아 덮으면 됨으로 그리디 스럽다고 할 수 있을 것 같다(?)
# 풀이시간 : 20분

n,l=map(int,input().split())
arr=[0]*2001
tmp=list(map(int,input().split()))
for i in range(n):
    arr[tmp[i]]=1
start=False
answer=0
now_length=0
for i in range(1001):
    if not start and arr[i]==1:
        start=True
        answer+=1
        now_length+=1
        if now_length==l:
            now_length=0
            start=False
    elif start:
        now_length+=1
        if now_length==l:
            now_length=0
            start=False
print(answer)