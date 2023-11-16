a,b=map(int,input().split())
print(not ((bool(a) and not bool(b)) or (not bool(b) and bool(a))))