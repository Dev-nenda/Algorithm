# 같은 눈이 3개 나오면 10,000 + (같은눈)x1000
# 같은 눈이 2개 나오면 1000 + (같은 눈)x100
# 모두 다른 눈 (그 중 가장 큰 눈)x100

T = int(input())
answer = 0

for _ in range(T):
    a, b, c = map(int, input().split())
    
    if a == b == c:
        answer = max(answer, 10000+a*1000)
    elif a == b:
        answer = max(answer, 1000+a*100)
    elif a == c:
        answer = max(answer, 1000+a*100)
    elif b == c:
        answer = max(answer, 1000+b*100)
    else:
        answer = max(answer, 100 * max(a,b,c))

print(answer)
        