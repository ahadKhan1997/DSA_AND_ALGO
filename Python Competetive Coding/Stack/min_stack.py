"""
155. Min Stack
Solved
Medium
Topics
premium lock icon
Companies
Hint
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

MinStack() initializes the stack object.
void push(int value) pushes the element value onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
You must implement a solution with O(1) time complexity for each function.

 

Example 1:

Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output
[null,null,null,null,-3,null,0,-2]

Explanation
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2
 

Constraints:

-231 <= val <= 231 - 1
Methods pop, top and getMin operations will always be called on non-empty stacks.
At most 3 * 104 calls will be made to push, pop, top, and getMin.
"""

class MinStack(object):

    def __init__(self):
        self.stack = []

    def push(self, value):
        """
        :type value: int
        :rtype: None
        """
        if not self.stack:
            # If stack is empty, value is the current minimum
            self.stack.append([value, value])
        else:
            # Look at the previous element's recorded min
            current_min = self.stack[len(self.stack) - 1][1]
            # Push the value along with the updated minimum
            self.stack.append([value, min(value, current_min)])

    def pop(self):
        """
        :rtype: None
        """
        # Simply pop. The previous min is automatically restored 
        # because it's safely embedded in the element below it!
        self.stack.pop()

    def top(self):
        """
        :rtype: int
        """
        # Direct Python shorthand syntax for self.stack[-1][0]
        return self.stack[-1][0] if self.stack else "NA"

    def getMin(self):
        """
        :rtype: int
        """
        # Look at the minimum tracked by the top item instantly
        return self.stack[len(self.stack) - 1][1] if self.stack else "NA"

# Your MinStack object will be instantiated and called as such:

obj = MinStack()
obj.push(2)
obj.pop()
param_3 = obj.top()
param_4 = obj.getMin()
print("top: ", param_3)
print("min: ", param_4)