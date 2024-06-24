def solution(answers):
  answer = []
  a=[1,2,3,4,5]
  b=[2,1,2,3,2,4,2,5]
  c=[3,3,1,1,2,2,4,4,5,5]
  method=[a,b,c]
  score=[0,0,0]
  for i in range(len(answers)):
      for j in range(3):
          if answers[i]==method[j][i%len(method[j])]:
              score[j]+=1
  max_value=max(score)
  for i in range(len(score)):
      if score[i]==max_value:
          answer.append(i+1)
  return answer