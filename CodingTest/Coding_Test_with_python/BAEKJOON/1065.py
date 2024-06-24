# 풀이시간 11분 시간제한 2초 메모리제한 128MB
# 1회차 정답
# 문제를 딱 보았을 때, 전체 수를 하나씩 짚어가면서 그 사이에 있는 수 하나하나를 분석하는데다가 그 수를 분석할 때도 각 자리수별로 다 조사하는 식의 전체를 탐색하는 완전탐색 알고리즘인걸 알 수 있었다. 또한 시간복잡도 또한 전체 최대 수가 1,000이하인데다가 자리수까지 for문으로 포함해도 *3까지이기 때문에 걱정할 필요가 없었다.
n=int(input())

count=0
for i in range(1,n+1):
  length=len(str(i))
  if length<3:
    count+=1
  else:
    for j in range(0,length-1):
      d=int(str(i)[0])-int(str(i)[1])
      if d!=(int(str(i)[j])-int(str(i)[j+1])):
        break
      elif j+1==length-1:
        count+=1
print(count)