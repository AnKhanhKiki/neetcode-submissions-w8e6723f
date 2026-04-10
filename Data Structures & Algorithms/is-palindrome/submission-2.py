class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()

        s = ''.join(c for c in s if c.isalnum())

        n = len(s)

        for i in range(0, int(n/2)):
            if s[i] != s[-i-1]:
                return False
        return True      