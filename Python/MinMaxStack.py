# This file should provides an upgraded stack class that keeps track of the
# minimum and maximum values in the stack so that you can always determine
# those values in O(1) time!


# TODO: Add an "empty" method, and array parameter to constructor
class MinMaxStack():
    def __init__(self):
        self.minStack = []
        self.maxStack = []
        self.mainStack = []

    # adds a given value to the stack, and possibly to the min/max stacks
    # as required
    def push(self, val):
        self.mainStack.append(val)

        #add value to minStack if minStack is empty or if the value represents
        # a minimum value on the stack
        if(len(self.minStack) == 0 or (len(self.minStack) > 0 and val <= self.getMin())):
            self.minStack.append(val)

        #add value to maxStack if maxStack is empty or if the value represents
        # a maximum value on the stack
        if(len(self.maxStack) == 0 or (len(self.maxStack) > 0 and val >= self.getMax())):
            self.maxStack.append(val)


    def removeTop(self):
        #guard statement for empty stack
        if(len(self.mainStack) == 0):
            return None

        removed = self.mainStack.pop()

        # remove minimum value if value to be removed is a minimum (top of minStack)
        if(removed == self.minStack[-1]):
            self.minStack.pop()

        # remove maximum value if value to be removed is a maximum (top of maxStack)
        if(removed == self.maxStack[-1]):
            self.maxStack.pop()

        return removed


    # returns the maximum value on the stack in O(1) time
    # or None if stack is empty
    def getMax(self):
        #guard statement for empty stack
        if(len(self.mainStack) == 0):
            return None

        return self.maxStack[-1]

    # returns the minimum value on the stack in O(1) time
    # or None if stack is empty
    def getMin(self):
        #guard statement for empty stack
        if(len(self.mainStack) == 0):
            return None

        return self.minStack[-1]



# Example Implementation
if __name__ == "__main__":
    testStack = MinMaxStack()

    testStack.push(5)
    testStack.push(4)
    testStack.push(3)
    testStack.push(4)
    testStack.push(5)

    # stack is [5, 4, 3, 4, 5]
    print(testStack.getMin(), testStack.getMax())

    testStack.removeTop()

    # stack is [5, 4, 3, 4]
    print(testStack.getMin(), testStack.getMax())

    testStack.removeTop()
    testStack.removeTop()

    #stack is [5, 4]
    print(testStack.getMin(), testStack.getMax())

    testStack.push(7)
    testStack.push(2)
    testStack.push(4)

    #stack is [5, 4, 7, 2, 4]
    print(testStack.getMin(), testStack.getMax())

    testStack.removeTop()
    testStack.removeTop()
    testStack.removeTop()
    testStack.removeTop()
    testStack.removeTop()

    #stack is []
    print(testStack.getMin(), testStack.getMax())
