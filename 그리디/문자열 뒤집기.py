data = input()
count0 = 0 # 1->0
count1 = 0 # 0->1

#첫 번째 원소에 대해서 처리
#이렇게 처리 안해주면 count0이랑 count1이 각각 1로 나옴
#왜냐? 0001100 입력 값에서 000을 1로 바꾸는걸 신경 안 써주기 때문
#따라서 첫 번째 원소 처리를 초기 값으로 꼭 해줘야하는 것을 기억해야함
if data[0] == '1':
  count0 += 1
else:
  count1 += 1

#두 번째 원소부터 모든 원소를 확인하며
for i in range(len(data)-1):
  if data[i] != data[i+1]:
    #다음 수에서 1로 바뀌는 경우
    if data[i+1]=='1':
      count0 += 1
    #다음 수에서 0으로 바뀌는 경우
    else:
      count1 += 1
      

print(min(count0, count1))