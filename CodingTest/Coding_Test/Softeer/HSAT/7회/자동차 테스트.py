import sys
from bisect import bisect_left,bisect_right
input=sys.stdin.readline

n,q=map(int,input().split())

cars=list(map(int,input().split()))
cars.sort()
carSet=set(cars)

for _ in range(q):
    m=int(input())
    if m not in carSet:
        print(0)
    elif m<=cars[0]:
        print(0)
    elif m>=cars[-1]:
        print(0)
    else:
        index=bisect_left(cars,m)
        # print(index)
        print(index*((n-1)-index))
