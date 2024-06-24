def solution(numbers):
  answer = []
  arr=list()
  for i in range(len(numbers)-1):
      for j in range(i+1,len(numbers)):
          arr.append(numbers[i]+numbers[j])
  answer=sorted(list(set(arr)))
  return answer