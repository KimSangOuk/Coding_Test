# 풀이시간 5분 시간제한 1초 메모리제한 512MB
# 1회차 정답
# 입력받은 좌표가 어느 사분면에 속하는지 출력하는 구현 문제.

x=int(input())
y=int(input())
if x>0 and y>0:
  print(1)
elif x<0 and y>0:
  print(2)
elif x<0 and y<0:
  print(3)
elif x>0 and y<0:
  print(4)