# 풀이 시간 - 5분/20분 시간제한 1초 메모리제한 128MB
# 1회차 정답
# s의 길이가 최대 10,000까지인데 정렬알고리즘과 순회 for문을 돌려야할꺼 같아서 최대 O(nlogn) 알고리즘을 쓰면 되겠다라는 생각이 들었다. 실제로 검색해보니 내부 sort() 함수의 시간복잡도가 O(nlogn)이라는 것을 알게되었다. 전체 모든 글자를 돌아보면서 확인해보는 완전탐색이 아닐까 싶다.

s=input()
arr=[]

sum=0

for i in range(len(s)):
  if s[i].isdigit():
    sum+=int(s[i])
  else:
    arr.append(s[i])

arr.sort()
for i in range(len(arr)):
  print(arr[i],end="")
if sum!=0:
  print(sum)

# # 답안지
# data=input()
# result=[]
# value=0

# # 문자를 하나씩 확인하며
# for x in data:
#   # 알파벳인 경우 결과 리스트에 삽입
#   if x.isalpha():
#     result.append(x)
#   # 숫자는 따로 더하기
#   else:
#     value+=int(x)

# # 알파벳을 오름차순으로 정렬
# result.sort()

# # 숫자가 하나라도 존재하는 경우 가장 뒤에 삽입
# if value!=0:
#   result.append(str(value))

# # 최종 결과 출력(리스트를 문자열로 변환하여 출력)
# print(''.join(result))