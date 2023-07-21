import heapq

#내림차 순 힙 정렬
def heapsort(iterable):
  h = []
  result = []
  #모든 원소를 차례대로 힙에 삽입
  for value in iterable:
    heapq.heappush(h, -value) #부호를 바꿔주고
  #힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
  for i in range(len(h)):
    result.append(-heapq.heappop(h)) #꺼낼 때 부호 바꿔주기
  return result

result = heapsort([1,3,5,7,9,2,4,6,8,0])
print(result)