#현재 나이트의 위치 입력받기
#현재 위치의 데이터가 들어왔을 때
input_data = input()
#두번째 위치의 문자를 숫자로 바꾸고
row = int(input_data[1])
#문자로 들어온 값(즉 첫번째 위치에 있는 문자)을 아스키코드로 변환 후 a를 아스키코드로 바꾼 값의 차를 구한 후 거기에 1을 더함
column = int(ord(input_data[0]))-int(ord('a'))+1

#나이트가 이동할 수 있는 8가지 방향 정의(방향 벡터
#여기서 steps변수가 dx와 dy 변수의 기능을 대신해 수행
steps = [(-2,-1), (-1,-2), (1,-2), (2,-1), (2,1), (1,2), (-1,2), (-2,1)]

#8가지 방향에 대하여 각 위치로 이동이 가능한지 확인
result = 0
for step in steps:
    #이동하고자 하는 위치 확인
    next_row = row+step[0]
    next_column = column+step[1]
    #해당 위치로 이동이 가능하다면 카운트 증가
    if next_row>=1 and next_row<=8 and next_column>=1 and next_column<=8:
        result+=1

print(result)