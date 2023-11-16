n,m,k=map(int,input().split())
a_list=list(map(int,input().split()))
a_list.sort(reverse=True)

result=(m//(k+1))*(a_list[0]*k+a_list[1])+(m%(k+1))*a_list[0]
print(result)