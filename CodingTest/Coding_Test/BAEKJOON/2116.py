n=int(input())
dices=[]
diceConnect={0:5, 5:0, 1:3, 3:1, 2:4, 4:2}
for i in range(n):
    dices.append(list(map(int,input().split())))
answer=0

def sumWithout(j,a,b):
    v=0
    for i in range(6):
        if i==a or b==i:
            continue
        v=max(v,dices[j][i])
    return v

for i in range(6):
    down=i
    downNum=dices[0][i]
    sumValue=0
    for j in range(n):
        up=diceConnect[down]
        upNum=dices[j][up]
        sumValue+=sumWithout(j,down,up)
        if j!=n-1:
            down=dices[j+1].index(upNum)
    answer=max(sumValue,answer)
print(answer)