import time


def create_pair():
    b = {'name' : 'Bar'}
    a = {'name': 'Foo', 'pair': b}
    b['pair'] = a
    #print(a)


for _ in range(1, 30000000):
    create_pair()

print("let's sleep now a bit")
time.sleep(20)
