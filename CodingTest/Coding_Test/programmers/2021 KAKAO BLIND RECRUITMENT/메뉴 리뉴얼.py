from itertools import combinations

def solution(orders, course):
    answer = []

    cnt_how_many=dict()
    for i in course:
        cnt_how_many[i]=dict()
    for order in orders:
        order_list=list(order)
        order_list.sort()
        for how_many in course:
            select_by_how_many=list(combinations(order_list,how_many))
            for select in select_by_how_many:
                s="".join(select)
                if s in cnt_how_many[how_many]:
                    cnt_how_many[how_many][s]+=1
                else:
                    cnt_how_many[how_many][s]=1
    for how_many in course:
        largest_list=[]
        largest_value=2
        for key in cnt_how_many[how_many]:
            if cnt_how_many[how_many][key]>largest_value:
                largest_value=cnt_how_many[how_many][key]
                largest_list=[key]
            elif cnt_how_many[how_many][key]==largest_value:
                largest_list.append(key)
        answer+=largest_list
    answer.sort()
    return answer