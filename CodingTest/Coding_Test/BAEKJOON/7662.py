import heapq

for tc in range(int(input())):
    n=int(input())
    qMin=[]
    qMax=[]
    numDict=dict()
    for _ in range(n):
        oper,num=map(str,input().split())
        # print(oper,num)
        if oper=='I':
            heapq.heappush(qMin,int(num))
            heapq.heappush(qMax,-int(num))
            if num not in numDict:
                numDict[num]=0
            numDict[num]+=1
        elif oper=='D':
            if int(num)==-1:
                while qMin and (str(qMin[0]) not in numDict or numDict[str(qMin[0])]<=0):
                    heapq.heappop(qMin)
                if qMin:
                    minValue=heapq.heappop(qMin)
                    numDict[str(minValue)]-=1
                    if numDict[str(minValue)]<=0:
                        del numDict[str(minValue)]
            else:
                while qMax and (str(-qMax[0]) not in numDict or numDict[str(-qMax[0])]<=0):
                    heapq.heappop(qMax)
                if qMax:
                    maxValue=-heapq.heappop(qMax)
                    numDict[str(maxValue)]-=1
                    if numDict[str(maxValue)]<=0:
                        del numDict[str(maxValue)]
        # print(numDict)

    if len(numDict.keys())==0:
        print("EMPTY")
    else:
        print(max(map(int,numDict.keys())),min(map(int,numDict.keys())))