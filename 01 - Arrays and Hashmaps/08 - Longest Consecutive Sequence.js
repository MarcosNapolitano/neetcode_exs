/**
 * @param {number[]} nums
 * @return {number}
 */

var longestConsecutive = function (nums) {
    if (nums.length ===0) return 0;
    let longest = 1;
    let current = 1;

    nums.sort((a, b) => a - b);

    for (let i = 0; i < nums.length - 1; i++) {
        if (nums[i] == nums[i + 1]) continue
        if (nums[i] + 1 == nums[i + 1]) current++;
        else current = 1;
        if (current > longest) longest = current;
    }

    return longest;
};
