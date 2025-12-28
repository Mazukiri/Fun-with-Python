def oddNumbers(numbers):
    for number in range(1, numbers + 1, 2):
        print(number)
    

# Lặp biết trước số lần và lặp không biết trước số lần

#times: 0 -> 9 

    
# In các số lẻ từ 1 -> n. N nhập vào

# n = int(input())

# sumOfDivisors = 0

# 12
# sum = sum + divisor
# 1 + 2 + 3 + 4 + 6 + 12

# for divisor in range(1, n + 1):
#     if n % divisor == 0:
#         sumOfDivisors = sumOfDivisors + divisor

# print(sumOfDivisors)
    
# a = int(input())
# b = int(input())

# prod = 1

# for number in range(a, b + 1):
#     if number % 3 == 0:
#         prod *= number
        
# print(prod)

n = int(input())

# 5 * 1 = 5
# 5 * 2 = 10
# ...
# 5 * 10 = 50

# BTVN tuan nay: 
# 1. Cho so n. In ra cac so nguyen to trong doan 1 -> n. VI du: n = 10 -> In ra: 2,3,5,7
# 2. Cho so n. In ra n so fibonanci dau tien: n = 5 -> 1 1 2 3 5
# 3. (Lam bang 2 cach): cho so a, b. Tinh tong cac so chia het cho 5 trong khoang a, b.

for i in range(1, 11):
    print(f'{n} * {i} = {n * i}')
    
    