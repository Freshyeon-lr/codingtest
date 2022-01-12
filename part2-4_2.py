# 큰 수의 법칙 
# part 2. 주요 알고리즘 이론과 실전 문제
# - chapter 4. 구현
# - 실전 문제 2. 왕실의 나이트

position = input()
cols = ['a','b','c','d','e','f','g','h']
possible = [[2,1],[-2,1],[2,-1],[-2,-1],[1,2],[1,-2],[-1,2],[-1,-2]]
count = 0

for i in possible:
	current_col = cols.index(position[0])+1
	current_row = int(position[1])
	new_col = current_col + i[0]
	new_row = current_row + i[1]

	if 1<=new_col<=8 and 1<=new_row<=8:
		count += 1
print("result = ", count)

