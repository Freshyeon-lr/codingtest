# part 2. 주요 알고리즘 이론과 실전 문제
# - chapter 4. 구현
# - 예제 4-1. 시각

N = int(input())

result = 0

for i in range(N + 1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                result += 1
print(result)
