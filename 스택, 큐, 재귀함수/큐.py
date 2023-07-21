from collections import deque

#큐 구현을 위해 deque 라이브러리 사용(리스트 자료형을 사용해 구현할 수 있지만 시간복잡도가 높아 추천하지는 않음)
queue = deque()

#삽입(5) - 삽입(2) - 삽입(3) - 삽입(7) - 삭제 - 삽입(1) - 삽입(4) - 삭제
queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

print(queue) #먼저 들어오 순서대로 출력
queue.reverse() #역순으로 바꾸기
print(queue) #나중에 들어온 원소부터 출력