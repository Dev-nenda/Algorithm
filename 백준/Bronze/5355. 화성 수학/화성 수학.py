T = int(input())

for _ in range(T):
    mars = list(map(str, input().split()))
    answer = 0
    
    for i in range(len(mars)):
        if i == 0:
            answer += float(mars[i])
        else:
            if mars[i] == '@':
                answer *= 3
            elif mars[i] == '%':
                answer += 5
            elif mars[i] == '#':
                answer -= 7
    # %는 문자열안에 변수 값을 포매팅할 때 사용
    # '0.2f' 부분은 소수점 형식을 지정
    print('%0.2f' % answer)

                
    