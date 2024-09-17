k=int(input())
paper=[[0]*2 for _ in range(2)]
opers=list(input().split())
h=int(input())

paper[h//2][h%2]=1

for oper in opers[::-1]:
    if oper=='R' or oper=='L':
        paperReverse=[[0]*len(paper[0]) for _ in range(len(paper))]
        for i in range(len(paper)):
            for j in range(len(paper[0])):
                paperReverse[i][len(paper[0])-1-j]=paper[i][j]
        if oper=='R':
            for i in range(len(paper)):
                paper[i]=paperReverse[i]+paper[i]
        else:
            for i in range(len(paper)):
                paper[i]+=paperReverse[i]
    else:
        paperReverse=[[0]*len(paper[0]) for _ in range(len(paper))]
        for i in range(len(paper)):
            for j in range(len(paper[0])):
                paperReverse[len(paper)-1-i][j]=paper[i][j]
        if oper=='U':
            paper+=paperReverse
        else:
            paper=paperReverse+paper

for i in range(0,2**k*2,2):
    for j in range(0,2**k*2,2):
        if paper[i][j]==1:
            print(0,end=' ')
        elif paper[i][j+1]==1:
            print(1,end=' ')
        elif paper[i+1][j]==1:
            print(2,end=' ')
        elif paper[i+1][j+1]==1:
            print(3,end=' ')
    print()