# need more practice
# 큰 수의 법칙 
# part 2. 주요 알고리즘 이론과 실전 문제
# - chapter 4. 구현
# - 실전 문제 3. 게임 개발

n, m = map(int, input().split())
x, y, direct = map(int, input().split())
all_map = []

save_xy = [[0] * m for _ in range(n)]
print("save_xy = ", save_xy)
def turn_left():
	global direct
	direct -= 1
	if direct == -1:
		direct = 3




for i in range(n):
	map_cols = list(map(int, input().split()))
	all_map.append(map_cols)

turn_time = 0
count = 1
save_xy[x][y] = 1
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

while True:
	turn_left()
	nx = x+dx[direct]
	ny = y+dy[direct]
	if save_xy[nx][ny] == 0 and all_map[nx][ny] == 0:
		save_xy[nx][ny] = 1
		x = nx
		y = ny
		count += 1
		turn_time = 0
		#continue
	else:
		turn_time += 1
		
	if turn_time == 4:
		nx = x-dx[direct]
		ny = y-dy[direct]
		if all_map[nx][ny] == 0:
			x = nx
			y = ny
		else:
			break
		turn_time = 0
print(count)

	
