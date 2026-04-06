class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        op_lst=[]
        index=0
        while index != len(nums):
            mul=1
            for i in range(0,len(nums)):
                if index != i:
                    mul = mul * nums[i]
            op_lst.append(mul)
            index = index+1
        return op_lst