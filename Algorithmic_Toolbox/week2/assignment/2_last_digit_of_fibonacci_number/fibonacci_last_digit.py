# Uses python3
import sys

def get_fibonacci_last_digit_naive(n):
    array = [None] * (n + 1)

    if n < 1:
        return n

    array[0] = 0
    array[1] = 1


    for i in range(2, n + 1):
        array[i] = (array[i - 1] + array[i - 2]) % 10
    return array[n]

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    # n = int(input())
    print(get_fibonacci_last_digit_naive(n))
