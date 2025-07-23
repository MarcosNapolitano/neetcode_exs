/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var search = function(arr, target) {
    let left = 0;
    let right = arr.length - 1;
    let half = Math.floor((left + right) / 2);

    if ((left === right) & (arr[left] !== target)) return -1;
    else if ((left === right) & (arr[left] === target)) return left;

    const recursive = function (l, r, h) {
        if ((r - l === 1) & (arr[l] !== target) & (arr[r] !== target)) return -1;
        if (arr[l] === target) return l;
        if (arr[r] === target) return r;
        if (arr[h] === target) return h;

        if (arr[l] < arr[h]) {
            if (arr[l] < target && target < arr[h]) r = h;
            else l = h;
        } else {
            if (arr[h] < target && target < arr[r]) l = h;
            else r = h;
        }

        h = Math.floor((l + r) / 2);
        return recursive(l, r, h);
    };
    return recursive(left, right, half);
};
