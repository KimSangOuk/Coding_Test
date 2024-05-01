# 풀이시간 20분
# 1회차 정답
# 신고한 사람과 신고받은 사람을 받아서 표를 그대로 딕테이션으로 만들었고 또한 횟수또한 필요하기 때문에 이에 관련해서도 딕테이션으로 나타냈다. 이를 통해 정지당한 사람을 구하고 정지당한 사람이 신고한 사람의 신고받은 사람 목록에서 몇명이나 있는지 반복문으로 찾았다.

def solution(id_list, report, k):
  answer = []
  
  reported=[] 
  
  reported_num_dict=dict()
  
  dict_report=dict()
  for id in id_list:
      dict_report[id]=[]
      reported_num_dict[id]=0
  
  for s in report:
      a,b=s.split()
      if b not in dict_report[a]:
          dict_report[a].append(b)
          reported_num_dict[b]+=1
  
  for id in id_list:
      if reported_num_dict[id]>=k:
          reported.append(id)
  
  for id in id_list:
      cnt=0
      for n in dict_report[id]:
          if n in reported:
              cnt+=1
      answer.append(cnt)
  
  return answer