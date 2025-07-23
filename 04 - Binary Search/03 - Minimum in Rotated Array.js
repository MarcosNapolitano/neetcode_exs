/**
 * @param {number[]} nums
 * @return {number}
 */
var findMin = function(nums) {
  let l = 0;
  let r = nums.length - 1;
  let half = Math.floor((l + r) / 2);

  while (l < r) {
    if (nums[half] > nums[l] && nums[half] > nums[r]) l = half;
    else if (nums[half] < nums[l] && nums[half] < nums[r]) r = half;
    else if (nums[half] > nums[l] && nums[half] < nums[r]) r = half;

    half = Math.floor((l + r) / 2);
    if (half === l || half === r) return Math.min(nums[l], nums[r]);
  }
  return nums[half];
};
