dx=[-1,0,1,0]
dy=[0,1,0,-1]

x,y,d=0,0,1
l=int(input())
n=int(input())

opers=[list(input().split()) for _ in range(n)]

totalT=0
traces=[]

def isCrushed(tx1,ty1,tx2,ty2,x1,y1,x2,y2):
    if tx1>tx2 and ty1==ty2:
        if y1==y2 and y1==ty1:
            if tx1>=x1>=tx2 or tx1>x2>tx2:
                return True
        elif x1==x2 and y1>y2:
            if y1>=ty1>=y2 and tx1>=x1>=tx2:
                return True
        elif x1==x2 and y1<y2:
            if y2>=ty1>=y1 and tx1>=x1>=tx2:
                return True
    elif tx1<tx2 and ty1==ty2:
        if y1==y2 and y1==ty1:
            if tx1<=x1<=tx2 or tx1<=x2<=tx2:
                return True
        elif x1==x2 and y1>y2:
            if y1>=ty1>=y2 and tx2>=x1>=tx1:
                return True
        elif x1==x2 and y1<y2:
            if y2>=ty1>=y1 and tx2>=x1>=tx1:
                return True
    elif tx1==tx2 and ty1>ty2:
        if x1>x2 and y1==y2:
            if x1>=tx1>=x2 and ty1>=y1>=ty2:
                return True
        elif x1<x2 and y1==y2:
            if x2>=tx1>=x1 and ty1>=y1>=ty2:
                return True
        elif x1==x2 and x1==tx1:
            if ty1>=y1>=ty2 or ty1>=y2>=ty2:
                return True
    elif tx1==tx2 and ty1<ty2:
        if x1>x2 and y1==y2:
            if x1>=tx1>=x2 and ty2>=y1>=ty1:
                return True
        elif x1<x2 and y1==y2:
            if x2>=tx1>=x1 and ty2>=y1>=ty1:
                return True
        elif x1==x2 and x1==tx1:
            if ty1<=y1<=ty2 or ty1<=y2<=ty2:
                return True
    return False

allClear=False
for i in range(n):
    t,dir=int(opers[i][0]),opers[i][1]
    nx=x+dx[d]*t
    ny=y+dy[d]*t

    checked=False
    dist=1e9
    for x1,y1,x2,y2 in traces:
        if isCrushed(x1,y1,x2,y2,x+dx[d],y+dy[d],nx,ny):
            if d==0 or d==2:
                dist=min(dist,abs(x-x1))
            else:
                dist=min(dist,abs(y-y1))
            checked=True
    if checked:
        totalT+=dist
        allClear=True
        break

    if nx<-l or ny<-l or nx>l or ny>l:
        dist=0
        if d==0:
            dist=abs(-l-x)
        if d==1:
            dist=abs(l-y)
        if d==2:
            dist=abs(l-x)
        if d==3:
            dist=abs(-l-y)
        totalT+=dist+1
        allClear=True
        break

    traces.append((x,y,nx,ny))
    x,y=nx,ny
    if dir=='L':
        d=(d+1)%4
    else:
        d=(d-1)%4
    totalT+=t
if allClear:
    print(totalT)
else:
    checked=False
    dist=1e9
    nx,ny=x,y
    if d==0:
        nx=-l
    elif d==1:
        ny=l
    elif d==2:
        nx=l
    elif d==3:
        ny=-l
    for x1,y1,x2,y2 in traces:
        if isCrushed(x1,y1,x2,y2,x+dx[d],y+dy[d],nx,ny):
            if d==0 or d==2:
                dist=min(dist,abs(x-x1))
            else:
                dist=min(dist,abs(y-y1))
            checked=True
    if checked:
        totalT+=dist
        allClear=True
        print(totalT)
    else:
        dist=0
        if d==0:
            dist=abs(-l-x)
        if d==1:
            dist=abs(l-y)
        if d==2:
            dist=abs(l-x)
        if d==3:
            dist=abs(-l-y)
        totalT+=dist+1
        print(totalT)

