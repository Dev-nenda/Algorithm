# A와 B가 한 오디션 프로의 결승전에 진출했다.
# 결승전의 승자는 심사위원의 투표로 결정된다.

# 첫째 줄에는 심사위원의 수  V
# 둘째 줄에는 심사위원이 누구에게 투표했는지 주어진다.

V = int(input())

Vote_list = list(str(input()))

A = 0
B = 0

for i in range(V):
    if Vote_list[i] == 'A':
        A += 1
    else:
        B += 1
    
if A > B:
    print('A')
elif B > A:
    print('B')
else:
    print('Tie')
