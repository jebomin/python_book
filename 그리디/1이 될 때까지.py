#N, K를 공백을 기준으로 구분해 입력 받고 map함수로 int형으로 전환
n, k = map(int, input().split())

result = 0

while True:
    #N이 K로 나누어 떨어지는 수가 될 때까지 빼기
    #n이 k로 나누어 떨어지지 않았을 때 k로 나눠떨어질 수 있는 가장 가까운 수를 찾을 수 있음
    #즉 n에서 1을 빼는 과정을 통해 target이라는 값까지 만들 수 있고 이 target은 k로 나눠떨어지는 수
    target = (n//k)*k 
    #result는 우리가 총 연산을 수행하는 횟수
    #여기서 1을 빼는 연산을 몇번 수행할 수 있는지 한번에 더해줌
    result += (n-target)
    n = target
    #N이 K보다 작을 때(더 이상 나눌 수 없을 때) 반복문 탈출
    if n<k:
        break
    #K로 나누는 걸 한번 수행하기 때문에 result에 1을 더해줌
    result += 1
    n //= k

#n이 1보다 크다면 1로 만들어주기 위해 마지막으로 남은 수에 대해 1씩 빼기
result += (n-1)
print(result)