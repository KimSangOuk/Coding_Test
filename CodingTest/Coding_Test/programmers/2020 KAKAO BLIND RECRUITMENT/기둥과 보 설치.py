# 이것이 취업을 위한 코딩테스트다 part03 '12. 기둥과 보 설치'와 동일

def check_right(answer,bo,gi):
  for block in answer:
    x,y,a=block
    if a==0:
      if y==0 or (bo[x][y] or bo[x-1][y]) or (gi[x][y-1]):
        gi[x][y]=True
      else:
        return False
    elif a==1:
      if (gi[x][y-1] or gi[x+1][y-1]) or (bo[x-1][y] and bo[x+1][y]):
        bo[x][y]=True
      else:
        return False
  return True


def solution(n, build_frame):
  answer = []
  bo=[[False]*(n+1) for _ in range(n+1)]
  gi=[[False]*(n+1) for _ in range(n+1)]

  for block in build_frame:
    x,y,a,b=block
    if b==1:
      answer.append([x,y,a])
      if a==0:
        gi[x][y]=True
      else:
        bo[x][y]=True
    else:
      answer.remove([x,y,a])
      if a==0:
        gi[x][y]=False
      else:
        bo[x][y]=False

    if check_right(answer,bo,gi):
      continue
    else:
      if b==1:
        answer.remove([x,y,a])
        if a==0:
          gi[x][y]=False
        else:
          bo[x][y]=False
      else:
        answer.append([x,y,a])
        if a==0:
          gi[x][y]=True
        else:
          bo[x][y]=True
  answer.sort()
  return answer