n = int(input())

even_sum = 0
odd_sum = 0
for i in range(1, n+1):
    num = int(input())
    if i % 2 == 1:
        odd_sum += num
    elif i % 2 ==0:
        even_sum += num
if even_sum == odd_sum:
    print("Yes")
    print(f"Sum = {even_sum}")
elif even_sum != odd_sum:
    print("No")
    print(f"Diff = {odd_sum}")
