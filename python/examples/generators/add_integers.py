from series import integers

def mysum(nums):
    print(nums)
    return sum(nums)

n3 = integers(3)
n7 = integers(7)
d = ( mysum(p) for p in zip(n3, n7) )

print("start")
for i in d:
    print(i)
    if i >= 20:
        break
