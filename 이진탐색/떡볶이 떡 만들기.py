#떡의 개수(N)와 요청한 떡의 길이(N)을 입력
n, m = list(map(int, input().split(' ')))
#각 떡의 개별 높이 정보를 입력
array = list(map(int, input().split()))

#이진 탐색을 위한 시작 점과 끝 점 설정
start = 0
end = max(array)+1

#이진 탐색 수행(반복문)
result = 0
while(start<=end):
  total = 0
  mid = (start+end)//2
  for x in array:
    #잘렸을 때의 떡의 양 계산
    if x>mid:
      total += x-mid
    #떡의 양이 부족한 경우 더 많이 자르기(왼쪽 부분 탐색)
    if total<m:
      end = mid-1
    #떡의 양이 충분한 경우 덜 자르기(오른쪽 부분 탐색)
    else:
      result = mid #최대한 덜 잘랐을 때가 정답이므로, 여기에서 result 기록
      start = mid+1

#정답 출력
print(result)