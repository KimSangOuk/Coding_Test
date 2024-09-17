def binary_search(rules,target,start,end):
  while start<=end:
      mid=(start+end)//2
      cnt=0
      for i in range(k):
          a,b,c=rules[i]
          if mid<a:
              continue
          elif mid>b:
              cnt+=(b-a)//c+1
          else:
              cnt+=(mid-a)//c+1
      if cnt<target:
          start=mid+1
      else:
          answer=mid
          end=mid-1
  return answer


n,k,d=map(int,input().split())
rules=[]
start=1000000
end=0
for _ in range(k):
  a,b,c=map(int,input().split())
  start=min(a,start)
  end=max(b,end)
  rules.append((a,b,c))

print(binary_search(rules,d,start,end))