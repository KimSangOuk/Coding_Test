# 풀이시간 35분 시간제한 2초 메모리제한 128MB
# 1회차 정답
# 숫자를 묶거나 더했을 때 최댓값이 되도록 하는 문제이다. 이 때, 양수의 경우는 큰 수씩 묶어 곱한다음 더해가면 되는데 이 때, 한수가 1일 경우 더해주면 된다. 음수의 경우는 똑같이 작은 순대로 묶어서 곱하여 양수로 만들면 최댓값이 나오는데 이 때 남는 수가 1개일때, 이 수를 제거할 0이 있으면 묶어서 음수를 없애주고 없다면 그대로 더해주면 된다. 이렇게 모든 경우를 따져서 문제를 풀어주면 된다.

n=int(input())
plus_array=[]
minus_array=[]
have_0=0

for _ in range(n):
  k=int(input())
  if k==0:
    have_0+=1
  elif k>0:
    plus_array.append(k)
  else:
    minus_array.append(k)

plus_array.sort(reverse=True)
minus_array.sort()

plus_max_value=0
index=0
while index<len(plus_array):
  first=index
  second=index+1
  if first<len(plus_array) and second<len(plus_array):
    if plus_array[first]==1 or plus_array[second]==1:
      plus_max_value+=plus_array[first]+plus_array[second]
    else:
      plus_max_value+=plus_array[first]*plus_array[second]
    index+=2
  else:
    plus_max_value+=plus_array[first]
    index+=1

minus_max_value=0
index=0
while index<len(minus_array):
  first=index
  second=index+1
  if first<len(minus_array) and second<len(minus_array):
    minus_max_value+=minus_array[first]*minus_array[second]
    index+=2
  else:
    if have_0==0:
      minus_max_value+=minus_array[first]
    index+=1

print(plus_max_value+minus_max_value)