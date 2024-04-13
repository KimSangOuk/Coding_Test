# 풀이시간 30분
# 1회차 정답
# 이진수를 다루는게 거의 처음이라 그 부분에서 애먹었다. 먼저 주어진 10진수 자체를 가지고 비트 연산을 수행한 후, 이를 bin을 통해 이진수 형태로 바꾸고 zfill을 통해 자리수를 채워넣는다. 그리고 이 수에서 빈칸과 벽을 각 #과 공백으로 바꾸어넣으면 된다.

def solution(n, arr1, arr2):
  answer = []
  
  for i in range(n):
      answer.append(bin(arr1[i]|arr2[i])[2:].zfill(n).replace('1','#').replace('0',' '))
  
  return answer