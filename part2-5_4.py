# part 2. 주요 알고리즘 이론과 실전 문제
# - chapter 5. DFS/BFS
# - 예제 5-4. 미로 탈출

from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x,y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    return graph[n-1][m-1]

if __name__ == '__main__':
    n, m = map(int, input().split())
    graph = []
    for i in n:
        graph.append(list(map(int, input())))
    print(bfs(0, 0))

'''
def bfs(graph, start, visited):
    
    for i in graph[start-1]:
        bfs(graph, [x-1, y])
    deque.popleft(graph[start-1])

n, m = map(int, input().split())
graph = []
for i in n:
    graph.append(input())
visited = [False]*n
bfs(graph, 1, visited)
'''
