def is_palindrome(s):
    if s == '':
        return True
    return is_palindrome(s[1:-1]) if s[0] == s[-1] else False

def iter_palindrome(s):
    return all(s[i] == s[-(i+1)] for i in range(0, len(s) // 2))

print(is_palindrome(''))      # True
print(is_palindrome('a'))     # True
print(is_palindrome('ab'))    # False
print(is_palindrome('aa'))    # True
print(is_palindrome('aba'))   # True
print(is_palindrome('abc'))   # False

print()
print(iter_palindrome(''))      # True
print(iter_palindrome('a'))     # True
print(iter_palindrome('ab'))    # False
print(iter_palindrome('aa'))    # True
print(iter_palindrome('aba'))   # True
print(iter_palindrome('abc'))   # False
