class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        op_lst = []
        for i in range(0,len(nums)):
            for j in range(0,i):
                if nums[i]+nums[j] == target and len(op_lst) == 0:
                    op_lst.extend([j,i])
        return op_lst