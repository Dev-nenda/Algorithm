# 세점이 주어졌을 때, 
# 축에 평행한 직사각형을 만들기 위해 필요한 네번째 점을 찾기

X = []
Y = []

x4 = 0
y4 = 0

for i in range(3):
    x, y = map(int, input().split())

    X.append(x)
    Y.append(y)

for i in range(3):
    if X.count(X[i]) == 1:
        x4 = X[i]
    
    if Y.count(Y[i]) == 1:
        y4 = Y[i]

print(x4, y4)