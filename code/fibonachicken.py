def fibonacci(number):
    if number == 0 or number == 1:
        return number
    return fibonacci(number-1) + fibonacci(number-2)

# n보다 작거나 같을 때까지의 fibonacci 배열 생성하는 함수
# ex) n = 5 => [0, 1, 1, 2, 3, 5]
# ex) n = 15 => [0, 1, 1, 2, 3, 5, 8, 13]
def make_fibonacci_list(n):
    fibonacci_list = []
    i = 0
    while fibonacci(i) <= n:
        fibonacci_list.append(fibonacci(i))
        i += 1
    return fibonacci_list

def fibonachicken(n):
    fibonacci_list = make_fibonacci_list(n) # n보다 작거나 같을 때까지의 fibonacci 배열 생성
    i =len(fibonacci_list)-1 # fibonacci 배열의 마지막에서부터 탐색하기 위해 초기화
    ret = 0
    while n != 0:
        if n >= fibonacci_list[i]:
            n -= fibonacci_list[i]
            ret += fibonacci_list[i-1]
        i -= 1
    return ret