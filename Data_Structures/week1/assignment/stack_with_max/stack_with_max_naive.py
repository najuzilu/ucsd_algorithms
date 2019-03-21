#python3
import sys

class StackWithMax():
    def __init__(self):
        self.__stack = []

    def Push(self, a):
        self.__stack.append(a)

    def Pop(self):
        assert(len(self.__stack))
        self.__stack.pop()

    def Max(self):
        assert(len(self.__stack))
        return max(self.__stack)

class MaxCache():
    def __init__(self):
        self.__stack = []

    def Push(self, a):
        self.__stack.append(a)

    def Pop(self):
        assert(len(self.__stack))
        self.__stack.pop()



if __name__ == '__main__':
    stack = StackWithMax() # initialize stack class
    max_stack = MaxValues() # initialize max stack class for max values in order

    max_val = 0 # initialize max value at the begining

    num_queries = int(sys.stdin.readline())

    for _ in range(num_queries):
        query = sys.stdin.readline().split()

        if query[0] == "push":
            value = int(query[1])
            if value > max_val:
                max_value = value
                max_stack.Push(max_value)
            stack.Push(value)

        elif query[0] == "pop":
            pop_value = stack.Pop()
            if pop_value == max_value:


        elif query[0] == "max":
            print(stack.Max())

        else:
            assert(0)
