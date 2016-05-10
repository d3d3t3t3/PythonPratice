def make_fibonacci_set(n):
    """
    n보다 작거나 같을 때까지 [[0, 0], [1, 1], [2, 1], [3, 2], [5, 3] ...] 2차원 배열 생성
    """
    fibonacci_set = []
    fibonacci_set.append([0, 0])
    fibonacci_set.append([1, 1])
    key = 1
    value = 1
    while key + value <= n:
        key, value = key + value, key
        key_value_set = [key, value]
        fibonacci_set.append(key_value_set)
    return fibonacci_set

class PeopleShouldnotNegative(Exception):
    """
    사람의 수를 음수일 때 에러처리하는 클래스
    """
    def __init__(self):
        pass

    def __str__(self):
        return "사람의 수가 음수일 수는 없습니다."

def fibonachicken(n):
    if n < 0:
        raise PeopleShouldnotNegative()
    fibonacci_set = make_fibonacci_set(n)
    index =len(fibonacci_set)-1 # fibonacci_set 배열의 마지막에서부터 탐색하기 위해 초기화
    ret = 0
    while n != 0:
        if n >= fibonacci_set[index][0]:
            n -= fibonacci_set[index][0]
            ret += fibonacci_set[index][1]
        index -= 1
    return ret

fibonachicken(16)