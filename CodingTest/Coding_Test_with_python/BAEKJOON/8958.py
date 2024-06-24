# 풀이시간 5분 시간제한 1초 메모리제한 128MB
# 1회차 정답
# 케이스마다 문자열을 받아서 O일 때는 스택을 증가시키며 더하고 X일 때는 스택을 초기화 시키면 된다.

for tc in range(int(input())):
  answer=0
  stack=1
  s=list(input())
  for i in s:
      if i=='O':
          answer+=stack
          stack+=1
      else:
          stack=1
  print(answer)