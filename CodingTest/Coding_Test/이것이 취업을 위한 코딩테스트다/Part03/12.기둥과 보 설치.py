# 풀이시간 25분/50분 시간제한 5초 메모리제한 128MB
# 3회차 풀이
# 각 블록을 설치하거나 제거하고 그 목록이 가능한 목록인지만 확인해주면 되는 문제이다. 가능한지는 좌표에 따라 다른 좌표가 존재하거나 하면 되는지 확인해주면 된다. 대표적인 시뮬레이션 유형이다.

def check(frames):
  for frame in frames:
    x,y,a=frame
    if a==0:
      if y==0 or [x,y-1,0] in frames or [x,y,1] in frames or [x-1,y,1] in frames:
        continue
      else:
        return False
    else:
      if [x,y-1,0] in frames or [x+1,y-1,0] in frames or ([x-1,y,1] in frames and [x+1,y,1] in frames):
        continue
      else:
        return False
  return True

def solution(n, build_frame):
  answer = []

  for frame in build_frame:
    x,y,a,b=frame
    # 삭제
    if b==0:
      answer.remove([x,y,a])
    # 설치
    else:
      answer.append([x,y,a])

    # 검사
    if check(answer):
      continue

    # 실패 시 다시 설치, 삭제
    if b==0: # 설치
      answer.append([x,y,a])
    else: # 삭제
      answer.remove([x,y,a])
    
  answer.sort()
  return answer


