# 같은 눈이 3개 나오면 10,000 + (같은눈)x1000
# 같은 눈이 2개 나오면 1000 + (같은 눈)x100
# 모두 다른 눈 (그 중 가장 큰 눈)x100

T = int(input())

max_prize = 0

for _ in range(T):
    dice = list(map(int, input().split()))

    if dice[0] == dice[1] == dice[2]:
        max_prize = max(max_prize, 10000 + dice[0]*1000)

    elif dice[0] == dice[1] or dice[0] == dice[2]:
        max_prize = max(max_prize, 1000 + dice[0] * 100)

    elif dice[1] == dice[2]:
        max_prize = max(max_prize, 1000 + dice[1] * 100)

    else:
        max_prize = max(max_prize, 100 * max(dice))

print(max_prize)
        
        