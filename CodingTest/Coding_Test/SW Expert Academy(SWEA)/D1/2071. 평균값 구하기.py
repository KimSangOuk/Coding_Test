for tc in range(1,int(input())+1):
  arr=list(map(int,input().split()))
  answer=0
  for i in arr:
      answer+=i
  print("#"+str(tc)+" "+str(round(answer/10)))