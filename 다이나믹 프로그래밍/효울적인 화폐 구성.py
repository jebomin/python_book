#정수 N, M을 입력받기
n, m = map(int, input().split())
#N개의 화폐 단위 정보를 입력받기
array = []
for i in range(n):
  array.append(int(input()))

#한 번 계산된 결과를 저장하기 위한 DP 테이블 초기화
d = [10001]*(m+1)

#다이나믹 프로그래밍 진행(보텀업)
d[0] = 0
#i는 각각의 화폐 단위, j는 각각의 금액을 의미
for i in range(n):
  for j in range(array[i], m+1): #해당 금액부터 m원까지
    if d[j-array[i]] != 10001: #(i-k)원을 만드는 방법이 존재하는 경우
      d[j] = min(d[j], d[j-array[i]]+1) #j-array[i]가 ai-k를 만드는 방법이고 거기서 1을 더한 값과 현재 값과 비교해서 더 작은 값을 갱신

#계산된 결과 출력
if d[m] == 10001: #최종적으로 M원을 만드는 방법이 없는 경우
  print(-1)
else:
  print(d[m])