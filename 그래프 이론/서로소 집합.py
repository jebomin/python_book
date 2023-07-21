#특정 원소가 속한 집단(루트 번호)을 찾기
def find_parent(parent, x): #parent는 부모 테이블, x는 노드의 번호
  #루트 노드를 찾을 때까지 재귀 호출
  if parent[x] != x: #현재 부모가 자기 자신이 아니면 루트 노드가 아닌 거니까
    return find_parent(parent, parent[x]) #자신에 대한 부모 노드를 넣어서 다시 find_parent하는 거
  return x

#두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
  a = find_parent(parent, a)
  b = find_parent(parent, b)
  if a<b: #더 번호가 큰 쪽이 작은 쪽을 부모로 설정
    parent[b] = a
  else:
    parent[a] = b

#노드의 개수와 간선(Union 연산)의 개수 입력 받기
v, e = map(int, input().split())
parent = [0]*(v+1) #부모 테이블 초기화하기(1번부터 v번까지)

#부모 테이블 상에서, 부모를 자기 자신으로 초기화
for i in range(1, v+1):
  parent[i] = i

#Union 연산을 각각 수행
for i in range(e):
  a, b = map(int, input().split())
  union_parent(parent, a, b)

#각 원소가 속한 집합 출력하기
print('각 원소가 속한 집단 : ', end = '')
for i in range(1, v+1):
  print(find_parent(parent, i), end = ' ') #각 노드에 대한 루트 노드가 출력 됨

print()

#부모 테이블 내용 출력하기
print('부모 테이블 : ', end = '')
for i in range(1, v+1):
  print(parent[i], end =' ')