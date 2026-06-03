class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for index, item in enumerate(nums):
            if item in nums[index + 1:]:
                return True
        return False