# OX퀴즈가 있다.
# OOXXOXXOOO 와 같은 답의 결과를 보여줌
# 해당 점수는 O의 연속된 갯수의 합

T = int(input())

for _ in range(T):
    answer = list(input())

    score = 0
    total = 0
    
    for ox in answer:
        if ox == 'O':
            score += 1
            total += score

        else:
            score =0
    print(total)