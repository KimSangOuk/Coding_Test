badukpan=[[0]*19 for _ in range(19)]
n=int(input())
for _ in range(n):
  a,b=map(int,input().split())
  badukpan[a-1][b-1]=1

for y in range(19):
  for x in range(19):
    print(badukpan[y][x],end=" ")
  print('\n')