arr=[7,5,9,0,3,1,6,2,4,8]

for i in range(len(arr)):
  min_index=i # 가장 작은 원소의 인덱스
  for j in range(i+1,len(arr)):
    if arr[min_index]>arr[j]:
      min_index=j
  arr[min_index],arr[i]=arr[i],arr[min_index] # 스와프

print(arr)