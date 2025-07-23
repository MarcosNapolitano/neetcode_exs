/**
 * @param {string[]} tokens
 * @return {number}
 */
var evalRPN = function (tokens) {
    let stack = [];
    let index = new Map();

    index.set("-", 1);
    index.set("+", 1);
    index.set("*", 1);
    index.set("/", 1);

    for (let i in tokens) {
        if (index.get(tokens[i])) {
            let a = stack.pop();
            let b = stack.pop();
            if (tokens[i] === "-") {
                a = `(${a})`;
                b = `(${b})`;
            }
            stack.push(Math.trunc(eval(b + tokens[i] + a)));
        } else {
            stack.push(tokens[i]);
        }

    }
    return stack[0];
};
