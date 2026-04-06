class Solution {
    /**
     * @param {number[]} nums
     * @return {number[]}
     */
    getConcatenation(nums) {
        let ans = nums
        ans = ans.concat(nums)
        return ans
    }
}
