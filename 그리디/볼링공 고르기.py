#볼링공의 개수 n과 공의 최대 무게 m을 입력 받음
n, m = map(int, input().split())
#각 볼링공의 무게를 입력 받음
data = list(map(int, input().split()))

#1부터 10까지의 무게를 담을 수 있는 리스트
array = [0]*11

for x in data:
  #각 무게에 해당하는 볼링공의 개수 카운트
  array[x]+= 1
  
result = 0
#1부터 m까지의 각 무게에 대한 처리(즉 a가 볼링공을 선택하는 경우의 수를 모두 다룬다는 의미)
for i in range(1, m+1):
  #여기서 이 n은 b가 선택하는 경우의 수가 됨
  n -= array[i] #무개가 i인 볼링공의 개수를 제외(A가 무게가 i인 볼링공의 개수를 골랐다고 가정해서 그만큼 빼주는 것임, B가 같은 무게를 고르면 안되니까)
  result += array[i]*n#a가 선택하는 경우의 수 * b가 선택하는 경우의 수
  
print(result)