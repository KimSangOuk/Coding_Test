# 풀이시간 10분 시간제한 2초 메모리제한 4MB
# 1회차 정답
# 단순하게 전체수를 탐색하면서 조건에 맞아떨어지는 경우까지가 어떤 수인지 탐색하는 완전탐색 문제이다.

e,s,m=map(int,input().split())

a,b,c=0,0,0
y=0
while True:
  if e==(a+y)%15+1 and s==(b+y)%28+1 and m==(c+y)%19+1:
    break
  y+=1
print(y+1)