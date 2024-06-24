# 풀이시간 50분 시간제한 1초 메모리제한 128MB
# 2회차 정답
# 순차적으로 한 수를 선택했을 때 그 수와 더했을 때 절댓값이 가장 작은 값이 되는 수를 구하는 문제이다. 데이터의 크기가 100,000이기 때문에 각 수를 고정으로 선택하면서 다른 한수를 고를 수 있는데, 이때, 완전 탐색을 하면 시간복잡도가 너무 커지므로 logN을 통해 찾는다면 총 NlogN의 시간복잡도로 가능해진다. 그렇게 탐색을 진행하면서 한수가 다르다면 저장을 하고 부호를 바꾼 값을 기준으로 범위를 좁혀가며 탐색해 가면 된다.

n=int(input())

array=list(map(int,input().split()))
array.sort()

def binary_search(array,target,start,end):
  result=int(2e9)
  answer=0
  while start<=end:
    mid=(start+end)//2
    one=array[target]
    two=array[mid]
    t=abs(one+two)
    if result>t:
      result=t
      answer=two
    if -one==two:
      return two
    if -one>two:
      start=mid+1
    else:
      end=mid-1
  return answer

result=int(2e9)
for i in range(0,n-1):
  k=binary_search(array,i,i+1,n-1)
  if result>abs(array[i]+k):
    result=abs(array[i]+k)
    answer=[array[i],k]

answer.sort()
for i in range(2):
  print(answer[i],end=' ')
    
    
























# 풀이시간 105분/60분 시간제한 1초 메모리제한 128MB
# 1회차 정답 - but 풀이시간 너무 오래 걸림
# 단순히 절대값이 작아지는 조건을 구한다음 하나씩 비교하며 구하면 되는 문제이지만 두가지에서 시간이 오래걸렸다.
# 첫번째, 절대값이 작아지는 조건을 구하는데 시간이 오래걸렸다. 절대값이 작아지는 조건은 한 수의 반대 값에 가까워지는 경우이므로 반대의 수보다 작아지면 커지고 커지면 작아지는 식으로 구하면 되었다.
# 두번째, 최소 값이 합이기 때문에 양수끼리나 음수끼리를 더하면 20억이 될 수 있다는 점을 간과하였다.
# 첫번째 케이스의 경우, 눈대중으로 수의 조건을 나누어서 구하는 것이 아닌 공식을 세우고 나서 크기를 비교해보는게 좋을 것 같다. 눈대중으로 확인하는 습관때문에 오래걸렸다고 할 수 있다.
# 두번째 경우는, 숫자의 최대크기가 얼마나 커질 수 있는지를 비교하지 않고 그냥 1e9로 때려박는 습관떄문에 발생했다고 볼 수 있다.

# def binary_search(array,fix,start,end):
#   min_value=2000000000
#   result=0
#   while start<=end:
#     mid=(start+end)//2
#     if abs(array[mid]+fix)<min_value:
#       min_value=abs(array[mid]+fix)
#       result=array[mid]
#     if array[mid]<=-fix:
#       start=mid+1
#     else:
#       end=mid-1
#   return min_value,result

# n=int(input())
# array=list(map(int,input().split()))

# array.sort()

# answer=[]
# for i in range(len(array)):
#   min_value,match_x=binary_search(array,array[i],i+1,len(array)-1)
#   answer.append((min_value,array[i],match_x))

# answer.sort()
# # print(answer)
# print(answer[0][1],answer[0][2])