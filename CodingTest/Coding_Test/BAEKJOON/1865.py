import sys
input=sys.stdin.readline

INF=int(1e9)

def bellmanford(start):
    distance[start]=0
    for i in range(n):
        for edge in edges:
            s,e,v=edge
            if distance[s]+v<distance[e]:
                distance[e]=distance[s]+v
                if i==n-1:
                    return True
    return False

for _ in range(int(input())):
    n,m,w=map(int,input().split())
    edges=[]
    for _ in range(m):
        s,e,t=map(int,input().split())
        edges.append((s,e,t))
        edges.append((e,s,t))
    for _ in range(w):
        s,e,t=map(int,input().split())
        edges.append((s,e,-t))

    distance=[INF]*(n+1)
    if bellmanford(1):
        print("YES")
    else:
        print("NO")