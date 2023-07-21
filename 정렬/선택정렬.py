array = [7,5,9,0,3,1]

#i값은 0부터 '데이터의 개수-1'까지 반복
#i는 가장 작은 데이터와 바뀔 인덱스를 의미, 결과적으로 매번 앞쪽으로 보내고자 하는 가장 앞쪽 원소의 위치
for i in range(len(array)): #매번 가장 작은 원소의 인덱스를 고를 수 있게 함
    min_index = i #가장 작은 원소의 인덱스
    for j in range(i+1, len(array)): #j를 통해 가장 작은 원소를 찾음
        if array[min_index]>array[j]: #현재 작은 원소보다 더 작은 원소 j 값이 있다면
            min_index = j #그걸로 바꿔
        #파이썬은 한줄로 swap를 진행 할 수 있음
        array[i], array[min_index]=array[min_index], array[i] #가장 앞쪽 원소와 가장 작은 원소를 스와프

print(array)