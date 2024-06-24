# 풀이시간 30분
# 1회차 정답
# 문자열을 처음부터 순서대로 풀어해치려고 하다가 숫자 10을 처리하기가 복잡해서 다트 단위로 한번 끊고 계산을 하기로 했다. 숫자의 진입을 기준으로 다트별로 끊고 다트별로 계산하는데 숫자->S,D,T->#,* 순서로 오기때문에 숫자를 받고 그것으로 바로 계산을 해도 문제가 없었다. 구한 점수들을 각 더해주면 답이 나온다.

def solution(dartResult):
  answer = 0

  n=len(dartResult)
  now=0

  dart_score=[0,0,0]

  dart=[]
  for i in range(n-1):
      if not dartResult[i].isdigit() and dartResult[i+1].isdigit():
          dart.append(dartResult[now:i+1])
          now=i+1
  dart.append(dartResult[now:])

  for i in range(3):
      num=''
      for j in range(len(dart[i])):
          if dart[i][j].isdigit():   
              num+=dart[i][j]
          elif dart[i][j]=='S':
              dart_score[i]=int(num)
          elif dart[i][j]=='D':
              dart_score[i]=int(num)*int(num)
          elif dart[i][j]=='T':
              dart_score[i]=int(num)*int(num)*int(num)
          elif dart[i][j]=='#':
              dart_score[i]=-dart_score[i]
          elif dart[i][j]=='*':
              if i==0:
                  dart_score[i]=2*dart_score[i]
              else:
                  dart_score[i]=2*dart_score[i]
                  dart_score[i-1]=2*dart_score[i-1]

  answer=sum(dart_score)    
  return answer