/**
 * @param {number[]} nums
 * @return {number[][]}
 */

var threeSum = function (nums) {
    nums.sort((a, b) => a - b);
    let index = new Map();
    let triplets = [];
    let length = nums.length;

    for (let i = 0; i < length - 2; i++) {

        if (nums[i] === nums[i - 1]) continue;
        let beg = i + 1;
        let end = length - 1;

        while (beg < end) {
            const result = nums[i] + nums[beg] + nums[end];
            if (result === 0) {
                if (!index.get(nums[i])) triplets.push([nums[i], nums[beg], nums[end]]);
                else {
                    if (
                        index.get(nums[i])[0] != nums[beg] &&
                        index.get(nums[i])[1] != nums[end]
                    ) {
                        triplets.push([nums[i], nums[beg], nums[end]]);
                    }
                }
                index.set(nums[i], [nums[beg], nums[end]]);
                end--;
                beg++;
            } 
            else if (result > 0) end--;
            else beg++;
        }
    }

    return triplets;
};
