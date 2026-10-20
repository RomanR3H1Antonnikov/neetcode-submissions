class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        L, R = 0, len(s1) - 1
        count1 = [0] * 26
        for i in s1:
            count1[ord(i) - ord('a')] += 1
        count2 = [0] * 26
        for i in range(L, R + 1):
            count2[ord(s2[i]) - ord('a')] += 1
        matches = 0
        for i in range(26):
            if count1[i] == count2[i]:
                matches += 1
        if matches == 26:
            return True
        while R < len(s2) - 1:
            R += 1
            idx = ord(s2[R]) - ord('a')
            count2[idx] += 1
            if count2[idx] == count1[idx]:
                matches += 1
            elif count2[idx] - 1 == count1[idx]:
                matches -= 1
            idx = ord(s2[L]) - ord('a')
            count2[idx] -= 1
            L += 1
            if count2[idx] == count1[idx]:
                matches += 1
            elif count2[idx] + 1 == count1[idx]:
                matches -= 1
            if matches == 26:
                return True
        return False