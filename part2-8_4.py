# part 2. 주요 알고리즘 이론과 실전 문제
# - chapter 8. 다이나믹 프로그래밍
# - 예제 8-4. 바닥 공사*

n = int(input())
d = [0]*1001
d[1] = 1
d[2] = 3
for i in range(3,n+1):
    d[i] = (d[i-1] + 2*d[i-2]) % 796796

print(d[n])