N=int(input())
ingredients=[]
k=list(map(int,input().split()))
for _ in range(N):
    ingredients.append(list(map(int,input().split())))

answer=1e9
answerList=[]
for i in range(1<<N):
    sumList=[0]*4
    cost=0
    numList=[]
    for j in range(N):
        if i&(1<<j):
            for t in range(4):
                sumList[t]+=ingredients[j][t]
            cost+=ingredients[j][4]
            numList.append(j+1)

    passed=True
    for t in range(4):
        if sumList[t]<k[t]:
            passed=False
            break
    if not passed:
        continue
    # print(cost,sumList,numList)
    if answer>cost:
        answer=cost
        answerList=[]
        answerList.append(" ".join(map(str,numList)))
    elif answer==cost:
        answerList.append(" ".join(map(str,numList)))
if len(answerList)==0:
    print(-1)
else:
    answerList.sort()
    print(answer)
    print(answerList[0])