# 풀이시간 15분 시간제한 1초 메모리제한 256MB
# 1회차 정답
# 3의 배수인 경우 각 자리 수의 합이 3의 배수가 되는 것을 이용하는 문제이다. 그렇기 때문에 그 중 우리는 가장 큰 숫자가 필요하기 때문에 받아온 숫자를 역으로 정렬시키면 된다. 그 정렬한 숫자의 각 자릿수가 3의 배수인지 그리고 30의 배수이기 때문에 0을하나 포함하고 있는지 확인하면 된다.

s=list(input())
array=[]
all_add=0
for i in range(len(s)):
  array.append(int(s[i]))

array.sort(reverse=True)

result=''
for i in range(len(array)):
  result+=str(array[i])

if sum(array)%3==0 and array[-1]==0:
  print(int(result))
else:
  print(-1)