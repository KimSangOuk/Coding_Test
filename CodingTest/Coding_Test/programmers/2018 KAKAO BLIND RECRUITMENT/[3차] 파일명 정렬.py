# - 런타임 에러 잡느라 시간을 다쓴 문제이다. 엄청 빨리 풀릴지 알았는데 왜 안풀린지를 모르겠다. 기존에는 start_number_index를 확인하는 것이 아니라 j-1로 처리했는데 런타임 에러가 났다. head도 number도 한글자 이상이기 때문에 문제가 생길 수가 없다고 생각했는데 어디서 런타임 에러가 났는지 못찾겠다... 질문게시판도 싹 돌아봤는데 다들 런타임 에러에 관련된 완전한 해결책을 제시하는 사람은 없더라... 아마 숫자가 없거나 문자가 없는 문자열도 처리가 되야하는게 아닌가 싶다. 이건 그냥 뇌피셜...
# - 풀이 자체는 단순하다. 처음 나오는 숫자열을 파악하고 그 앞에 오는 문자열, 숫자열, 그 파일의 순서를 키로 잡아서 정렬한 다음 출력하면 된다.
# - 풀이시간 : 60분

def solution(files):
  answer = []
  n=len(files)
  files_include_sort_standard=[]
  for i in range(n):
      file=files[i]
      length=len(file)
      lower_file=file.lower()
      head=''
      number=''
      start_number_index=-1
      for j in range(1,length):
          if file[j].isdigit() and start_number_index==-1:
              head=file[0:j]
              start_number_index=j
          elif not file[j].isdigit() and start_number_index!=-1:
              number=file[start_number_index:j]
              break
      if start_number_index!=-1 and number=='':
          number=file[start_number_index:]
      # print(head,number)
      files_include_sort_standard.append((head.lower(),int(number),i,file))
  files_include_sort_standard.sort()
  for i in range(n):
      answer.append(files_include_sort_standard[i][3])
  return answer