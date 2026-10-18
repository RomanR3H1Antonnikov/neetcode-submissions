class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        set_filter = set()
        L = R = 0
        max_len = 0
        while R < len(s):
            while s[R] in set_filter:
                set_filter.remove(s[L])
                L += 1
            set_filter.add(s[R])
            R += 1
            max_len = max(len(set_filter), max_len)
        return max_len