# 풀이시간 5분 시간제한 1초 메모리제한 128MB
# 1회차 정답
# 입력받은 숫자 3개의 곱을 구한 다음 그 수를 문자열로 변환하여 count에 갯수를 기록하여 count를 전부 출력하면 된다.

a=int(input())
b=int(input())
c=int(input())

mul=a*b*c
count=[0]*(10)

for c in str(mul):
  count[int(c)]+=1

for i in range(0,10):
  print(count[i])