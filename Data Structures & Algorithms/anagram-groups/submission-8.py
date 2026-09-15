class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict1 = {}
        for string in range(len(strs)):
            alph = [0] * 26
            for char in strs[string]:
                alph[ord(char) - ord("a")] += 1
            kluch = tuple(alph)
            if kluch not in dict1:
                dict1[kluch] = []
            dict1[kluch].append(strs[string])
        return list(dict1.values())