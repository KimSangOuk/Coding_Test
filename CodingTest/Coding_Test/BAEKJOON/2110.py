# 이것이 취업을 위한 코딩테스트다 part03 '29. 공유기 설치'와 동일

import sys

n,c=map(int,input().split())
arr=[]
for _ in range(n):
  arr.append(int(sys.stdin.readline()))

arr.sort()

start=1
end=arr[-1]-arr[0]
answer=0
while start<=end:
  mid=(start+end)//2
  #print("mid",mid)
  # 갯수를 구해
  value=1
  s=0
  for i in range(len(arr)-1):
    if arr[i+1]-arr[i]>=mid:
  #    print(arr[i],arr[i+1])
      value+=1
      s=0
    else:
      s+=arr[i+1]-arr[i]
  #    print("s 누적량",s)
      if s>=mid:
        s=0
        value+=1
  # print("value",value)

  # 구한 갯수가 너무 많거나 같아
  if value>=c:
    answer=mid
    start=mid+1
  else:
    end=mid-1

print(answer)