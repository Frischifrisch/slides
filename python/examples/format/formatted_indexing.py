txt = "Foo Bar"
num = 42.12

print(f"The user {txt} was born {num} years ago.")
print("The user {0} was born {1} years ago.".format(txt, num))
print("The user {1} was born {0} years ago.".format(num, txt))


print("{0} is {0} and {1} years old.".format(txt, num))
