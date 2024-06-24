def solution(N, stages):
  answer = []
  stages.sort()
  count=[0]*(N+1)
  for i in range(len(stages)):
      if stages[i]<=N:
          count[stages[i]]+=1

  length=len(stages)

  fail=[]
  for i in range(1,N+1):
      if length>0:
          value=count[i]/length
          fail.append((value,i))
          length-=count[i]
      else:
          fail.append((0,i))

  fail.sort(key=lambda x:(-x[0],x[1]))
  for i in range(0,N):
      answer.append(fail[i][1])

  return answer