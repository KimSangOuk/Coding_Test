# 풀이 시간 - 5분/20분 시간제한 1초 메모리제한 256MB
# 1회차 정답
# n의 숫자의 크기가 크지만 결국 길이를 이용하여 푸는 문제이고 조건을 그대로 구현하라고 되어있었기 때문에 그냥 구현 문제라고 생각해서 풀었음. 아마 구현중 시뮬레이션에 해당 될 것이라고 생각됨.

left_sum=0
right_sum=0

num=input()
length=len(num)
half=length//2
for i in range(0,half):
  left_sum+=int(num[i])

for i in range(half,length):
  right_sum+=int(num[i])

if left_sum==right_sum:
  print("LUCKY")
else:
  print("READY")

# # 답안지
# n = input()
# length=len(n)
# summary=0

# # 왼쪽 부분의 자릿수 합 더하기
# for i in range(0,length//2):
#   summary+=int(n[i])

# # 오른쪽 부분의 자릿수 합 빼기
# for i in range(length//2,length):
#   summary-=int(n[i])
  
# # 왼쪽 부분과 오른쪽 부분의 자릿수 합이 동일한지 검사
# if summary==0:
#   print("LUCKY")
# else:
#   print("READY")