N = int(input())

for _ in range(N):
    r, e, c= map(int, input().split())

    revenue = e - c - r

    if revenue > 0:
        print('advertise')
    
    elif revenue == 0:
        print('does not matter')

    elif revenue < 0:
        print('do not advertise')