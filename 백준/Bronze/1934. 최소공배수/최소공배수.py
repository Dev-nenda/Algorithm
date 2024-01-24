# 두 자연수 A와 B에 대해서 
# A의 배수이면서 B의 배수인 자연수를 A와 B의 공배수라 한다.

T = int(input())

for _ in range(T):
    A, B = map(int, input().split())

    answer = A*B

    while B > 0:
        A, B = B, A%B

    print(answer//A)
    