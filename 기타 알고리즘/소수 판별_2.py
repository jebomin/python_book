import math

#소수 판별 함수(2 이상의 자연수에 대하여)
def is_prime_number(x):
  #2부터 x의 제곱근까지의 모든 수를 확인하며
  for i in range(2, int(math.sqrt(x))+1):
    #x가 해당 수로 나누어 떨어진다면
    if x%i==0:
      return False #소수가 아님
  return True #소수임

print(is_prime_number(4))
print(is_prime_number(7))