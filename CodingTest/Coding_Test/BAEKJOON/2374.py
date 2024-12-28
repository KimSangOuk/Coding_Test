import sys

input=sys.stdin.readline

n=int(input())

arr=list()
for i in range(n):
    arr.append(int(input()))

answer=0

while True:
    smallestConnectedGroup=[0]
    smallestNum=arr[0]
    for i in range(1,n):
        if smallestNum>arr[i]:
            smallestNum=arr[i]
            smallestConnectedGroup=[i]
        elif smallestNum==arr[i] and smallestConnectedGroup[-1]+1==i:
            smallestConnectedGroup.append(i)
        elif smallestNum==arr[i] and smallestConnectedGroup[-1]+1!=i:
            smallestConnectedGroup=[i]
    if len(smallestConnectedGroup)==n:
        break

    left=smallestConnectedGroup[0]-1
    right=smallestConnectedGroup[-1]+1
    nextNum=-1
    if left==-1 or right==n:
        if left==-1:
            nextNum=arr[right]
        else:
            nextNum=arr[left]
    else:
        nextNum=min(arr[right],arr[left])
    answer+=(nextNum-smallestNum)
    for k in smallestConnectedGroup:
        arr[k]=nextNum

print(answer)