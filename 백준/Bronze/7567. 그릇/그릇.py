# '('은 정방향 ')'은 역방향

# 같은 방향 + 5, 다른 방향 +10
# 기존 높이 10

dish = list(str(input()))
high = 0

for i in range(len(dish)):
    if i == 0:
        high += 10
    elif dish[i] == dish[i-1]:
        high += 5
    else:
        high += 10
        
print(high)