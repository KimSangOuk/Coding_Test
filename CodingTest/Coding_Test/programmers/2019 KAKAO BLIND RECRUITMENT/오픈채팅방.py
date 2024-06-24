# 아이디랑 닉네임 부분만 변경될 것을 염두해두고 따로 딕테이션으로 처리한 후 출력할 때만 인지시키면 된다.
# 풀이시간 : 10분

def solution(record):
  answer = []
  name_data=dict()
  for t in record:
      arr=list(t.split())
      if arr[0]=='Enter':
          name_data[arr[1]]=arr[2]
          answer.append((0,arr[1]))
      elif arr[0]=='Leave':
          answer.append((1,arr[1]))
      else:
          name_data[arr[1]]=arr[2]
  for k in range(len(answer)):
      if answer[k][0]==0:
          answer[k]=name_data[answer[k][1]]+"님이 들어왔습니다."
      elif answer[k][0]==1:
          answer[k]=name_data[answer[k][1]]+"님이 나갔습니다."


  return answer