
def swap(txt):
    '''
    >>> half("abcd"))
    cdab
    '''
    return txt[len(txt) // 2:] + txt[:len(txt) // 2]

def average(*numbers):
    '''
    >>> average(2, 4, 6)
    4
    '''
    s = 0
    c = 0
    for n in numbers:
        s += n
        c += 1
    return s/c

