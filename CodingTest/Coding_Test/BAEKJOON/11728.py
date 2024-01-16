# 풀이시간 3분 시간제한 1.5초 메모리제한 256MB
# 1회차 정답
# 배열을 합쳐서 정렬하면 되는 문제.

n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=a+b
c.sort()
for i in range(len(c)):
  print(c[i],end=' ')