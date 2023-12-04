# 풀이 시간 - 17분/20분 시간제한 2초 메모리제한 128MB
# 1회차 정답
# S의 길이가 100만보다 작기 때문에 적어도 O(N) 알고리즘을 써야할것으로 예상(근데 2초이기 때문에 괜찮음)
# 순서대로 훓어가면서 0과 1이 변하는 시점을 챙기기만 하면 되는 그리디 알고리즘


count=[0,0]

s=input()
first=int(s[0])
count[first]=1 # first를 굳이 안쓰고 data[i], data[i+1]로 표현해도 된다는 걸 다시 봤다.
for i in range(1,len(s)):
  data=int(s[i])
  if data!=first:
    if data==0:
      count[0]+=1
    else:
      count[1]+=1
  first=data
print(min(count))

# # 답안지
# data = input()
# count0=0 # 전부 0으로 바꾸는 경우
# count1=0 # 전부 1로 바꾸는 경우

# # 첫 번쨰 원소에 대하여 처리
# if data[0]=='1':
#   count0+=1
# else:
#   count1+=1

# # 두 번째 원소부터 모든 원소를 확인하며
# for i in range(len(data)-1):
#   if data[i]!=data[i+1]:
#     # 다음 수에서 1로 바뀌는 경우
#     if data[i+1]=='1':
#       count0+=1
#     # 다음 수에서 0으로 바뀌는 경우
#     else:  
#       count1+=1

# print(min(count0,count1))