# 풀이시간 3분 시간제한 1초 메모리제한 128MB
# 1회차 정답
# 5개 수를 받아서 평균과 정렬했을 때, 중앙값을 출력하는 문제이다.

array=[]
for i in range(5):
  array.append(int(input()))
print(sum(array)//5)
array.sort()
print(array[2])