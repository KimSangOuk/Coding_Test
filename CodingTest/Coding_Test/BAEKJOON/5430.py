from collections import deque

t=int(input())

def func(opers,n,arr):
    flag=0
    for oper in opers:
        if oper=='D':
            if len(arr)==0:
                return 'error'
            if flag==0:
                arr.popleft()
            else:
                arr.pop()
        else:
            if flag==0:
                flag=1
            else:
                flag=0
    return list(arr) if flag==0 else list(arr)[::-1]


for _ in range(t):
    p=list(input())
    n=int(input())
    inputArr=input()[1:-1]
    arr=[]
    if len(inputArr)==0:
        arr=[]
    else:
        arr=list(inputArr.split(','))
    result=func(p,n,deque(arr))
    if result=='error':
        print(result)
    else:
        answer="["
        if len(result)>0:
            for k in result:
                answer+=k
                answer+=","
            answer=answer[:-1]+"]"
        else:
            answer+="]"
        print(answer)