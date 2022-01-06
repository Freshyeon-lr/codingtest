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

