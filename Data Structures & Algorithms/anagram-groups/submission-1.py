class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict1 = {}
        for string in strs:
            alph = [0] * 26
            for char in string:
                alph[ord(char) - ord("a")] += 1
            kluch = tuple(alph)
            if kluch not in dict1:
                dict1[kluch] = []
            dict1[kluch].append(string)
        return list(dict1.values())