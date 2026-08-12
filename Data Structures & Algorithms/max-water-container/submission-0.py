class Solution:
    def maxArea(self, heights: List[int]) -> int:
        total = len(heights) - 1
        pointer_a = 0
        pointer_b = total
        output = 0

        while pointer_a != pointer_b:
            interm_output = min(heights[pointer_a], heights[pointer_b]) * (pointer_b - pointer_a)
            output = max(output, interm_output)
            if (heights[pointer_a] < heights[pointer_b]):
                pointer_a += 1
            else:
                pointer_b -= 1
            print(interm_output)

        return output