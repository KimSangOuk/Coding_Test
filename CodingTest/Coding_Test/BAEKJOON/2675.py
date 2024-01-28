# 풀이시간 5분 시간제한 1초 메모리제한 128MB
# 1회차 정답
# 문자열을 받아서 그 문자를 주어진 횟수만큼 반복해 나가면서 더해주면 되는 문제이다.

for tc in range(int(input())):
  r,s=map(str,input().split())
  r=int(r)
  answer=""
  for i in s:
      answer+=r*i
  print(answer)
