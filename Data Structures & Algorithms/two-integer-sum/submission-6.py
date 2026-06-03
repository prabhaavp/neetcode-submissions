class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for index, item in enumerate(nums):
            goal = target - item
            if goal not in dict:
                dict[item] = index
            else:
                return [dict[goal], index]