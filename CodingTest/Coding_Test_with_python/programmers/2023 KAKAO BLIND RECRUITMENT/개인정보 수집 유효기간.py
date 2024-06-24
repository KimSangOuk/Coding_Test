# 풀이시간 20분
# 1회차 정답
# 처음 문제를 접근을 생각하면서 날짜를 비교해서 빼주면 되겠다고 생각하고 풀기 시작하였다. 단순 문자열을 나누어서 접근하면 되었고 총 날짜로 다 환산해서 차이를 계산하기 쉽도록 하였다. 결국 시작 날짜와 오늘 날의 차이가 유효기간을 넘어가면 계약이 파기 되기 때문에 주어진 answer 배열에 담아서 출력 하였다.

def solution(today, terms, privacies):
  answer = []
  
  today_year,today_month,today_day=today.split('.')
  today_total_day=int(today_year)*28*12+int(today_month)*28+int(today_day)
  
  terms_dict=dict()
  for k in terms:
      a,b=k.split()
      terms_dict[a]=int(b)
  
  for i in range(1,len(privacies)+1):
      start_date,type_=privacies[i-1].split()
      date_year,date_month,date_day=start_date.split('.')
      start_day_total_day=int(date_year)*28*12+int(date_month)*28+int(date_day)
      if today_total_day-start_day_total_day>=terms_dict[type_]*28:
          answer.append(i)
  
  return answer