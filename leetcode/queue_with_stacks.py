# https://leetcode.com/problems/implement-queue-using-stacks/description/
# https://leetcode.com/articles/implement-queue-using-stacks/


class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack1 = []
        self.stack2 = []
        

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        self.stack1.append(x)
        

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        if self.stack1 and not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        temp = self.stack2.pop()
        while self.stack2:
            self.stack1.append(self.stack2.pop())
        return temp
            
        
    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if self.stack1 and not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        temp = self.stack2[-1]
        while self.stack2:
            self.stack1.append(self.stack2.pop())
        return temp

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        if self.stack1 or self.stack2:
            return False
        return True


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()