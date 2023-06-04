def isPalindrome(self, s):
    s = s.lower()
    s = ''.join(e for e in s if e.isalnum())

    return s == s[::-1]