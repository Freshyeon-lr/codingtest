n, m, k = map(int, input("n, m, k = ").split())
data = list(map(int, input("data = ").split()))

data.sort()
second_cnt = m%k #2
first_cnt = int(m/k)*k

result = data[-1]*first_cnt + data[-2]*second_cnt
print("result = ", result)