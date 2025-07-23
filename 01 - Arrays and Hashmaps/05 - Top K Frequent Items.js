/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */

var topKFrequent = function (nums, k) {
    let index = new Map();

    for (let i in nums) {
        if (index.get(nums[i])) index.set(nums[i], index.get(nums[i]) + 1);
        else index.set(nums[i], 1);
    }

    const result = [...index.entries()].sort((a, b) => b[1] - a[1]).slice(0, k);
    let result2 = [];

    k--;
    while (k >= 0) {
        result2.push(result[k][0]);
        k--;
    }

    return result2;
};
