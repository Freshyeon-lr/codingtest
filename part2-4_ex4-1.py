N = input()
step = list(input().split())
x = 1
y = 1
for i, j in enumerate(step):
    if j == 'R':
        if y < int(N):
            y = y + 1
    elif j == 'L':
        if y > 1:
            y = y - 1
    elif j == 'U':
        if x > 1:
            x = x - 1
    elif j == 'D':
        if x < int(N):
            x = x + 1
    print("test = ",x,y)
print(x, y)