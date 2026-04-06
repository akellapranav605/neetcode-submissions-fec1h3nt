class Solution {
    /**
     * @param {number[]} nums
     * @param {number} val
     * @return {number}
     */
    removeElement(nums, val) {
        let nums_arr = nums.filter((n) => n!= val)
        for(let i =0;i<nums_arr.length;i++){
            nums[i]=nums_arr[i]
        }
        return nums_arr.length;
    }
}
