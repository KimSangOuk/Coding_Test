# 풀이시간 5분 시간제한 1초 메모리제한 256MB
# 1회차 정답
# 각 합을 출력하는 구현 문제.

n=int(input())
for i in range(1,n+1):
  a,b=map(int,input().split())
  print("Case #"+str(i)+": "+str(a)+" + "+str(b)+" = "+str(a+b))