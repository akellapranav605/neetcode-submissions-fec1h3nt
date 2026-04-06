class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        op_val = False
        for number in nums:
            if nums.count(number) > 1:
                op_val = True
        return op_val