import sys
sys.setrecursionlimit(10**5)

n,r,c=map(int,input().split())

x=0
y=0
k=2**n
start=nstart=0
end=nend=(2**n)*(2**n)
# print(2**512)
while True:
    if x==r and y==c:
        print(int(start))
        break
    k//=2
    if r<x+k and c<y+k:
        nend=start+(end-start)//4
    elif r<x+k and c>=y+k:
        y=y+k
        nstart=start+(end-start)//4
        nend=start+(end-start)//4*2

    elif r>=x+k and c<y+k:
        x=x+k
        nstart=start+(end-start)//4*2
        nend=start+(end-start)//4*3
        # print("3사분면",nstart,nend)
    elif r>=x+k and c>=y+k:
        x=x+k
        y=y+k
        nstart=start+(end-start)//4*3
        nend=start+(end-start)
        # print("4사분면",nstart,nend)
    start,end=nstart,nend