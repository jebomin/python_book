def gcd(a,b):
    #a가 b의 배수면 b를 반환
    if a%b==0:
        return b
    #그렇지 않다면 b와 a를 b로 나눈 나머지의 최대공약수를 반환할 수 있게함
    else:
        return gcd(b,a%b)

print(gcd(192,162))