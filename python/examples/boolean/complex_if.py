age = 16
name = "Foo"

if 0 < age <= 18:
    print("age is bewteen 0 and 18")
else:
    print("age is NOT between 0 and 18")

if age < 18 or age > 65:
    print("Young or old")
else:
    print("Working age")


if age < 18 and name != "Foo":
    print("True")
else:
    print("False")

