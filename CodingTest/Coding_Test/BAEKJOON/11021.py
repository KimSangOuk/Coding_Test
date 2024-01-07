# 풀이시간 5분 시간제한 1초 메모리제한 256MB
# 1회차 정답
# 합을 출력하는 간단한 구현 문제.

for tc in range(1,int(input())+1):
  a,b=map(int,input().split())
  print("Case #"+str(tc)+": "+str(a+b))