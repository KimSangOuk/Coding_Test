# 풀이시간 5분 시간제한 1초 메모리제한 256MB
# 1회차 정답
# 입력받은 수의 합을 출력하는 문제.

n=int(input())
num=list(str(input()))

answer=0
for i in range(n):
  answer+=int(num[i])

print(answer)