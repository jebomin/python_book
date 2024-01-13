import heapq

def solution(food_times, k):

    # 전체 음식을 먹는 시간보다 네트워크 지연 시작 시간이 크거나 같다면 더 이상 먹을 음식이 없으므로 -1 출력
    if (sum(food_times) <= k):
        return -1

    # 먹는 시간이 작은 음식부터 제거해야하므로 우선순위 큐를 사용
    q = []
    # 우선순위 큐에 (소요 시간, 음식 번호) 튜플을 삽입
    for i in range(len(food_times)):
        heapq.heappush(q, (food_times[i], i+1))

    # 이전 음식 섭취까지 소요한 전체 시간
    sum_time = 0
    # 이전 음식의 섭취 시간
    previous_time = 0
    # 남은 음식 개수
    length = len(food_times)

    # [이전 음식 섭취까지 소요한 전체 시간 + 현재 음식을 섭취하기 위해 필요한 시간]이 K보다 커지면, 반복문 종료
    # 현재 음식을 섭취하기 위한 시간은, (현재 음식 섭취 시간 - 이전 음식 섭취 시간) * 남은 음식 개수
    while (sum_time + ((q[0][0] - previous_time) * length) <= k):
        # 현재 음식을 우선순위 큐에서 제거하며, 현재 음식의 섭취 시간을 저장
        now_time = heapq.heappop(q)[0]
        # 현재 음식을 모두 섭취하기 위해 걸리는 시간을, 음식 섭취에 소요한 전체 시간에 추가
        sum_time += (now_time - previous_time) * length
        # 남은 음식 개수 감소
        length -= 1
        # 이전 음식 섭취 시간을 현재 음식 섭취 시간으로 변경
        previous_time = now_time

    # 반복문 종료 이후에는, K 발생까지 남은 시간을 확인해, K 이후에 섭취할 음식을 결정

    # 우선순위큐의 남아있는 요소들을 음식 번호를 기준으로 오름차순 정렬
    result = sorted(q, key=lambda x:x[1])

    # (K 발생까지 남은 시간 % 남은 음식 개수), 배열의 idx는 0부터 시작하므로 나머지 값을 idx로 사용하면 됨
    return result[(k-sum_time) % length][1]