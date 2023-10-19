
var MinStack = function() {
    this.newObject = [];
};

/** 
 * @param {number} val
 * @return {void}
 */
MinStack.prototype.push = function(val) {
    this.newObject.push(val)
};

/**
 * @return {void}
 */
MinStack.prototype.pop = function() {
    this.newObject.pop();
};

/**
 * @return {number}
 */
MinStack.prototype.top = function() {
    return this.newObject[this.newObject.length - 1];
};

/**
 * @return {number}
 */
MinStack.prototype.getMin = function() {
    return Math.min(...this.newObject);
};

/** 
 * Your MinStack object will be instantiated and called as such:
 * var obj = new MinStack()
 * obj.push(val)
 * obj.pop()
 * var param_3 = obj.top()
 * var param_4 = obj.getMin()
 */
