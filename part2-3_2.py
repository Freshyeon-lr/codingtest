# 큰 수의 법칙 
# part 2. 주요 알고리즘 이론과 실전 문제
# - chapter 3. Greedy
# - 실전 문제 2. 큰 수의 법칙

n, m, k = map(int, input("n, m, k = ").split())
data = list(map(int, input("data = ").split()))

data.sort()
second_cnt = m%k #2
first_cnt = int(m/k)*k

result = data[-1]*first_cnt + data[-2]*second_cnt
print("result = ", result)
