# 풀이 시간 - 30분 시간제한 1초 메모리제한 128MB
# 1회차 정답
# n이 5000보다 작거나 같기 떄문에 딱봐도 O(nlogn)이하의 알고리즘으로 풀어야겠다 생각이 듬
# 딱 봤을 때, 5의 개수가 그냥 판도를 내린다 싶어서 5의 개수를 통해 나누면서 개수를 줄여감으로써 현재 상황에서 최소의 개수를 구하는 그리디 알고리즘으로 품.

n=int(input())

max_5=n//5
result=-1

if n%5==0:
  result=max_5
else:
  for i in range(max_5,-1,-1):
    result=i
    remain=n-(5*i)
    if remain%3==0:
      result+=remain//3
      break
    result=-1

print(result)