def dfs(total,now):
  global answer
  if total>=b:
      answer=min(answer,total-b)
  else:
      for i in range(now+1,n):
          dfs(total+arr[i],i)

for tc in range(int(input())):
  n,b=map(int,input().split())
  arr=list(map(int,input().split()))
  arr.sort()
  answer=sum(arr)
  for i in range(len(arr)):
      total=arr[i]
      dfs(total,i)

  print("#"+str(tc+1)+" "+str(answer))