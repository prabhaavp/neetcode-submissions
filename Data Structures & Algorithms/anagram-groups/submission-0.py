class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = {}
        for index, element in enumerate(strs):
            word_l = sorted(element)
            word_s = "".join(word_l)
            if word_s not in output:
                output[word_s] = [element]
            else:
                output[word_s].append(element)
        
        ret = []
        for key, value in output.items():
            list = []
            for element in value:
                list.append(element)
            ret.append(list)

        return ret
