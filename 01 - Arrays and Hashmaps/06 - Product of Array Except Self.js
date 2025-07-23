/**
 * @param {number[]} nums
 * @return {number[]}
 */

var productExceptSelf = function (nums) {
    const newArr = [1]; //siempre el primero va a ser uno cuando calcule los pre
    const length = nums.length;
    let temp = 1;

    for (let i = 1; i < length; i++) {
        newArr.push(temp * nums[i - 1]);
        temp *= nums[i - 1];
    }

    temp = nums[length - 1];

    for (let i = length - 1; i > 0; i--) {
        newArr[i - 1] *= temp;
        temp *= nums[i - 1];
    }

    return newArr;
};
