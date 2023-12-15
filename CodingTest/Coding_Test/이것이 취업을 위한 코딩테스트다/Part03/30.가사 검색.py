# 풀이시간 초과/90분 시간제한 1초 메모리제한 128MB
# 1회차 오답 - 풀이 방식에는 접근했으나 완전한 알고리즘을 구하지 못함
# 먼저 틀린 이유는 명확하게 떨어졌다. 두가지가 있는데 첫 번째, bisect 함수가 문자열에도 적용이 되는지 몰랐다. 그리고 두 번째, bisect 함수의 정의를 알지 못했다. 이 함수의 정의는 목표를 찾는게 아니라 넣는 위치를 찾는 거였는데 계속 뭔가 찾으려고 했다.
# 이 두가지를 알고 있었다면 더 쉽게 접근했을 것 같다. 거의 대부분의 아이디어는 비스무리하다.
# 개념이 일단 틀리고 나서 구현을 하려고 하다보니 당연히 찾는 거 위주로 구현했고 비교에서 그쳤다. 그리고 문자열 적용이 되는지 몰랐으니 무한정 구현하느라 식이 길어졌다. 내가보니까 만약 이 두가지를 알고 있었다면 1시간 내로 풀었다.

# 2회차 풀이




# 1회차 풀이
# 이 식들을 그냥 bisect가 문자열에 사용되는 줄 알았으면 구현이 길어질 필요가 없이 메인함수에만 신경 쓸 수 있었음
def count_by_value(array,x):
  n=len(array)

  a=first(array,x,0,n-1)

  if a==None:
    print("a가 0일리가")
    return 0

  b=last(array,x,0,n-1)

  # if b==None:
  #   print("b가 0일리가")
  #   return 0

  return b-a+1

def first(array,target,start,end):
  if start>end:
    return None
  mid=(start+end)//2
  if match(array[mid],target) and (mid==0 or not match(array[mid-1],target)):
    print("처음 좌표 찾았당!",mid)
    return mid
  elif match(array[mid],target) or (not match(array[mid],target) and array[mid]>target) :
    return first(array,target,start,mid-1)
  else:
    return first(array,target,mid+1,end)

def last(array,target,start,end):
  if start>end:
    return None
  mid=(start+end)//2
  if match(array[mid],target) and (mid==len(array)-1 or not match(array[mid+1],target)):
    print("마지막 좌표 찾았당!",mid)
    return mid
  elif  (not match(array[mid],target) and array[mid]>target):
    return last(array,target,mid+1,end)
  else:
    return last(array,target,start,mid-1)

def match(s,target):
  if len(s)==len(target):
    for i in range(len(s)):
      if target[i]!='?' and s[i]!=target[i]:
        print("글자 불일치",s,target)
        return False
  else:
    print("글자 수 불일치",s,target)
    return False
  print("일치",s,target)
  return True
        
def solution(words,queries):
  answer=[]
  # 여기서도 길이에 따라 한번 정렬한 후 하고 있는데 만약 개념을 알아서 넣는걸로 쳤다면 길이별로 배열을 나누어봤을만 하다. 애초에 그 전 아이디어를 생각하지 못한게, 즉 지식이 부족한게 먼저 잘못임.
  words.sort(key=lambda x:(len(x),x))
  print(words)
  reverse_words=sorted([word[::-1] for word in words], key=lambda word: (len(word), word))
  print(reverse_words)
  for query in queries:
    if query[0]!='?':
      # 여기서도 마찬가지로 넣는 줄 알았으면 ?를 변환했을 텐데 개념이 틀리니까 문제도 틀리는 경우이다.
      count=count_by_value(words,query)
    else:
      count=count_by_value(reverse_words,query[::-1])
    print("갯수는?",count)
    answer.append(count)
  return answer

words=["frodo","front","frost","frozen","frame","kakao"]
queries=["fro??","????o","fr???","fro???","pro?"]
print(solution(words,queries))

# 답안 예시
from bisect import bisect_left, bisect_right

# 값이 [left_value, right_value]인 데이터의 개수를 반환하는 함수
def count_by_value(a, left_value, right_value):
  right_index=bisect_right(a,right_value)
  left_index=bisect_left(a,left_value)

  reutrn right_index-left_index

# 모든 단어를 길이마다 나누어서 저장하기 위한 리스트
array = [[] for _ in range(10001)]
# 모든 단어를 길이마다 나누어서 뒤집어 저장하기 위한 리스트

def solution(words,queries):
  answer=[]
  for word in words: # 모든 단어를 접미사 와일드카드 배열, 접두사 와일드카드 배열에 각각 삽입
    array[len(word)].append(word) # 단어를 삽입
    reversed_array[len(word)].append(word[::-1]) # 단어를 뒤집어서 삽입

  for i in range(10001): # 이진 탐색을 수행하기 위해 각 단어 리스트 정렬 수행
    array[i].sort()
    reversed_array[i].sort()

  for q in queries: # 쿼리를 하나씩 확인하며 처리
    if q[0] != '?': # 접미사에 와일드카드가 붙은 경우
      res=count_by_value(array[len(q)],q.replace('?','a'),q.replace('?','z'))
    else: # 접두사에 와일드 카드가 붙은 경우
      res=count_by_value(reversed_array[len(q)],q[::-1].replace('?','a'),q[::-1].replace('?','z'))
    # 검색된 단어의 개수를 저장
    answer.append(res)
  return answer