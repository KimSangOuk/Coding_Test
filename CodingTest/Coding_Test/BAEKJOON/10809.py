# 풀이시간 5분 시간제한 1초 메모리제한 256MB
# 1회차 정답
# 각 문자를 출력하돼 주어진 문자열에 포함되어 있으면 위치를 아니면 -1을 출력하는 문제이다. 그렇기 때문에 반복문으로 a~z까지 돌려주면서 포함되어 있으면 인덱스를 아니면 -1을 출력하면 된다.

s=list(input())

for i in range(0,ord('z')-ord('a')+1):
  if chr(ord('a')+i) in s:
    print(s.index(chr(ord('a')+i)),end=' ')
  else:
    print(-1,end=' ')