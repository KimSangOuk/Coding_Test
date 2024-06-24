# 이것이 취업을 위한 코딩테스트다 part03 '30. 가사 검색'와 동일

# 2회차 풀이

import bisect
def solution(words, queries):
  answer = []

  # 단어의 중 최대의 길이
  max_length=0
  for word in words:
    max_length=max(len(word),max_length)

  words.sort()
  reversed_words=[]
  for word in words:
    reversed_words.append(word[::-1])
  reversed_words.sort()
  words_length_l_to_r=[[] for _ in range(max_length+1)]
  words_length_r_to_l=[[] for _ in range(max_length+1)]
  for word in words:
    words_length_l_to_r[len(word)].append(word)
  for word in reversed_words:
    words_length_r_to_l[len(word)].append(word)
  # print(words_length_l_to_r)
  # print(words_length_r_to_l)

  for query in queries:
    length=len(query)
    if length>max_length:
      answer.append(0)
      continue
    count=0
    find_right=query.replace('?','z')
    find_left=query.replace('?','a')
    if query[0]=='?':
      right=bisect.bisect_right(words_length_r_to_l[length],find_right[::-1])
      left=bisect.bisect_left(words_length_r_to_l[length],find_left[::-1])
      count=right-left
    else:
      right=bisect.bisect_right(words_length_l_to_r[length],find_right)
      left=bisect.bisect_left(words_length_l_to_r[length],find_left)
      count=right-left
    answer.append(count)

  return answer