first_case=[[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]
print(solution(5,first_case))
print()
second_case=[[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]
print(solution(5,second_case))

# 2회차 풀이
# 풀이시간 1시간 30분/50분
# 1회차 정답 - 풀이시간 초과, 알고리즘 복잡(정답은 맞음)
# 딱히 시간제한이 없는 문제인 것을 일단 간과했다. in을 쓰려고 하다가 in에서 들어가는 1,000 블록을 전부 탐색하는 1,000 또 맞는지 전부 확인하는 1,000 해서 N^3의 복잡도가 나오기 때문에 말이 안된다고 생각했다.
# 근데 딱히 시간제한이 없었다.
# 먼저 시간이 오래 걸린 부분은 문제를 풀 때, 빠트린 부분이 컸다. 한 지점에 두 개의 시작점이 올 수 있다는 점을 까먹고 풀었다가 다시 고치느라 오래 걸렸다.
# 그리고 in을 쓰지 않다보니 더 추가적으로 쓰는 배열을 두어서 시간이 오래걸렸다.
# 먼저 첫번재 잘못은 시간제한을 확인하지 않은 나의 잘못이다. 시간제한을 먼저 확인했어야했다. 요즘 급하게 풀다보니 오히려 시간제한을 확인하지 않는 습관이 생기면서, 1초로 그냥 생각하고 푸는 경향이 있는데 이런 문제도 존재한다는 것을 인지했으니, 다음부터는 시간제한이 몇 초지 있는지 없는지 부터 확인해보자. 그렇게 된다면 in을 사용하기도 하고 배열도 따로 두지 않게 되어 더 짧게 풀었을 것이다.
# 두번째 잘못은 한 지점에 시작이 두개 온다는 것을 간과한건데, 간과하게 된 이유는 이차원 배열을 둘 때, 보통 한 자리에 하나의 것이 온다는 인식이 보통이었다고 생각한다. 보통 다른 '뱀'같은 문제에서 하나의 자리에 하나가 오는 것이 보통이기 때문에 이게 습관으로 굳어져서 확인도 안하고 선 접근했던 것 같다. 그렇게 때문에 만약 이차원 배열이 온다면 하나의 자리에 두가지 상태가 존재할 수 있는지 확인해볼 수 있다.
# 그래도 나름 풀이 속도도 빨라지고 풀이도 점점 간단해지고 있는게 느껴진다.
# def check_right(answer,bo,gi):
#   for block in answer:
#     x,y,a=block
#     if a==0:
#       if y==0 or (bo[x][y] or bo[x-1][y]) or (gi[x][y-1]):
#         gi[x][y]=True
#       else:
#         return False
#     elif a==1:
#       if (gi[x][y-1] or gi[x+1][y-1]) or (bo[x-1][y] and bo[x+1][y]):
#         bo[x][y]=True
#       else:
#         return False
#   return True
    

# def solution(n, build_frame):
#   answer = []
#   bo=[[False]*(n+1) for _ in range(n+1)]
#   gi=[[False]*(n+1) for _ in range(n+1)]

#   for block in build_frame:
#     x,y,a,b=block
#     if b==1:
#       answer.append([x,y,a])
#       if a==0:
#         gi[x][y]=True
#       else:
#         bo[x][y]=True
#     else:
#       answer.remove([x,y,a])
#       if a==0:
#         gi[x][y]=False
#       else:
#         bo[x][y]=False

#     if check_right(answer,bo,gi):
#       continue
#     else:
#       if b==1:
#         answer.remove([x,y,a])
#         if a==0:
#           gi[x][y]=False
#         else:
#           bo[x][y]=False
#       else:
#         answer.append([x,y,a])
#         if a==0:
#           gi[x][y]=True
#         else:
#           bo[x][y]=True
#   answer.sort()
#   return answer

# first_case=[[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]
# print(solution(5,first_case))
# print()
# second_case=[[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]
# print(solution(5,second_case))


# 풀이 시간 - 1시간 30분/50분 시간제한 5초 메모리제한 128MB
# 1회차 오답 - 풀이시간 초과, 알고리즘 복잡(정답은 맞음)
# 내가 짠 코드에서 줄일 수 있는 부분 - 애초에 block을 빼고 넣었으면 각 설치 함수의 제거하는 블록을 있는지 확인하는 부분을 없애고 제거 확인 함수에서도 똑같이 포함하는지 확인하는 부분을 없앨 수 있다.
# 일단 벽을 받아서 그 벽마다 추가하고 삭제하는 작업을 하면 되기 때문에 for문으로 벽마다 작업하는데 1,000 이하 이기 때문에 O(N^2) 까지 가능하다고 보았다.
# 시뮬레이션 문제인 것은 문제에서 주어지기도 했고 순차적으로 조건을 코드로 풀어서 쓰는 유형이었다.
# 일단 알고리즘이 너무 복잡한데다가 그러다 보니 시간이 길어지고 오류가 발생시에도 코드를 뒤지느라 한나절 걸렸다.

# # 1회차 풀이
# # 먼저 '자물쇠와 열쇠'문제에서 한번 느껴듯이 넣었다가 빼는 아이디어를 떠올리긴 했으나 삭제부분에서 구현 중에 떠올렸다. 또한 삭제와 추가의 경우는 다른식으로 구현아이디어를 떠올리다보니 생각하지 못한 점도 있다. 그래서 추가의 조건을 삭제에 이용하긴 했으나 반대로 통일된 환경을 만들고 이를 추가하고 빼는 방법까지는 떠올리지 못했다. '자물쇠와 열쇠'의 경우에는 해보고 안되면 제거하는 경우였는데 이도 똑같이 해보고 안되면 말고라는 경우를 생각해서 풀었어야 했다. 그래서 통일 조건을 세운다음 만들고 이에 따라 추가와 삭제를 구현했다면 정답지와 유사해졌을 것이다.
# # 전체알고리즘에서의 문제는 위와 같고 좌표로 구했을 때의 복잡함에 대해서도 문제이다. 좌표로 구하는 것이 예전부터 습관이 되어있어서 좌표와 관련되면 무조건 좌표를 x,y에 대해 찍고 보는 습관이 있다. 하지만 이번 문제와 같이 좌표단위로 보기보다는 큰 단위로 본다면 훨씬 식이 단순해진다는 점을 알았다. 최대한 큰 단위로 나눠서 단순화 시킬 수 있는지를 확인하는 버릇을 들여야겠다.
# from itertools import combinations
# import copy

# # 이 함수와 밑에 있는 보 함수는 통일하에 작성될 수 있으며 식이 길어져서 나누어 놓았지만 이 두식을 통일해서 하나로 썼다면 더 간단해졌을 것이다.
# # 결국 이 근본은 길어서 길게 쓴 것인데 이는 위에서 언급했다 싶이 점단위로 보아서 코드가 길어진 이유가 크다. 코드가 짧았다면 체크하는 함수를 합쳤을 가능성 + 해보고 안되면 취소하는 식의 알고리즘 두가지를 생각했으면 되었다.
# def install_check_pillar(installed,case):
#   for block in installed:
#     if block==case:
#       continue
#     if block[2]==0:
#       if block[0]==case[0] and (block[1]+1)==case[1]:
#         #print("기둥이 다른 기둥 위에 있음",case)
#         return True
#     elif block[2]==1:
#       if (block[0]==case[0] and block[1]==case[1]) or ((block[0]+1)==case[0] and block[1]==case[1]):
#         #print("기둥이 다른 보 위에 있음",case)
#         return True
#   if case[1]==0:
#     #print("기둥이 바닥 위에 있음")
#     return True
#   return False

# def install_check_bo(installed,case):
#   installed_bo=[]
#   for block in installed:
#     if block==case:
#       continue
#     if block[2]==0:
#       if (block[0]==case[0] and (block[1]+1)==case[1]) or ((block[0]==(case[0]+1)) and ((block[1]+1)==case[1])):
#         #print("보가 기둥 위에 있음")
#         return True
#     elif block[2]==1:
#       installed_bo.append(block)
#   new_arr=list(combinations(installed_bo,2))
#   for bo1,bo2 in new_arr:
#     if ((bo1[0]+1)==case[0] and bo1[1]==case[1] and bo2[0]==(case[0]+1) and bo2[1]==case[1]) or ((bo2[0]+1)==case[0] and bo2[1]==case[1] and bo1[0]==(case[0]+1) and bo1[1]==case[1]):
#       #print("보가 다른 보의 양쪽에 연결되어 있음")
#       return True
#   return False

# # 이 함수를 고치면서 '뺐네 다시 더하면 되는거 아닌가' 까지 생각했으나 추가 함수해서 '더한다음에 안되면 빼지'는 생각하지 못했다. 동일상황을 만드려고 버릇을 만들어야한다.
# def check_delete_pillar_bo(answer,case):
#   new_answer=copy.deepcopy(answer)
#   new_answer.remove(case)
#   # 여기 부분에서 헷깔림. 나머지 블록들이 되는지 확인하는 건데, case로 받아온 블록을 확인함.
#   for block in answer:
#     if block!=case:
#       if block[2]==0:
#         if not install_check_pillar(new_answer,block):
#           #print("삭제 실패 사유 : 다른 기둥이 조건이 안맞음",block)
#           return False
#       elif block[2]==1:
#         if not install_check_bo(new_answer,block):
#           #print("삭제 실패 사유 : 다른 보가 조건이 안맞음",block)
#           return False
#   return True

# def solution(n, build_frame):

#   answer=[]
#   for case in build_frame:
#     now_block=[case[0],case[1],case[2]]
#     # 삭제 시
#     if case[3]==0:
#       # 삭제되어있는거 제외, 나머지 것들이 기준들을 전부 만족하는지 확인
#       if check_delete_pillar_bo(answer,[case[0],case[1],case[2]]):
#         # 전부 충족 시 삭제
#         answer.remove([case[0],case[1],case[2]])
#         print("삭제:",now_block)
#     # 설치 시
#     elif case[3]==1:
#       # 기둥 설치 시 조건 확인
#       if case[2]==0:
#         # 기둥 바닥 위, 보의 한쪽 끝, 다른 기둥 위
#         if install_check_pillar(answer,[case[0],case[1],case[2]]):
#           # 조건이 맞을 시 설치
#           answer.append([case[0],case[1],case[2]])
#           #print("설치:",now_block)
#       # 보 설치 시 조건 확인
#       elif case[2]==1:
#         # 한쪽 끝부분이 기둥 위, 양쪽 끝부분 보랑 연결
#         if install_check_bo(answer,[case[0],case[1],case[2]]):
#           # 조건이 맞을 시 설치
#           answer.append([case[0],case[1],case[2]])
#           #print("설치:",now_block)
        
#   # answer=[[]]
#   # 정답을 정렬
#   answer.sort()
#   return answer

# first_case=[[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]
# print(solution(5,first_case))
# print()
# second_case=[[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]
# print(solution(5,second_case))

# # 답안지
# # 현재 설치된 구조물이 '가능한' 구조물인지 확인하는 함수
# def possible(answer):
#   for x,y,stuff in answer:
#     if stuff==0: # 설치된 것이 '기둥'인 경우
#       # '바닥 위' 혹은 '보의 한쪽 끝부분 위' 혹은 '다른 기둥 위'라면 정상
#       if y==0 or [x-1,y,1] in answer or [x,y,1] in answer or [x,y-1,0] in answer:
#         continue
#       return False # 아니라면 거짓(False) 반환
#     elif stuff==1: # 설치된 것이 '보'인 경우
#       # '한쪽 끝부분이 기둥 위' 혹은 '양쪽 끝부분인 다른 보와 동시에 연결'이라면 정상
#       if [x,y-1,0] in answer or [x+1,y-1,0] in answer or ([x-1,y-1] in answer and [x+1],y,1 in answer):
#         continue
#       return False # 아니라면 거짓(False) 반환
#   return True

# def solution(n, build_frame):
#   answer=[]
#   for frame in build_frame: # 작업의 개수는 최대 1,000개
#     x,y,stuff,operate=frame
#     if operate==0: # 삭제하는 경우
#       answer.remove([x,y,stuff]) # 일단 삭제를 해본 뒤에
#       if not possible(answer): # 가능한 구조물인지 확인
#         answer.append([x,y,stuff]) # 가능한 구조물이 아니라면 다시 설치
#     elif operate==1: # 설치하는 경우
#       answer.append([x,y,stuff]) # 일단 설치를 해본 뒤에
#       if not possible(answer): # 가능한 구조물인지 확인
#         answer.remove([x,y,stuff]) # 가능한 구조물이 아니라면 다시 제거
#   return sorted(answer) # 정렬된 결과를 반환