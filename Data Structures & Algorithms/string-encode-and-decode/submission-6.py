class Solution:

    def encode(self, strs: List[str]) -> str:
        ret = ""
        if len(strs) == 0:
            return "\0"
        for word in strs:
            ret += word + "\n\0"
        return ret[:-2]

    def decode(self, s: str) -> List[str]:
        if (s == "\0"):
            return []
        output = s.split("\n\0")
        if len(output) > 0:
            return output
       