# 이것이 취업을 위한 코딩테스트다 part03 '03. 문자열 뒤집기'와 동일

count=[0,0]

s=input()
first=int(s[0])
count[first]=1
for i in range(1,len(s)):
  data=int(s[i])
  if data!=first:
    if data==0:
      count[0]+=1
    else:
      count[1]+=1
  first=data
print(min(count))