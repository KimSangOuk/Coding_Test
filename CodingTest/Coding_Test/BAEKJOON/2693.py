# 풀이시간 3분 시간제한 1초 메모리제한 32MB
# 1회차 정답
# 배열을 역순으로 정렬해서 그 중 3번째 수를 출력하면 되는 문제이다.

for tc in range(int(input())):
  array=list(map(int,input().split()))
  array.sort(reverse=True)
  print(array[2])