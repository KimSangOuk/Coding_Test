# 이것이 취업을 위한 코딩테스트다 part03 '19. 연산자 끼워넣기'와 동일

n=int(input())

num=list(map(int,input().split()))

code=list(map(int,input().split()))

max_answer=-int(1e9)
min_answer=int(1e9)

def dfs(result,deep):
  global max_answer,min_answer
  if deep==n:
    max_answer=max(result,max_answer)
    min_answer=min(result,min_answer)
  else:
    if code[0]>0:
      deep+=1
      code[0]-=1
      dfs(result+num[deep-1],deep)
      code[0]+=1
      deep-=1
    if code[1]>0:
      deep+=1
      code[1]-=1
      dfs(result-num[deep-1],deep)
      code[1]+=1
      deep-=1
    if code[2]>0:
      deep+=1
      code[2]-=1
      dfs(result*num[deep-1],deep)
      code[2]+=1
      deep-=1
    if code[3]>0:
      deep+=1
      code[3]-=1
      if result<0:
        result=-result 
        result=-(result//num[deep-1])
      else:
        result=result//num[deep-1]
      dfs(result,deep)
      code[3]+=1
      deep-=1

dfs(num[0],1)
print(max_answer)
print(min_answer)