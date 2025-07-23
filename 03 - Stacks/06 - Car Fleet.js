/**
 * @param {number} target
 * @param {number[]} position
 * @param {number[]} speed
 * @return {number}
 */
const carFleet = function (target, position, speed) {
    if (position.length === 1) return 1

    const index = new Map()
    const stack = []
    let res = 0

    for (const i in position) {
        const steps = (target - position[i]) / speed[i]
        index.set(position[i], steps)
    }

    position.sort((a, b) => a - b)
    for (const i in position) {
        stack.push(index.get(position[i]))
    }

    let temp
    while (stack[0]) {
        if (!temp) {
            temp = stack.pop()
            res++
            continue
        }
        const current = stack.pop()
        if (current > temp) {
            res++
            temp = current
        }
    }
    return res
}
