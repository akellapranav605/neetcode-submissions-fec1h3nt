class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
        let index_arr=[];
        for(let i=0; i<nums.length; i++){
            for(let j=i+1; j<nums.length; j++){
                if(nums[i]+nums[j] === target){
                    index_arr.push(i,j);
                }
            }
        }
        return index_arr;
    }
}
