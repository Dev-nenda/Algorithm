# 두 양의 정수가 주어짐
# 첫번째 수가 두번째 수보다 큰지 구하는 프로그램

while True:
    a, b = map(int, input().split())

    if a == 0 and b == 0:
        break

    if a > b:
        print('Yes')

    else:
        print('No')