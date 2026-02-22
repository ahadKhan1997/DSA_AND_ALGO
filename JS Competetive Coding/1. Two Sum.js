/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    let temp = [];
    /**solution 1 LEAST OPTIMAL*/
    // for ( let i = 0; i < nums.length; i++) {
    //     for ( let j = i + 1; j < nums.length; j++) {
    //         if ( nums[i] + nums[j] === target) {
    //             temp.push(i);
    //             temp.push(j);
    //             return temp;
    //         }
    //     }
    // }

    /**solution 2 OPTIMAL*/
    // for ( let i = 0; i < nums.length; i++) {
    //     let complement = target - nums[i];
    //     if ( temp[complement] !== undefined) {
    //         return [temp[complement], i];
    //     }
    //     temp[nums[i]] = i;
    // }

    /**solution 3 MOST OPTIMAL*/
    let obj = {};
    for ( let i = 0; i < nums.length; i++) {
        let n = nums[i]
        if(obj[target - n] != undefined) {
            return [obj[target - n], i]
        } else {
            obj[n] = i
        }
    }
}
console.log(twoSum([2,7,11,15], 9));
