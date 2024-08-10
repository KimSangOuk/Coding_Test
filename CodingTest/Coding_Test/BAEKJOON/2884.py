h,m=map(int,input().split())

if m>=45:
    m-=45
else:
    m=60-(45-m)
    if h>0:
        h-=1
    else:
        h=23

print(h,m)