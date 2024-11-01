def create_pi_table(pattern):
  table=[0 for _ in range(len(pattern))]
  i=0
  for j in range(1,len(pattern)):
      while i>0 and pattern[i]!=pattern[j]:
          i=table[i-1]
      if pattern[i]==pattern[j]:
          i+=1
          table[j]=i
  return table

def kmp(all_string,pattern):
  table=create_pi_table(pattern)

  i=0
  result=[]
  for j in range(len(all_string)):
      while i>0 and pattern[i]!=all_string[j]:
          i=table[i-1]
      if pattern[i]==all_string[j]:
          i+=1
          if i==len(pattern):
              result.append(j-i+2)
              i=table[i-1]
  return result

N,K=map(int,input().split())
programs=[]
programsToString=[]
for _ in range(N):
  mL=int(input())
  program=list(map(int,input().split()))
  programs.append(program)
  programsToString.append(" ".join(map(str,program)))

result=False
for i in range(0,len(programs[0])-K+1):
  pattern=programs[0][i:i+K]
  reversePattern=pattern[::-1]
  thisPatternIncluded=True
  for j in range(1,len(programs)):
      if len(kmp(programsToString[j]," ".join(map(str,pattern))))>0 or len(kmp(programsToString[j]," ".join(map(str,reversePattern)))):
          continue
      else:
          thisPatternIncluded=False
          break
  if thisPatternIncluded:
      result=True
      break
if result:
  print("YES")
else:
  print("NO")

