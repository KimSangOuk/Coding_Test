from collections import deque

for tc in range(1,int(input())+1):
    N,K=map(int,input().split())
    arr=deque(list(input()))
    sideNum=N//4
    allCase=set()
    for _ in range(sideNum):
        arr.appendleft(arr.pop())
        for i in range(0,N,sideNum):
            allCase.add(int("0x"+"".join(list(arr)[i:i+sideNum]),16))
    print("#"+str(tc)+" "+str(sorted(allCase,reverse=True)[K-1]))