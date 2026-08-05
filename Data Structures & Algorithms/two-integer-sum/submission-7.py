class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for index, item in enumerate(nums):

            if item in d:
                return [d[item], index]
            else:
                complement = target - item
                d[complement] = index
        return []