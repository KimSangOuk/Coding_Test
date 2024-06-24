# 풀이시간 5분 시간제한 1초 메모리제한 256MB
# 1회차 정답
# 각 횟수를 수의 범위가 크기 때문에 dict으로 세고 그 것을 배열로 변환하여 저장한 다음 횟수가 많고 수가 작은 순으로 정렬한 다음 맨 앞에 있는 숫자를 출력하면 된다.

n=int(input())
arr=dict()
for _ in range(n):
  k=int(input())
  if k in arr:
    arr[k]+=1
  else:
    arr[k]=1

new=[]
for key in arr.keys():
  new.append((key,arr[key]))

new.sort(key=lambda x:(-x[1],x[0]))
print(new[0][0])