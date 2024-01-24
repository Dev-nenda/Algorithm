# 서로 다른 N개의 자연수의 합이 S
# N의 최댓값

S = int(input())

N = 0
sum_numbers = 0

for i in range(1, S + 1):
    sum_numbers += i
    N += 1

    if sum_numbers > S:
        N -= 1
        break
print(N)