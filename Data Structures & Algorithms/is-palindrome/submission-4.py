class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        L, R = 0, len(s) - 1
        while L < R:
            print(s[L], s[R])
            if not s[L].isalnum() and s[R].isalnum():
                L += 1
                continue
            elif s[L].isalnum() and not s[R].isalnum():
                R -= 1
                continue
            elif not s[L].isalnum() and not s[R].isalnum():
                L += 1
                R -= 1
                continue
            if s[L] != s[R]:
                return False
            L += 1
            R -= 1
        return True