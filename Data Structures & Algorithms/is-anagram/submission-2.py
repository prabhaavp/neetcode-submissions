class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        list_t = list(t)
        try:
            for index, item in enumerate(s):
                list_t.remove(item)
        except:
            return False
        return len(list_t) == 0