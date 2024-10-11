def create_PSL(pattern):
  i=0
  table=[0 for _ in range(len(pattern))]
  for j in range(1,len(pattern)):
      while i>0 and pattern[i]!=pattern[j]:
          i=table[i-1]
      if pattern[i]==pattern[j]:
          i+=1
          table[j]=i
  return table

s=input()
answer=0
for i in range(len(s)):
  answer=max(answer,max(create_PSL(s[i:])))
print(answer)