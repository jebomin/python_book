#집합 자료형 방식으로 구현
#N(가게의 부품 개수)을 입력 받기
n = int(input())
#가게에 있는 전체 부품 번호를 입력 받아서 집합(set) 자료형에 기록
array = set(map(int, input().split()))

#M(손님이 확인 요청한 부품 개수)을 입력 받기
m = int(input())
#손님이 확인 요청한 전체 부품 번호를 공백으로 구분하여 입력
x = list(map(int, input().split()))

#손님이 호가인 요청한 부품 번호를 하나씩 확인
for i in x:
  if i in array:
    #해당 부품이 존재하는지 확인
    print('yes', end = ' ')
  else:
    print('no', end = ' ')