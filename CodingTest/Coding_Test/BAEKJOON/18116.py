import sys
input=sys.stdin.readline

def find_parent(parent,x):
    if parent[x]!=x:
        parent[x]=find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
    global cnt
    a=find_parent(parent,a)
    b=find_parent(parent,b)
    if a==b:
        return
    if a<b:
        parent[b]=a
        cnt[a]+=cnt[b]
        cnt[b]=0
    else:
        parent[a]=b
        cnt[b]+=cnt[a]
        cnt[a]=0

parent=dict()
cnt=dict()
n=int(input())
for _ in range(n):
    oper=list(map(str,input().split()))
    if oper[0]=='I':
        if oper[1] not in parent:
            parent[oper[1]]=oper[1]
            cnt[oper[1]]=1
        if oper[2] not in parent:
            parent[oper[2]]=oper[2]
            cnt[oper[2]]=1
        union_parent(parent,oper[1],oper[2])
    else:
        if oper[1] not in parent:
            parent[oper[1]]=oper[1]
            cnt[oper[1]]=1
        print(cnt[find_parent(parent,oper[1])])
