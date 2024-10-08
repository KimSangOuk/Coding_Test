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

  # kmp
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

s=input()
t=input()
result=kmp(s,t)
print(len(result))
print(*result)