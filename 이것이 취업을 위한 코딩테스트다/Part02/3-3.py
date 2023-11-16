n,m=map(int,input().split())
answer=-1
for _ in range(n):
  k=list(map(int,input().split()))
  mid=min(k)
  if answer<mid:
    answer=mid
  # answer=max(mid,answer)

print(answer)