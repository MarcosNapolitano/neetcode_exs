class MinStack {
    constructor() {
        this.stack = [];
        this.min = [];
    }
    /**
    * @param {number} val
    * @return {void}
    */
    push(val) {
        this.stack.push(val);
        if (this.min.length === 0) this.min.push(val);
        else {
            if (this.getMin() >= val) this.min.push(val);
        }
    }
    /**
    * @return {void}
    */
    pop() {
        let elem = this.stack.pop();

        if (this.getMin() === elem) this.min.pop();
        return elem;
    }
    /**
    * @return {number}
    */
    top() {
        return this.stack[this.stack.length - 1];
    }
    /**
    * @return {number}
    */
    getMin() {
        return this.min[this.min.length - 1];
    }
}
