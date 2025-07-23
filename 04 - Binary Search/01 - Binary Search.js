/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
const search = function (nums, target) {
    const sliceIndex = Math.floor(nums.length / 2)

    if (nums.length === 1 && nums[0] !== target) return -1
    if (nums[sliceIndex] === target) return sliceIndex

    if (nums[sliceIndex] > target) {
        return search(nums.slice(0, sliceIndex), target)
    }

    else {
        const result = search(nums.slice(sliceIndex), target)
        if (result === -1) return -1
        else return sliceIndex + result
    }
}
