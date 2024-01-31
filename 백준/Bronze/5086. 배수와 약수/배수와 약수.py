# 두 수가 주어진다.
# 첫 번재 수가 두번째수의 약수일 경우 'factor'를 출력
# 배수라면 'multiple'을 출력
# 둘다 아니라면 'neither'를 출력

while True:
    n1,n2=map(int,input().split())

    if n1==0 and n2==0:
        break
    elif n2%n1==0:#약수인 경우
        print('factor')
    elif n1%n2==0: #배수인 경우
        print('multiple')
    else:#둘 다 아닌 경우
        print('neither')
