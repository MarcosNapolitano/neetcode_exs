/**
 * @param {number[]} height
 * @return {number}
 */

var maxArea = function (height) {
    let end = height.length - 1;
    let beg = 0;
    let result = 0;

    while (beg < end) {
        const current = Math.min(height[beg], height[end]) * (end - beg);
        if (current > result) result = current;

        if (height[beg] < height[end]) beg++;
        else end--;
    }
    return result;
};
