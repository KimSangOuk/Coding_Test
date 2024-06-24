# 풀이시간 1분 시간제한 1초 메모리제한 512MB
# 1회차 정답
# @구현

a,b=map(int,input().split())
if a>b:
  print('>')
elif a<b:
  print('<')
else:
  print('==')