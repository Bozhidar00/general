n = int(input())

sum1 = 0
sum2 = 0

for i in range(0, n*2):
    m = int(input())
    if i <= n:
        sum1 = sum2 + m
    elif i >= n:
        sum2 = sum2 + m

if sum1 == sum2:
    print(f'Yes, sum = {sum1}')
else:
    print(f"No, diff = {abs(sum1 - sum2)}")
