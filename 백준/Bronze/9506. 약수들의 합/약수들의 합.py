# 약수들의 합

# 어떤 숫자가 자신을 제외한 모든 약수들의 합과 같으면, 그 수를 완전수라 한다.
# 숫자가 완전수인지 아닌지 판단해주는 프로그램을 작성하자

while True:
    n = int(input())
    if n == -1: # 입력 값이 -1이면 반복문 종료
        break;
    divisor = []
    for i in range(1, n):
        if n % i == 0:
            divisor.append(i)
    if sum(divisor) == n:
        print(n, " = ", " + ".join(str(i) for i in divisor), sep="")
    else:
        print(n, "is NOT perfect.")