class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_s = set(nums)
        max = 0

        for num in nums:
            counter = 1
            if (num - 1) not in nums_s:
                curr = num
                while True:
                    curr += 1
                    if curr in nums_s: 
                        counter += 1
                    else: 
                        break
            
            if counter > max:
                max = counter
        
        return max
