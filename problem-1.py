# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.
x = 3
y = 5
soma = 0
arr_x = []
for x in range(0, 1000):
    diff_x = x % 3
    diff_y = x % 5
    if diff_x == 0 or diff_y == 0:
        soma =+ x
        arr_x.append(x)
print("the sum is", sum(arr_x))

