n=int(input())
a=map(int,input().split())
list=[0]*23
for i in a:
  list[i-1]+=1

for k in list:
  print(k,end=' ')