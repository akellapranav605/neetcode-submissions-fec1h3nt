class Solution {
    /**
     * @param {string[]} strs
     * @return {string[][]}
     */
     

    groupAnagrams(strs) {

        function sort(word) {
            return word.toLowerCase().split('').sort().join("");
        } 

        let dummy_arr = [];
        let op_arr=[];
        for(let i=0; i<strs.length; i++){
            dummy_arr.push(sort(strs[i]));
        }
        let unique_words = new Set(dummy_arr);
        for(const x of unique_words) {
            let new_arr = [];
            for(let i=0;i<strs.length;i++){
                if(x===dummy_arr[i]){
                    new_arr.push(strs[i]);
                }
            }
            if(new_arr.length ===0){
                op_arr.push(x)
            }
            else{
                op_arr.push(new_arr)
            }
        }
        return op_arr;
    }
}
