class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        L = 0
        count1 = {}
        count2 = {}
        res_len = float('inf')
        res_L = 0
        have = 0
        need = len(set(t))
        for i in t:
            count1[i] = count1.get(i, 0) + 1
        for R in range(len(s)):
            idx = s[R]
            count2[idx] = count2.get(idx, 0) + 1
            if count2[idx] == count1.get(idx, 0):
                have += 1
            while have == need:
                if R - L + 1 < res_len:
                    res_len = R - L + 1
                    res_L = L
                idx = s[L]
                count2[idx] = count2.get(idx, 0) - 1
                L += 1
                if count2[idx] == count1.get(idx, 0) - 1:
                    have -= 1

        return s[res_L: res_L + res_len] if res_len != float('inf') else ""