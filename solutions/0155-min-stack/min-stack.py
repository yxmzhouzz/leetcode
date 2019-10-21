# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
#
#
# 	push(x) -- Push element x onto stack.
# 	pop() -- Removes the element on top of the stack.
# 	top() -- Get the top element.
# 	getMin() -- Retrieve the minimum element in the stack.
#
#
#  
#
# Example:
#
#
# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin();   --> Returns -3.
# minStack.pop();
# minStack.top();      --> Returns 0.
# minStack.getMin();   --> Returns -2.
#
#
#  
#


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minele = []
        

    def push(self, x: int) -> None:
        
        self.stack.append(x)
        
        # !!! if minele is popped, the minele should be updated
        # so need another list to store the min till the current position
        if not self.minele or x < self.minele[-1]:
            self.minele.append(x)
        else:       # if new element is not min, then let current = previous element
            self.minele.append(self.minele[-1])
        

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()
            self.minele.pop()  # don't forget

    def top(self) -> int:
        if not self.stack:
            return None
        else:
            return self.stack[-1]

    def getMin(self) -> int:
        return self.minele[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
