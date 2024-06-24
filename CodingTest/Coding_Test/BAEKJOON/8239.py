# 풀이시간 5분 시간제한 1초 메모리제한 128MB
# 1회차 정답
# 단순히 현재 수까지의 합을 출력하는 문제.

answer=0
for i in range(int(input())+1):
  answer+=i
print(answer)