# - 처음에는 앞과 뒤의 숫자를 확인하면서 증가, 감소를 확인하면서 그리디스럽게 앞에서부터 접근하면 어떨까 하는 식으로 생각해보았지만 중간에 최대값이 있고 앞에 있는 증가, 감소가 무관해질 수 있다는 사실을 떠올려서 최대값 중심으로 알고리즘을 구성하기 위해서 뒤에서부터 확인하기로 하였다. 
# - 이때, 중심이 되는건 주식을 판매하는 시점인 최대값이 되는 시점이기 때문에 뒤에서 부터 확인하면서 최대값이 갱신되는 시점이면 쌓아둔거를 다팔고 그렇지 않을 경우에는 주식을 다 구매하는 식으로 for문을 사용하였다. 필요한 최대시점만을 보고 현재만을 보고 판단하기 때문에 그리디스럽다고 할 수 있을꺼 같다.
# - 풀이시간 : 25분

tc=int(input())
for _ in range(tc):
    n=int(input())
    arr=list(map(int,input().split()))
    max_cost=0
    sub_spend_cost=0
    answer=0
    cnt=0
    for i in range(n-1,-1,-1):
        if arr[i]<max_cost:
            cnt+=1
            sub_spend_cost+=arr[i]
        elif arr[i]>=max_cost:
            answer+=-sub_spend_cost+cnt*max_cost
            max_cost=arr[i]
            cnt=0
            sub_spend_cost=0
    answer+=-sub_spend_cost+cnt*max_cost
    print(answer)