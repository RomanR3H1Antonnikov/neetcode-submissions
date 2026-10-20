class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        L = R = 0
        count = [0] * 26
        res = 0
        max_count = 0
        while R < len(s):
            count[ord(s[R]) - ord('A')] += 1
            max_count = max(max_count, count[ord(s[R]) - ord('A')])
            while R - L + 1 - max_count > k:
                count[ord(s[L]) - ord('A')] -= 1
                L += 1
            res = max(res, R - L + 1)
            R += 1
        return res