# part 2. 주요 알고리즘 이론과 실전 문제
# - chapter 3. Greedy
# - 실전 문제 3. 숫자 카드 게임

n, m = map(int, input().split())

for i in range(n):
    data = map(int, list(input().split()))
    min_data = []
    min_data.append(min(data))
    result = max(min_data)
print("max = ", result)

'''
n, m = map(int, input().split())
result = 0
for i in range(n):
    data = list(map(int, input().split()))
    min_value = min(data)
    result = max(result, min_value)
print(result)
'''

