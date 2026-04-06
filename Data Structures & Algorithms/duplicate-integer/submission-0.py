class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        bool_arr = []
        for i in nums:
            if nums.count(i) > 1:
                bool_arr.append(True)
            else:
                bool_arr.append(False)
        if bool_arr.count(True) > 0:
            return bool(True)
        else:
            return bool(False)