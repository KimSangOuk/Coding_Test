# 처음에는 while문을 써서 하나씩 계산할까 했지만 한꺼번에 수식으로 풀릴꺼 같아서 조건을 여러개 두면서 그리디 식으로 조건을 걸어 사용했다. 처음에 갯수가 패키지의 개수의 6개보다 많을 경우, 패키지의 가격 보다 낱개로 전부 사는게 더 싸다면 낱개로 사고 패키지를 섞어사는게 더 싸다면 패키지를 포함해서 사되 남은 낱개의 수를 사는 것이 싼지 아니면 패키지를 하나 더 사는게 싼지를 판단해서 계산에 포함시킨다. 6개보다 적은 경우도 마찬가지의 수를 고려해주면 된다.
# 풀이시간 : 15분
n,m=map(int,input().split())
package_min=int(1e9)
one_min=int(1e9)
for i in range(m):
    package,one=map(int,input().split())
    package_min=min(package,package_min)
    one_min=min(one,one_min)

total_price=0
if n>=6:
    num=n//6
    if package_min/6>one_min:
        total_price=one_min*n
    else:
        total_price=package_min*num
        if (n-6*num)*one_min<package_min:
            total_price+=one_min*(n-6*num)
        else:
            total_price+=package_min
else:
    if n*one_min<package_min:
        total_price+=one_min*n
    else:
        total_price+=package_min

print(total_price)