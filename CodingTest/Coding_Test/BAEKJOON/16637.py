import sys
input=sys.stdin.readline

n=int(input())
expReal=list(map(str,list(input().strip())))
operNum=n//2
answer=-2**31

def dfs(k,visited):
    global answer
    exp=expReal[:]
    for i in range(len(exp)//2-1,-1,-1):
        if visited&(1<<i):
            exp[2*i:2*i+3]=[str(eval(exp[2*i]+exp[2*i+1]+exp[2*i+2]))]
    tmpAnswer=exp[0]
    for i in range(1,len(exp),2):
        tmpAnswer=eval(str(tmpAnswer)+exp[i]+exp[i+1])
    answer=max(int(tmpAnswer),answer)
    for i in range(k,operNum):
        if not visited&(1<<i):
            dfs(i+2,visited|(1<<i))

dfs(0,0)
print(answer)