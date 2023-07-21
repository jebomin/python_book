#각 노드가 연결된 정보를 표현(2차원 리스트)
graph = [
    [], #인덱스 0인 부분은 비워두기
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

#각 노드가 방문된 정보를 리스트 자료형으로 표현(1차원 리스트)
#1번 노드부터 8번 노드까지 사용하고 있기 때문에 인덱스 0번은 무시하기 위해 9를 곱해줌
visited = [False]*9

#DFS 매서드 정의
def dfs(graph, v, visited):
    #현재 노드를 방문 처리
    visited[v] = True
    print(v, end = ' ')
    #현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

dfs(graph,1,visited)