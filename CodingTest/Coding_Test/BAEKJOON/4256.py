import sys
from collections import deque
input=sys.stdin.readline

def makeTree(rootV,rootI,start,end):
    global preorder, inorder
    if start>end:
        return False
    rootIndex=-1
    root=-1
    for i in range(start,end+1):
        if inorder[i]==preorder[0]:
            rootIndex=i
            root=preorder.popleft()
            break
    left=makeTree(root,rootIndex,start,rootIndex-1)
    right=makeTree(root,rootIndex,rootIndex+1,end)
    if left:
        graph[root].append((0,left))
    if right:
        graph[root].append((1,right))
    return root

def printPostOrder(tree,root):
    if len(graph[root])==0:
        print(root,end=' ')
        return
    for i in range(len(tree[root])):
        printPostOrder(tree,tree[root][i][1])
    print(root,end=' ')

for tc in range(1,int(input())+1):
    n=int(input())
    preorder=deque(list(map(int,input().split())))
    k=preorder[0]
    inorder=list(map(int,input().split()))
    graph=[[] for _ in range(n+1)]

    makeTree(0,0,0,n-1)
    printPostOrder(graph,k)
    print()