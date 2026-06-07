def least_difference(a, b, c):
    diff_1 = abs(a - b)
    diff_2 = abs(a - c)
    diff_3 = abs(b - c)
    return min(diff_1, diff_2, diff_3)

print(least_difference(10, 11, 10.5))