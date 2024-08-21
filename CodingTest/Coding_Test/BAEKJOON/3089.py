import bisect

n,m=map(int,input().split())
pos1=[]
pos2=[]
for _ in range(n):
    a,b=map(int,input().split())
    pos1.append((a,b))
    pos2.append((b,a))

opers=list(input())
pos1.sort()
pos2.sort()

x=0
y=0
for oper in opers:
    if 'U'==oper:
        index=bisect.bisect_left(pos1,(x,y+1))
        # print(pos1[index])
        x,y=pos1[index]
    if 'L'==oper:
        index=bisect.bisect_right(pos2,(y,x-1))
        # print(pos2[index-1][::-1])
        x,y=pos2[index-1][::-1]
    if 'R'==oper:
        index=bisect.bisect_left(pos2,(y,x+1))
        # print(pos2[index][::-1])
        x,y=pos2[index][::-1]
    if 'D'==oper:
        index=bisect.bisect_right(pos1,(x,y-1))
        # print(pos1[index-1])
        x,y=pos1[index-1]

print(x,y)        
