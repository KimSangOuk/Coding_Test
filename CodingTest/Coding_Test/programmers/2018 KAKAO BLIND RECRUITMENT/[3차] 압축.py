# - 앞에서부터 문자열을 늘려가면서 현재 사전에 있는 가장 긴 길이까지 늘리고 그 길이를 출력하고 그 다음 문자가 있다면 그 다음 문자까지를 포함해서 사전에 기록하는 식의 문제이다. 앞에서부터 기준을 잡고 index를 while문을 통해 둔 다음, 길이를 늘려가면서 만약 존재하지 않는다면 그 전까지는 존재하기 때문에 answer배열에 사전번호를 담아 정답을 기록하고 그 다음문자열을 사전에 기록하였다.
# - 끝부분에 관한 처리를 추가로 하였는데 늘리다가 결국 존재하는 경우에는 단순히 정답에 담고 종료하고 마지막 문자가 시작지점이 되는 부분일 경우에는, 마지막 문자의 사전 번호를 담아 출력하였다.
# - 풀이시간 : 50분

def solution(msg):
  answer = []
  my_dict=dict()
  find_set=set()
  for i in range(0,26):
      my_dict[chr(ord('A')+i)]=i+1
      find_set.add(chr(ord('A')+i))
  last_index=26
  i=0
  while i<len(msg):
      if i==len(msg)-1:
          answer.append(my_dict[msg[-1]])
          break
      for j in range(i+1,len(msg)+1):
          s=msg[i:j]
          if s not in find_set:
              answer.append(my_dict[msg[i:j-1]])
              i+=j-1-i
              last_index+=1
              my_dict[s]=last_index
              find_set.add(s)
              break
          elif s in find_set and j==len(msg):
              answer.append(my_dict[s])
              return answer

  return answer