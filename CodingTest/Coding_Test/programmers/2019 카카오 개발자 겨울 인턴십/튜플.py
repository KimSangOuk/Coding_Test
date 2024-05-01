# 처음에 입력 형식을 제대로 보지 않아서 문자열로 주어진 점을 놓쳤다. 집합 형태로 주어졌다고 생각하고 풀다가 답이 안나와서 보니 문자열이었다.
# 문자열을 split(), 와 map()으로 풀어서 리스트로 다시 담은 후 풀이를 하였다. 주어진 입력 형식에서 숫자의 갯수가 전체의 정답으로 구할 리스트의 길이와 같고 갯수가 늘어날 수록 구할 리스트의 순서를 반영하기 때문에 dict()을 사용해서 길이별로 구별하였다. 그 후, 짧은 순으로 새롭게 들어있는 숫자만 정답에 순서대로 포함시키도록 하였다.
# 풀이시간 : 25분
# 1회차 정답

def solution(s):
  answer = []
  
  s=s[1:-1]
  s=s[1:-1].split('},{')
  new_s=list()
  for i in s:
      new_s.append(list(map(int,i.split(','))))
  
  sort_by_len=dict()
  total_len=len(list(new_s))
  for arr in list(new_s):
      arr_len=len(arr)
      sort_by_len[arr_len]=list(arr)
  
  for i in range(1,total_len+1):
      for j in sort_by_len[i]:
          if j not in answer:
              answer.append(j)
  
  return answer