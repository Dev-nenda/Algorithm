# 첫 번째 줄에서 설문조사를 한 사람의 수 N
# 0 = 준희가 귀엽지 않다.
# 1 = 준희가 귀엽다.

N = int(input())

not_cute = 0
cute = 0

for _ in range(N):
    vote = int(input())

    if vote == 0:
        not_cute += 1
    else:
        cute += 1

if not_cute > cute:
    print('Junhee is not cute!')

elif cute > not_cute:
    print('Junhee is cute!')
