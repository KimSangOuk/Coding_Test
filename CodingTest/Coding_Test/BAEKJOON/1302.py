# 풀이시간 5분 시간제한 2초 메모리제한 128MB
# 1회차 정답
# dict으로 숫자를 세고 그걸 배열로 변경해서 담은 다음 각 기준에 따라 정렬하면 되는 문제이다.

n=int(input())
array=dict()
for i in range(n):
  k=input()
  if k in array:
    array[k]+=1
  else:
    array[k]=1

new=[]
for i in array:
  new.append((array[i],i))

new.sort(key=lambda x:(-x[0],x[1]))
print(new[0][1])