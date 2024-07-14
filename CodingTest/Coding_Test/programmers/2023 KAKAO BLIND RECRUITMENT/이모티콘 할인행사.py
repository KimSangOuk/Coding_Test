from itertools import product

def solution(users, emoticons):
    answer = []


    sales_percent=[10,20,30,40]

    cases=list(product(sales_percent,repeat=len(emoticons)))
    for case in cases:
        plus_service=0
        sales_total=0
        for user in users:
            total=0
            add_service=False
            for i in range(len(emoticons)):
                if case[i]>=user[0]:
                    total+=emoticons[i]*(100-case[i])//100
                if total>=user[1]:
                    plus_service+=1
                    add_service=True
                    break
            if not add_service:
                sales_total+=total
        answer.append([plus_service,sales_total])

    answer.sort(key=lambda x:(x[0],x[1]))
    # print(answer)
    return answer[-1]