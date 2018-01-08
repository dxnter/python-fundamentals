# Multiples Part I
for num in range(1001):
    if num % 2 != 0:
        print num

# Multiples Part II
for int in range(5, 1000000):
    if int % 5 == 0:
        print int

# Sum List
a = [1, 2, 5, 10, 255, 3]
sum = 0
for i in range(len(a)):
    sum += a[i]
print sum

# Average List
b = [1, 2, 5, 10, 255, 3]
sum = 0
for j in range(len(b)):
    sum += b[j]
avg = sum / len(b)
print avg