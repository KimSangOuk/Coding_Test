for tc in range(1,int(input())+1):
  stack=0
  total=0
  max_now=0
  n=int(input())
  arr=list(map(int,input().split()))
  for i in range(n-1,-1,-1):
      if max_now<arr[i]:
          total+=max_now*stack
          stack=0
          max_now=arr[i]
      else:
          stack+=1
          total-=arr[i]
  if stack>0:
      total+=stack*max_now
  print("#"+str(tc)+" "+str(total))