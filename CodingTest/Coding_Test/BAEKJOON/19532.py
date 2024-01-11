# 풀이시간 10분 시간제한 1초 메모리제한 1024MB
# 1회차 정답
# 각 방정식에 맞는 수를 찾기 위해 두 수의 모든 범위를 탐색하는 브루트 포스 알고리즘 문제이다.

a,b,c,d,e,f=map(int,input().split())

for i in range(-999,1000):
  for j in range(-999,1000):
    if a*i+b*j==c and d*i+e*j==f:
      print(i,j)
      exit()