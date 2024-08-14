import math

def isPrimeNum(num):
    for i in range(2,int(math.sqrt(num))+1):
        if num%i==0:
            return False
    return True

def dfs(deep,s):
    global answer
    if not isPrimeNum(int(s)):
        return
    if deep==n-1:
        answer.append(s)
    for i in range(1,10):
        dfs(deep+1,s+str(i))

answer=[]
n=int(input())
for i in range(2,10):
    dfs(0,str(i))

for a in answer:
    print(a)