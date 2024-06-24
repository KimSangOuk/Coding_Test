# 풀이시간 10분 시간제한 1초 메모리제한 64MB
# 1회차 정답
# 동전 문제처럼 각 단위가 배수의 관계를 이루기 때문에 큰 단위부터 차례차례 나누어가면 되는 그리디 문제이다.

t=int(input())

btns=[300,60,10]
count=[0]*3

for i in range(3):
  count[i]=t//btns[i]
  t%=btns[i]

if t!=0:
  print(-1)
else:
  for i in range(3):
    print(count[i],end=' ')