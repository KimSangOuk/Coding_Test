# 이것이 취업을 위한 코딩테스트다 part03 '18. 괄호 변환'과 동일

def solution(p):
  answer = ''

  # 입력이 빈 문자열인 경우, 빈 문자열을 반환합니다.
  if len(p) == 0:
    return p

  # 문자열 w를 두 "균형잡힌괄호 문자열" u, v로 분리합니다.
  u=''
  v=''
  count=0
  right=True
  for i in p:
    if i=='(':
      count+=1
      u+=i
    else:
      count-=1
      if count<0:
        right=False
      u+=i
    if count==0:
      v=p[len(u):]
      break
  # 문자열 u가 "올바른 괄호 문자열"이라면 문자열 v에 대해 1단계부터 다시 수행합니다.
  if right:
    u+=solution(v)
    return u
  # 문자열 u가 올바른 괄호 문자열"이 아니라면 아래 과정을 수행합니다.
  else:
    answer+='('
    answer+=solution(v)
    answer+=')'
    u=u[1:len(u)-1]
    new_u=''
    for i in u:
      if i=='(':
        new_u+=')'
      else:
        new_u+='('
    answer+=new_u
  return answer

print(solution("(()())()"))
print(solution(")("))
print(solution("()))((()"))