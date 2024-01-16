# 풀이시간 5분 시간제한 1초 메모리제한 256MB
# 1회차 정답
# 단어의 시작 인덱스를 순차적으로 늘려가면서 모든 단어를 배열에 넣은 후 정렬한 후 출력하면 되는 문제이다.

s=input()
length=len(s)

array=[]
for i in range(0,length):
  array.append(s[i:])

array.sort()

for i in range(len(array)):
  print(array[i])