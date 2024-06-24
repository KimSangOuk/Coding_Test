# 풀이시간 30분
# 1회차 정답
# 조건이 까다로운 구현 문제인듯 하다. 친구들의 모든 기록을 한번 정리를 해야 첫번째 조건을 도달할 수 있고 또 선물지수를 구하기 위한 총 갯수를 한번 더 정리해야 두번째 조건에 도달할 수 있다. 마지막으로 두 조건을 만족시키면서 다음달에 받을 선물을 구하면서 최대값을 구해주면 된다.

def solution(friends, gifts):
  result = dict()
  history=dict()
  answer=dict()
  for friend_name in friends:
      history[friend_name]=dict()
      answer[friend_name]=0
      result[friend_name]=dict()
      result[friend_name]['give']=0
      result[friend_name]['get']=0
      result[friend_name]['value']=0
      for k in friends:
          if k!=friend_name:
              history[friend_name][k]=0
  
  for k in gifts:
      a,b=k.split()
      history[a][b]+=1
      result[a]['give']+=1
      result[b]['get']+=1
  
  for friend_name in friends:
      result[friend_name]['value']=result[friend_name]['give']-result[friend_name]['get']
  
  num=len(friends)
  for i in range(num):
      for j in range(i+1,num):
          a=friends[i]
          b=friends[j]
          if (history[a][b]!=0 or history[b][a]!=0) and history[a][b]!=history[b][a]:
              if history[a][b]>history[b][a]:
                  answer[a]+=1
              else:
                  answer[b]+=1
          else:
              if result[a]['value']==result[b]['value']:
                  continue
              if result[a]['value']>result[b]['value']:
                  answer[a]+=1
              else:
                  answer[b]+=1
  
  t=0
  
  for i in range(num):
      t=max(t,answer[friends[i]])

return t