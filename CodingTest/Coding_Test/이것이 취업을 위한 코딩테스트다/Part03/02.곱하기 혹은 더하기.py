# 풀이 시간 - 14분/30분 시간제한 1초 메모리제한 128MB
# 1회차 정답
# 현 상태에서 0,1을 더하고 나머지는 곱하기로 빼서 쓰기 때문에 그리디 알고리즘

s=input()
result=int(s[0])
for i in range(1,len(s)):
  if int(s[i])==0 or int(s[i])==1 or result==0 or result==1:
    result+=int(s[i])
  else:
    result*=int(s[i])

print(result)

# 답안지
# data = input()

# # 첫 번째 문자를 숫자로 변경하여 대입
# result=int(data[0])
# for i in range(1,len(data)):
#   # 두 수 중에서 하나라도 '0' 혹은 '1'인 경우, 곱하기보다는 더하기 수행
#   num = int(data[i])
#   if num<=1 or result<=1:
#     result+=num
#   else:
#     result*=num

# print(result)