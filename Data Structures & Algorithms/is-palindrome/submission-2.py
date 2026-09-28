class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(char for char in s if char.isalnum()).lower()
        L, R = 0, len(s) - 1
        for i in range(len(s)):
            if s[L + i] != s[R - i]:
                return False
        return True