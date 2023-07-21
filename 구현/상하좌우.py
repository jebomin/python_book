#N 입력받기
n = int(input())
#현재 위치를 의미하는 x와 y변수 선언
x, y = 1, 1
plans = input().split()

#방향 벡터를 통해 L, R, U, D에 따른 이동방향을 명시
dx = [0,0,-1,1]
dy = [-1,1,0,0]
move_types = ['L', 'R', 'U', 'D']

#이동 계획을 하나씩 확인하기
for plan in plans:
    #이동 후 좌표 구하기
    #현재 이동계획이 move_types에서 어떤건지 확인
    for i in range(len(move_types)):
        #해당 move_types에 맞는 다음위치 값을 dx랑 dy를 통해 찾아서 할당
        if plan == move_types[i]:
            #파이썬에서는 nx와 ny를 초기화 하지 않아도 됨
            nx = x+dx[i]
            ny = y+dy[i]
    #또한 반복문 밖에서 nx와 ny를 참조할 수 있음
    #공간을 벗어나는 경우 무시
    if nx<1 or ny<1 or nx>n or ny>n:
            continue
    #이동 수행
    x, y = nx, ny

print(x,y)