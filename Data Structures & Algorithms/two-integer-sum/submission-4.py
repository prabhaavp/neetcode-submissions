class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for index, item in enumerate(nums):
            goal = target - item
            if goal in nums[index + 1:]:
                return [index, nums[index + 1:].index(goal) + 1 + index]