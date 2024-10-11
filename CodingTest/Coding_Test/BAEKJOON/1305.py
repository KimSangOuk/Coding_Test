def create_psl(pattern):
  i=0
  table=[0]*len(pattern)
  for j in range(1,len(pattern)):
      while i>0 and pattern[i]!=pattern[j]:
          i=table[i-1]
      if pattern[i]==pattern[j]:
          i+=1
          table[j]=i
  return table

l=int(input())
s=input()

table=create_psl(s)
print(l-table[l-1])