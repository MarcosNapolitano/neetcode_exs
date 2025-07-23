var dailyTemperatures = function (temperatures) {
    let stack = [];
    let res = [];

    for (let i = 0; i < temperatures.length; i++) {
        stack.unshift(i);
        const next = temperatures[i + 1];

        if (!next) {
            while (stack[0]) {
                res[stack.pop()] = 0;
            }
        }

        while (next > temperatures[stack[0]]) {
            const index = stack.shift();
            res[index] = i + 1 - index;
        }
    }
    return res;
};
