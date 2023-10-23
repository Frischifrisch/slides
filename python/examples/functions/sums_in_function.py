a = [2, 3, 93, 18]
b = [27, 81, 11, 35]
c = [32, 105, 1]

def calc(numbers):
    total = sum(numbers)
    return total, total / len(numbers)

total_a, avg_a = calc(a)
print(f"sum of a: {total_a} average of a: {avg_a}")

total_b, avg_b = calc(b)
print(f"sum of b: {total_b} average of b: {avg_b}")


total_c, avg_c = calc(c)
print(f"sum of c: {total_c} average of c: {avg_c}")
