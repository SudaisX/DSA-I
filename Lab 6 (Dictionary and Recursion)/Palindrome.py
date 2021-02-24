def is_palindrome(s):
    length = len(s)
    if length <= 1:
        return True
    elif s[0] != s[-1]:
        return False
    else:
        return is_palindrome(s[1:length-1])

s = input().strip()
print(is_palindrome(s))