# 과자 한개의 가격이 K
# 사려고 하는 과자의 개수가 N
# 현재 가진 돈의 액수가 M

K, N, M = map(int, input().split())

if K * N > M:
    print(K*N - M)

elif M >= K*N:
    print(0)