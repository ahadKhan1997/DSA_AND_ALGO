// let stack = stack || [];
// stack.push(1);
// stack.pop();
// stack.peek();
// stack.isEmpty();
// stack.size();


class Stack {
    constructor() {
        this.stack = [];
    }
    push(value) {
        this.stack.push(value);
    }

    pop() {
        if(this.stack.length === 0) return null;
        return this.stack.pop();
    }

    peek() {
        if(this.stack.length === 0) return null;
        return this.stack[this.stack.length - 1];
    }

    isEmpty() {
        return this.stack.length === 0;
    }

    size() {
        return this.stack.length;
    }
}

const stack = new Stack();
stack.push(1);
stack.push(2);
stack.push(3);
console.log(stack.peek()); // 3
console.log(stack.pop()); // 3
console.log(stack.peek()); // 2
console.log(stack.isEmpty()); // false
console.log(stack.size()); // 2