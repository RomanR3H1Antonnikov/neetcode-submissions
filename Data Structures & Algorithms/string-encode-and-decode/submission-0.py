class Solution:

    def encode(self, strs: List[str]) -> str:
        strslist = []
        for element in strs:
            strslist.append(f"{len(element)}#{element}")
        strslist = "".join(strslist)
        return strslist

    def decode(self, s: str) -> List[str]:
        anslist = []
        while s:
            length = int(s[:s.index("#")])
            anslist.append(s[s.index("#") + 1:s.index("#") + length + 1])
            s = s[s.index("#") + length + 1:]
        return anslist