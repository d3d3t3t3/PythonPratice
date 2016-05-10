#2016년 1월 1일은 '금요일'(0이면 일요일, 6이면 월요일)
FIRST_WEEKDAY = 5

# 이번 년도
CURRENT_YEAR = 2016

# 요일 이름
WEEKDAYS = ['Su', 'Mo', 'Tu', 'We', 'Th', 'Fr','Sa']

# 월 이름
MONTH_NAME = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

def is_leap_year(year):
    """
    이번년도가 윤년인지 체크하는 함수
    """
    return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0

def get_month_days():
    """
    월별 최대날짜 반환
    """
    return [
        31,
        28 + is_leap_year(CURRENT_YEAR),
        31,
        30,
        31,
        30,
        31,
        31,
        30,
        31,
        30,
        31,
    ]

def get_day_of_week(month, day):
    """
    [CURRENT_YEAR]년 [month]월 [day]일의 요일을 반환하는 함수
    """
    month_days = get_month_days()
    all_days = FIRST_WEEKDAY
    for i in range(1,month):
        all_days += month_days[i-1]
    all_days += day-1
    return WEEKDAYS[all_days % 7]

def print_title(year, month):
    """
    [월 이름] [CURRENT_YEAR] 출력
    """
    if month > 12 or month < 1:
        raise CalendarOutofRange(month)
    print(" " * 6 + "{month_name} {year}".format(month_name =  MONTH_NAME[month-1], year = year))

def print_weekdays():
    """
    요일 부분 출력
    """
    column = ''
    for weekday in WEEKDAYS:
        column += weekday + ' '
    print(column)

def print_calendar_format(function):
    """
    달력의 상단 부분 출력해주는 Decorator 함수
    """
    def wrapper(*args, **kwargs):
        print_title(*args, **kwargs)
        print_weekdays()
        function(*args, **kwargs)
    return wrapper

class CalendarOutofRange(Exception):
    """
    월의 범위를 벗어낫을 시 에러처리하는 클래스
    """
    def __init__(self, month):
        self.month = month

    def __str__(self):
        return "{month}월은 존재하지 않습니다.".format(month=self.month)

@print_calendar_format
def get_calendar(year, month):
    month_days = get_month_days()
    first_day_weekday = get_day_of_week(month, 1) # month월 1일의 요일
    date = 1
    first_space = ''
    for weekday in WEEKDAYS:
        if first_day_weekday == weekday:
            break
        first_space += " " * 3
    result = first_space
    while date <= month_days[month-1]:
        if date < 10:
            result += " "
        result += str(date) + " "
        if get_day_of_week(month, date) == 'Sa':
            result += '\n'
        date += 1
    print(result)

get_calendar(CURRENT_YEAR, 5)