class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ret = [1] * len(nums)
        for index, item in enumerate(nums):
            for index_ret, item_ret in enumerate(ret):
                if index != index_ret:
                    ret[index_ret] *= item
        return ret