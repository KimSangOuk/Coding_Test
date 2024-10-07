n=int(input())
arr=[]
for i in range(n):
    arr.append(input())

answerMaxLength=0
answerTwoWord=[]
for i in range(n):
    for j in range(i+1,n):
        s1=arr[i]
        s2=arr[j]
        minL=min(len(s1),len(s2))
        maxL=0
        length=0
        for k in range(minL):
            if s1[k]!=s2[k]:
                maxL=max(maxL,length)
                break
            else:
                length+=1
        if length==minL:
            maxL=max(maxL,length)
        if answerMaxLength<maxL:
            answerTwoWord=[s1,s2]
            answerMaxLength=maxL
for i in range(2):
    print(answerTwoWord[i])