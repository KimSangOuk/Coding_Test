# 풀이시간 13분
# 1회차 정답
# 파이썬에 문자열 교체 기능이 있다는 사실을 기억하고 있어서 전부 다른 문자열 이고 중복되는 경우가 없기에 찾아서 숫자 문자로 바꾸면 된다고 생각했다. 출력값이 정수형을 원하고 있기 때문에 전환하여 출력했다.

def solution(s):
  answer = ''
  n=len(s)
  self_dict=dict()
  self_dict['zero']='0'
  self_dict['one']='1'
  self_dict['two']='2'
  self_dict['three']='3'
  self_dict['four']='4'
  self_dict['five']='5'
  self_dict['six']='6'
  self_dict['seven']='7'
  self_dict['eight']='8'
  self_dict['nine']='9'
  for key in self_dict.keys():
      s=s.replace(key,self_dict[key])
  answer=int(s)

  return answer