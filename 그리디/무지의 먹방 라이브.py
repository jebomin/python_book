# 최악의 경우 음식의 수만큼만 roop를 돌면 되므로 시간복잡도가 줄어든다.
# operator 모듈의 itemgetter 함수는 주어진 인덱스(또는 여러 인덱스)에 해당하는 항목을 추출하는 함수다.
# 주로 정렬에 사용되며, 특히 복잡한 데이터 구조에서 정렬 기준을 지정하는 데 효과적입니다.
from operator import itemgetter

def solution(food_times, k):
  foods = [] # (먹는데 걸리는 시간, 음식 번호) 저장
  n = len(food_times) # 음식의 수
  for i in range(n):
    foods.append((food_times[i], i+1))
    
  # 튜플의 첫번째 인덱스 기준으로 정렬(걸리는 시간이 작은 음식부터 큰 음식순으로 정렬)
  foods.sort() 
  pretime = 0
  for i, food in enumerate(foods): # 음식을 먹는 roop
    diff = food[0] - pretime #여기서 이 diff는 위 그림들의 높이를 나타내는 거다. 즉, 위 예시라면? 1,2,2가 될 것이다.
    if diff != 0:
      spend = diff * n # 현재 음식을 다먹는데 걸리는 시간
      if spend <= k:
        k -= spend 
        pretime = food[0]
      else:
        idx = k % n # 여기서 n은 남은 음식의 수이다
        # key=itemgetter(1)은 각 튜플의 두번째 원소로 정렬한다는 의미다.
        # 즉, 남은 음식을 번호 순으로 다시 정렬한다는 의미
        sublist = sorted(foods[i:], key=itemgetter(1)) 
        return sublist[idx][1]

    n -= 1 # 현재 음식 다 먹음
  # for문 도중 return이 안됬다는 것은 k가 남았다 
  # -> 음식을 다 먹었다 -> -1 반환  
  return -1