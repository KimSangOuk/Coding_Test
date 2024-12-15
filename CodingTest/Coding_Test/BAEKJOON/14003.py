from bisect import bisect_left

def lis(arr):
    tails=[]
    tails_idx=[]
    prev_idx=[-1]*n

    for i in range(len(arr)):
        num=arr[i]
        pos=bisect_left(tails,num)
        if pos==len(tails):
            tails.append(num)
            tails_idx.append(i)
        else:
            tails[pos]=num
            tails_idx[pos]=i

        if pos>0:
            prev_idx[i]=tails_idx[pos-1]

    max_length=len(tails)

    list_lis=[]
    k=tails_idx[-1] if tails_idx else -1
    while k!=-1:
        list_lis.append(arr[k])
        k=prev_idx[k]
    list_lis.reverse()
    return max_length,list_lis

n=int(input())
arr=list(map(int,input().split()))
max_length,list_lis=lis(arr)
print(max_length)
print(*list_lis)