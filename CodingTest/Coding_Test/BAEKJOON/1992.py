n=int(input())
arr=[list(map(int,list(input()))) for _ in range(n)]

def func(x,y,l):
    if l==1:
        if arr[x][y]==1:
            return 1
        else:
            return 0
    k=l//2
    ul=func(x,y,k)
    ur=func(x,y+k,k)
    dl=func(x+k,y,k)
    dr=func(x+k,y+k,k)
    if ul==ur and ur==dl and dl==dr and (dl==1 or dl==0):
        if ul==1:
            return 1
        else:
            return 0
    return "("+str(ul)+str(ur)+str(dl)+str(dr)+")"

print(func(0,0,n))