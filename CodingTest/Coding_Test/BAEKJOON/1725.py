import sys
sys.setrecursionlimit(10**5)

N=int(input())

arr=[]
for _ in range(N):
    arr.append(int(input()))

tree=[0]*(4*N)

def build_segment_tree(tree,arr,node,start,end):
    if start==end:
        tree[node]=(arr[start],start)
    else:
        mid=(start+end)//2
        build_segment_tree(tree,arr,node*2,start,mid)
        build_segment_tree(tree,arr,node*2+1,mid+1,end)
        tree[node]=min(tree[node*2],tree[node*2+1])

def range_query(tree,node,start,end,L,R):
    if R<start or L>end:
        return (1e9,1e9)
    elif L<=start and end<=R:
        return tree[node]
    else:
        mid=(start+end)//2
        left_min=range_query(tree,node*2,start,mid,L,R)
        right_min=range_query(tree,node*2+1,mid+1,end,L,R)
        return min(left_min,right_min)

def getSize(tree,left,right):
    minH,minIdx=range_query(tree,1,0,N-1,left,right)

    nSize=(right-left+1)*minH

    if left<minIdx:
        nSize=max(getSize(tree,left,minIdx-1),nSize)
    if minIdx<right:
        nSize=max(getSize(tree,minIdx+1,right),nSize)
    return nSize

build_segment_tree(tree,arr,1,0,N-1)
print(getSize(tree,0,N-1))
