# 풀이시간 20분 시간제한 1초 메모리제한 128MB
# 1회차 정답
# 단순하게 모든 구현 과정을 일일이 설명해주는 걸 보고 구현문제임을 느꼈고, 재귀함수를 사용해야한다는 점을 강하게 느꼈다. 이미 문제에서도 재귀라는 표현을 사용하기도 하였다.
# 굳이 시간복잡도를 따지자면 문자열의 최대 길이가 1,000이기 때문에 O(N^2) 즉, 이중 포문 이상으로 안넘어가게 하는 것이 좋다.
# 풀이과정은 정답지와 유사하다.

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

# # 답안 예시
# # "균형잡힌 괄호 문자열"의 인덱스 반환
# def balanced_index(p):
#   count=0 # 왼쪽 괄호의 개수
#   for i in range(len(p)):
#     if p[i]=='(':
#       count+=1
#     else:
#       count-=1
#     if count==0:
#       return i

# # "올바른 괄호 문자열"인지 판단
# def check_proper(p):
#   count=0 # 왼쪽 괄호의 개수
#   for i in p:
#     if i=='(':
#       count+=1
#     else:
#       if count==0: # 쌍이 맞지 않는 경우에 False 반환
#         return False
#       count-=1
#   return True # 쌍이 맞는 경우에 True 반환
  
# def solution(p):
#   answer=''
#   if p=='':
#     return answer
#   index=balanced_index(p)
#   u=p[:index+1]
#   v=p[index+1:]
#   # "올바른 괄호 문자열"이면, v에 대해 함수를 수행한 결과를 붙여 반환
#   if check_proper(u):
#     answer = u + solution(v)
#   # "올바른 괄호 문자열"이 아니라면 아래의 과정을 수행
#   else:
#     answer='('
#     answer+=solution(v)
#     answer+=')'
#     u=list(u[1:-1])
#     for i in range(len(u)):
#       if u[i]=='(':
#         u[i]=')'
#       else:
#         u[i]='('
#     answer+="".join(u)
#   return answer