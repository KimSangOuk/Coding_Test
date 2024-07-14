t=int(input())

for tc in range(t):
    n=int(input())

    answer=0
    for i in range(1,n):
        k=5**i
        if k>n:
            break
        else:
            answer+=n//k
    print(answer)