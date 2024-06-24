baduckpan=[]
for _ in range(19):
  row=list(map(int,input().split()))
  baduckpan.append(row)

n=int(input())
for _ in range(n):
  x,y=map(int,input().split())
  for i in range(19):
    if baduckpan[i][x-1]==0:
      baduckpan[i][x-1]=1
    elif baduckpan[i][x-1]==1:
      baduckpan[i][x-1]=0
    if baduckpan[y-1][i]==0:
      baduckpan[y-1][i]=1
    elif baduckpan[y-1][i]==1:
      baduckpan[y-1][i]=0

for y in range(19):
  for x in range(19):
    print(baduckpan[y][x],end=' ')
  print("\n")