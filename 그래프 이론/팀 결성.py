#특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
  #루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출 
  if parent[x] != x:
    parent[x] = find_parent(parent, parent[x])
  return parent[x]

#두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
  a = find_parent(parent, a)
  b = find_parent(parent, b)
  if a<b: #더 번호가 큰 쪽이 작은 쪽을 부모로 설정
    parent[b] = a
  else:
    parent[a] = b

#노드의 개수와 간선(Union 연산)의 개수 입력 받기
n, m = map(int, input().split())
parent = [0]*(n+1) #부모 테이블 초기화하기(1번부터 n번까지)

#부모 테이블 상에서, 부모를 자기 자신으로 초기화
for i in range(1, n+1):
  parent[i] = i

#각 연산을 하나씩 확인
for i in range(m):
  oper, a, b = map(int, input().split())
  #합집합(union) 연산인 경우
  if oper == 0:
    union_parent(parent, a, b)
  #찾기(find) 연산인 경우
  elif oper == 1:
    if find_parent(parent, a) ==  find_parent(parent, b):
      print('YES')
    else:
      print('NO')