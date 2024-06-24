# 백준 2470과 동일한 문제임 - 주어진 리스트가 정렬되었는지 안되었는지만 다름

def binary_search(array,fix,start,end):
  min_value=2000000000
  result=0
  while start<=end:
    mid=(start+end)//2
    if abs(array[mid]+fix)<min_value:
      min_value=abs(array[mid]+fix)
      result=array[mid]
    if array[mid]<=-fix:
      start=mid+1
    else:
      end=mid-1
  return min_value,result

n=int(input())
array=list(map(int,input().split()))

array.sort()

answer=[]
for i in range(len(array)):
  min_value,match_x=binary_search(array,array[i],i+1,len(array)-1)
  answer.append((min_value,array[i],match_x))

answer.sort()
# print(answer)
print(answer[0][1],answer[0][2])