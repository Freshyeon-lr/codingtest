# part 2. 주요 알고리즘 이론과 실전 문제
# - chapter 3. Greedy
# - 실전 문제 4. 1이 될 때까지

N, K = map(int, input().split())

result = 0
while N!=1:
    if N%K==0:
        N = int(N/K)
        result += 1
    else:
        N = N-1
        result += 1
print("result = ", result)
