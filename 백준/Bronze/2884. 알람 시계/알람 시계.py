# 첫째줄에 두 정수 H와 M이 주어진다.
# 입력시간은 24시간 표현을 사용
# 45분 일찍 알람설정하기

H, M = map(int, input().split())

if M -45 < 0:
    if H == 0:
        H = 23
        M += 60
    else: 
        H -= 1
        M += 60

print(H, M-45)