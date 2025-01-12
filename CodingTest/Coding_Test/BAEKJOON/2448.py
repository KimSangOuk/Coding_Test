import sys
input=sys.stdin.readline

N=int(input())

stars=['  *  '," * * ","*****"]

def recur(k,starsNext):
    if k==N:
        for i in range(len(starsNext)):
            print(starsNext[i])
        return
    else:
        new_stars=[]
        for i in range(len(starsNext)):
            new_stars.append(" "*k+starsNext[i]+" "*k)
        for i in range(len(starsNext)):
            new_stars.append(starsNext[i]+" "+starsNext[i])
        recur(k*2,new_stars)

recur(3,stars)    