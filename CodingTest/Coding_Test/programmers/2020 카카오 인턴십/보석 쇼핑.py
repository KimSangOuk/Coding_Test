def solution(gems):
  answer = []

  start=0
  end=0

  types=set(gems)
  typesCnt=len(types)

  nowSet=set()
  nowSet.add(gems[end])
  minLength=len(gems)
  answer=[1,len(gems)]

  counter=dict()
  counter[gems[0]]=1

  while end<len(gems):
      if typesCnt>len(nowSet):
          end+=1
          if end==len(gems):
              break
          if gems[end] not in nowSet:
              counter[gems[end]]=1
              nowSet.add(gems[end])
          else:
              counter[gems[end]]+=1
      elif typesCnt<=len(nowSet):
          if typesCnt==len(nowSet):
              if minLength>(end-start+1):
                  answer=[start+1,end+1]
                  minLength=end-start+1
          prev=gems[start]
          start+=1
          if counter[prev]==1:
              del counter[prev]
              nowSet.remove(prev)
          else:
              counter[prev]-=1


  return answer