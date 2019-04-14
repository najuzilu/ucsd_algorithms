# Uses python3
import sys

def calc_fib(n):
    array = [None] * (n + 1)
    if n == 0:
        return 0
    array[0] = 0
    array[1] = 1
    for i in range(2, n + 1):
        array[i] = array[i - 1] + array[i - 2]
    return array[n]

def get_fibonacci_huge(n, m):
    length_cycle = m**2 - 1
    remainder = n % length_cycle
    return calc_fib(remainder) % m

if __name__ == '__main__':
    input = input()
    # input = sys.stdin.read()
    n, m = map(int, input.split())
    print(get_fibonacci_huge(n, m))
