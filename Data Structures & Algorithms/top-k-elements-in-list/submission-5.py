class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        op_lst = []
        unique_nums = list(set(nums))
        unique_num_dict = {}
        for unique_num in unique_nums:
            unique_num_dict[unique_num] = nums.count(unique_num)
        for i in range(0,len(unique_nums)):
            for j in range(i, len(unique_nums)):
                if unique_num_dict.get(unique_nums[i])<unique_num_dict.get(unique_nums[j]):
                    temp_a = unique_nums[i]
                    temp_b = unique_nums[j]
                    unique_nums[i] = temp_b
                    unique_nums[j] = temp_a
        return unique_nums[:k]