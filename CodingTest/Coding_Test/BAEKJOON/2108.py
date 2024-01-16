# 풀이시간 15분 시간제한 2초 메모리제한 256MB
# 1회차 정답
# 배열을 정렬하고 횟수를 카운트해서 각 조건대로 출력하면 되는 문제이다.

n=int(input())
array=[]
count=[0]*8001
for _ in range(n):
  k=int(input())
  count[k+4000]+=1
  array.append(k)

max_value=0
value=[]
for i in range(len(count)):
  if max_value<count[i]:
    max_value=count[i]
    value=[]
    value.append(i-4000)
  elif max_value==count[i]:
    value.append(i-4000)

# print(value)
array.sort()
value.sort()
print(round(sum(array) / n))
print(array[n//2])
if len(value)>=2:
  print(value[1])
else:
  print(value[0])
print(array[-1]-array[0])