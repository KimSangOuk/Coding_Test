from itertools import product

def solution(n, info):
    answer = []
    answerList=[]
    maxDiffScore=0

    cases=list(product(range(0,2),repeat=11))
    for case in cases:
        lionScore=0
        appeachScore=0
        lionShot=n
        caseTf=True
        caseResult=[]
        for i in range(11):
            if case[i]==1:
                if lionShot>info[i]:
                    lionShot-=info[i]+1
                    lionScore+=(10-i)
                    caseResult.append(info[i]+1)
                else:
                    caseTf=False
                    break
            else:
                if info[i]>0:
                    appeachScore+=(10-i)
                caseResult.append(0)
        if caseTf and lionScore>appeachScore:
            index=10
            while lionShot>0:
                if case[index]==1:
                    lionShot-=1
                    caseResult[index]+=1
                else:
                    if info[i]>caseResult[i]+1:
                        lionShot-=1
                        caseResult[i]+=1
                    else:
                        index-=1
            if maxDiffScore<abs(lionScore-appeachScore):
                maxDiffScore=abs(lionScore-appeachScore)
                answerList=[caseResult]
            elif maxDiffScore==abs(lionScore-appeachScore):
                answerList.append(caseResult)

    if maxDiffScore==0:
        return [-1]

    strList=[]
    for k in answerList:
        t=""
        for i in range(11):
           t=t+str(k[i])
        strList.append(t[::-1])
    strList.sort(reverse=True)
    for i in strList[0][::-1]:
        answer.append(int(i))

    return answer