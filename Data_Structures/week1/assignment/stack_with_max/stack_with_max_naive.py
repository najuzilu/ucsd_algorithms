#python3
import sys

class StackWithMax():
    def __init__(self):
        self.__stack = []
        self.maxcache = []

    def Push(self, a):
        if len(self.maxcache) == 0:
            self.maxcache.append([a, 1])
        else:
            latest_cached = self.maxcache[-1]
            if latest_cached[0] == a:
                latest_cached[1] = latest_cached[1] + 1
            elif latest_cached[0] < a:
                self.maxcache.append([a, 1])
        self.__stack.append(a)

    def Pop(self):
        assert(len(self.__stack))
        latest_cached = self.maxcache[-1]
        stack_pop = self.__stack.pop()
        if stack_pop == latest_cached[0]:
            if latest_cached[1]-1 == 0:
                self.maxcache.pop()
            else:
                latest_cached[1] = latest_cached[1] - 1

    def Max(self):
        assert(len(self.__stack))
        return self.maxcache[-1][0]


if __name__ == '__main__':
    stack = StackWithMax()

    num_queries = int(sys.stdin.readline())

    for _ in range(num_queries):
        query = sys.stdin.readline().split()

        if query[0] == "push":
            value = int(query[1])
            stack.Push(value)
        elif query[0] == "pop":
            pop_value = stack.Pop()
        elif query[0] == "max":
            print(stack.Max())
        else:
            assert(0)
