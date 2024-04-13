# 풀이시간 20분
# 1회차 정답

def solution(survey, choices):
  answer = ''
  scores=dict()
  scores['R']=0
  scores['T']=0
  scores['C']=0
  scores['F']=0
  scores['J']=0
  scores['M']=0
  scores['A']=0
  scores['N']=0
  n=len(survey)
  for i in range(n):
      q=survey[i]
      if choices[i]<4:
          scores[q[0]]+=abs(choices[i]-4)
      else:
          scores[q[1]]+=abs(choices[i]-4)

  rt='R' if scores['R']>=scores['T'] else 'T'
  cf='C' if scores['C']>=scores['F'] else 'F'
  jm='J' if scores['J']>=scores['M'] else 'M'
  an='A' if scores['A']>=scores['N'] else 'N'
  answer=rt+cf+jm+an

  return answer