/**
 * @param {number[][]} matrix
 * @param {number} target
 * @return {boolean}
 */
const searchMatrix = function (matrix, target) {
    let correctArr
    for (const i in matrix) {
        if (target >= matrix[i][0] && target <= matrix[i][matrix[i].length - 1]) {
            correctArr = matrix[i]
            break
        } else {
            continue
        }
    }
    if (!correctArr) return false

    const binary = function (arr, target) {
        const sliceIndex = Math.floor(arr.length / 2)
        if (arr.length === 1 && arr[0] !== target) return false
        if (target === arr[sliceIndex]) return true
        if (target > arr[sliceIndex]) return binary(arr.slice(sliceIndex), target)
        if (target < arr[sliceIndex]) {
            return binary(arr.slice(0, sliceIndex), target)
        }
    }
    return binary(correctArr, target)
}
