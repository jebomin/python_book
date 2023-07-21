#n을 입력받기
n = int(input())

#n개의 정수를 입력받아 리스트에 저장
array = []
for i in range(n):
    input_data = input().split()
    array.append((input_data[0], int(input_data[1])))

#파이썬 기본 정렬 라이브러리를 이용해 정렬 수행
array = sorted(array, key = lambda student: student[1])

#정렬이 수행된 결과를 출력
for student in array:
    print(student[0], end=' ')