import sys
input = sys.stdin.readline
 
m, n = map(int, input().split())
arr = list(map(int, input().split()))
prefix_sum = [0]      
 
temp = 0    
for i in arr:    
    temp += i
    prefix_sum.append(temp)
 
for i in range(n):
    a, b = map(int, input().split())
    print(prefix_sum[b] - prefix_sum[a-1])
