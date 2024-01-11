n=int(input())
m=int(input())

answer=[]

for i in range(1,10001):
  if n<=i*i<=m:
    answer.append(i*i)

if len(answer)==0:
  print(-1)
else:
  print(sum(answer))
  print(answer[0])