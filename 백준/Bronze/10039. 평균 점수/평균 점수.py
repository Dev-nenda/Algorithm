# 40점 이상이면 자신의 성적
# 40점 미만이면 보충학습을 듣고 40점

# 5명의 점수가 주어졌을 때 평균 점수를 구하는 프로그램

total_score = 0

for _ in range(5):
    score = int(input())

    if score < 40:
        score = 40

    total_score += score

print(total_score // 5)