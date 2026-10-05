class Solution:
    def isValid(self, s: str) -> bool:
        hashmap = {')': '(', ']': '[', '}': '{'}
        curr_condition = []
        for element in s:
            if element not in hashmap:
                curr_condition.append(element)
            else:
                if curr_condition and hashmap[element] == curr_condition[-1]:
                    curr_condition.pop()
                else:
                    return False
        return not curr_condition