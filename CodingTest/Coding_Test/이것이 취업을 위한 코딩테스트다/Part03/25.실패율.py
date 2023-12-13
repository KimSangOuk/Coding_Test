# 풀이시간 20분 시간제한 1초 메모리제한 128MB
# 1회차 정답
# 처음 주어진 배열의 길이가 200,000이기 때문에 O(NlogN) 이상을 사용하면 안되겠다고 생각하고 있었음. 그래서 sort() 함수를 사용함.
# 정렬을 하고 각 갯수를 구해서 해를 구한 후 다시 조건에 맞게 정렬하면 된다고 생각함.

import math

def solution(N, stages):
  answer = []
  stages.sort()
  now=stages[0]
  arr=[]
  count=0
  length=len(stages)
  for i in range(1,N+1):
    count=stages.count(i)

    if count==0 or length==0:
      value=0
    else:
      value=count/length
    arr.append((i,value))
    
    # print(i,count/length)
    length-=count
    
  arr.sort(key=lambda x:(-x[1],x[0]))
  for i in arr:
    answer.append(i[0])
  return answer

n=5
stages=[2,1,2,6,2,4,3,3]
print(solution(n,stages))
n=4
stages=[4,4,4,4,4]
print(solution(n,stages))

# 답안 예시
def solution(N, stages):
  answer=[]
  length=len(stages)

  # 스테이지 번호를 1부터 N까지 증가시키며
  for i in range(1,N+1):
    # 해당 스테이지에 머물러 있는 사람의 수 계산
    count = stages.count(i)

    # 실패율 계산
    if length==0:
      fail=0
    else:
      fail=count/length

    # 리스트에 (스테이지 번호, 실패율) 원소 삽입
    answer.append((i,fail))
    length-=count

  # 실패율을 기준으로 각 스테이지를 내림차순 정렬
  answer=sorted(answer,key=lambda t:t[1],reverse=True)

  # 정렬된 스테이지 번호 출력
  answer = [i[0] for i in answer]
  return answer