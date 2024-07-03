for tc in range(1,int(input())+1):
  arr=list(map(int,input().split()))
  answer=0
  for i in arr:
      if i%2==1:
          answer+=i
  print("#"+str(tc)+" "+str(answer))