t=int(input())

arr=[]

for _ in range(t):
    s=input()
    stack=0
    left=0
    right=len(s)-1
    answer=0
    while left<=right:
        if s[left]==s[right]:
            left+=1
            right-=1
        else:
            if s[left+1:right+1]==s[left+1:right+1][::-1] or s[left:right]==s[left:right][::-1]:
                answer=1
            else:
                answer=2
            break
    print(answer)
