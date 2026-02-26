/**
 * @param {number[]} nums
 * @param {number} k
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var rotate = function(nums, k) {
    if(nums.length <= 1 || k <= 0){
        return nums;
    }

    k = k % nums.length;
    console.log(k)
    nums.splice(0, 0, ...nums.splice(nums.length - k)); // remove last k elements and add them to the beginning of the array
    return nums;
};

console.log(rotate([1, 2, 3, 4, 5, 6, 7], 3)); // [5, 6, 7, 1, 2, 3, 4]
console.log(rotate([-1, -100, 3, 99], 2)); // [3, 99, -1, -100]
console.log(rotate([1, 2], 3)); // [2, 1]