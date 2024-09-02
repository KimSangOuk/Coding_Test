from itertools import combinations

for tc in range(1,int(input())+1):
    N,M,C=map(int,input().split())
    answer=0
    board=[list(map(int,input().split())) for _ in range(N)]
    for x1 in range(N):
        for y1 in range(N):
            for x2 in range(N):
                for y2 in range(N):
                    group1=set()
                    group2=set()
                    outOfBound=False
                    for m in range(M):
                        if y1+m<0 or y1+m>=N or y2+m<0 or y2+m>=N:
                            outOfBound=True
                            break
                        group1.add((x1,y1+m))
                        group2.add((x2,y2+m))
                    if outOfBound:
                        continue
                    if len(group1&group2)>0:
                        continue
                    group1=[board[x][y] for x,y in list(group1)]
                    group2=[board[x][y] for x,y in list(group2)]
                    maxValue1=0
                    maxValue2=0
                    for i in range(1,M+1):
                        for case in list(combinations(group1,i)):
                            if sum(case)>C:
                                continue
                            sum1=0
                            for k in case:
                                sum1+=k*k
                            maxValue1=max(maxValue1,sum1)
                    for i in range(1,M+1):
                        for case in list(combinations(group2,i)):
                            if sum(case)>C:
                                continue
                            sum2=0
                            for k in case:
                                sum2+=k*k
                            maxValue2=max(maxValue2,sum2)
                    answer=max(answer,maxValue1+maxValue2)
    print("#"+str(tc)+" "+str(answer))

