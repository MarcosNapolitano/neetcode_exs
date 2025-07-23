/**
 * @param {string} s
 * @return {boolean}
 */

var isPalindrome = function(s) {
    s = s.replace(/\W/g, "").replace(/_/, "").toLowerCase();
    let length = s.length - 1;

    for (let i in s) {
        if (i === length) break;
        if (s[i] === s[length]) {
            length--;
            continue;
        }
        return false;
    }

    return true;
};
