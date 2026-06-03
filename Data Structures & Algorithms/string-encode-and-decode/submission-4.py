class Solution:

    def encode(self, strs: List[str]) -> str:
        ret = ""
        if len(strs) == 0:
            return "-----"
        for word in strs:
            ret += word + "\n"
        return ret[:-1]

    def decode(self, s: str) -> List[str]:
        # ret = []
        # word = ""
        # for char in s:
        #     if char != 
        #     word += char
        if (s == "-----"):
            return []
        output = s.split("\n")
        if len(output) > 0:
            return output
       