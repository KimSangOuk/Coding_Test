dp=[]
dp.append(6)
dp.append(14)
M=int(input())
while True:
    k=dp[-2]+dp[-1]
    dp.append(k)
    if k>M:
        break

messi=["Messi ","Messi Gimossi "]

if M<=14:
    index=1
else:
    index=len(dp)-1
front=index-1
back=index-2
wordIndex=M

while True:
    if index==0 or index==1:
        answer=messi[1][wordIndex-1]
        if answer==" ":
            print("Messi Messi Gimossi")
        else:
            print(answer)
        break
    if wordIndex>dp[front]:
        index=back
        wordIndex-=dp[front]
    else:
        index=front
    front=index-1
    back=index-2
