# part 2. 주요 알고리즘 이론과 실전 문제
# - chapter 5. DFS/BFS
# - 예제 5-3. 음료수 얼려 먹기

n, m = map(int, input().split())
graph = []
for i in n:
    graph.append(list(map(int, input())))

def dfs(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False

result = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j):
            result += 1
print("result = ", result)