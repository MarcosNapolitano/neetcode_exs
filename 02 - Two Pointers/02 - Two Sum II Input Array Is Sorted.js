/**
 * @param {number[]} numbers
 * @param {number} target
 * @return {number[]}
 */

var twoSum = function (numbers, target) {

    let end = numbers.length - 1;
    let beg = 0;

    while (beg != end) {
        let current = target - numbers[beg];
        if (current < numbers[end]) end--;
        else if (current === numbers[end]) break;
        else beg++;
    }

    return [beg + 1, end + 1];
};
