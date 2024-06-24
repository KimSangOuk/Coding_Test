# 진수로 바꾸는 과정은 단순 나누기와 나머지 연산을 통해 진행하였다. 이 코드는 SSAFY 12기 준비 중 연습 문제로 코드 트리에서 충분히 풀어봤기에 빠르게 작성할 수 있었다. 다음은 하나씩 0을 제외한 연속된 숫자를 찾아서 소수인지 판별하는 구간이였다. 연속된 숫자를 찾는것은 어렵지 않았으나 소수를 처음 구하는 알고리즘을 사용하였을 때, 현 숫자까지 모든 숫자로 나누어지는지 확인하다보니 O(N)이 나왔다. 전체 최대 N이 1,000,000이므로 시간 초과가 테스트케이스에서 하나 나왔다.
# 시간 초과를 해결하기 위해서는 빠른 소수 찾기 알고리즘을 찾아야만 했다. 찾아보던 중 sqrt를 써서 범위를 줄이면 되는 알고리즘이 있어 시간 복잡도를 계산해보니 1,000*1,000,000이 나오므로 충분히 가능하였다. (1초에 20,000,000회를 기준으로 삼는다.)
# 풀이시간 : 30분

import math

def trans_k(n,k):
    result=''
    while True:
        if n//k<k:
            result=str(n//k)+str(n%k)+result
            break
        result=str(n%k)+result
        n//=k
    return result

def isPrime(n):
    if n==1:
        return False
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True

def solution(n, k):
    answer = 0

    p=trans_k(n,k)
    length=len(p)
    s=''
    arr=[]
    for i in range(length):
        if p[i]=='0':
            if len(s)>0:
                if isPrime(int(s)):
                    answer+=1
            s=''
        elif i==length-1 and p[i]!='0':
            s+=p[i]
            if isPrime(int(s)):
                    answer+=1
        else:
            s+=p[i]



    return answer