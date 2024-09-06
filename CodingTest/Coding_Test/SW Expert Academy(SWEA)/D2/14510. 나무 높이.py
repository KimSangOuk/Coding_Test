for tc in range(1,int(input())+1):
  answer=0
  N=int(input())
  arr=list(map(int,input().split()))
  maxH=max(arr)
  needed=dict()
  needed[1]=0
  needed[2]=0
  for i in range(N):
      k=maxH-arr[i]
      needed[2]+=k//2
      needed[1]+=k%2
  minTwo=min(needed[1],needed[2])
  answer=minTwo*2
  needed[2]-=minTwo
  needed[1]-=minTwo
  if needed[1]>0:
      answer+=needed[1]*2-1
  else:
      t=needed[2]*2
      if t%3==0:
          answer+=t//3*2
      else:
          answer+=t//3*2+t%3

  print("#"+str(tc)+" "+str(answer))