n,k=map(int,input().split())
arr_a=list(map(int,input().split())).sort()
arr_b=list(map(int,input().split())).sort(reverse=True)

for i in range(k):
  if arr_a[i]<arr_b[i]:
    arr_a[i],arr_b[i]=arr_b[i],arr_a[i]
  else:
    break

print(sum(arr_a))