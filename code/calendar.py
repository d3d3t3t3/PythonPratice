import datetime

# 요일 이름
WEEKDAYS = ['Su', 'Mo', 'Tu', 'We', 'Th', 'Fr','Sa']

# 이번년도가 윤년인지 체크
def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0

# 월 이름, 월 기간 설정
def set_month_data(year):
    return [
                ['Jan', 31],
                ['Feb', 28 + is_leap_year(year)],
                ['Mar', 31],
                ['Apr', 30],
                ['May', 31],
                ['Jun', 30],
                ['Jul', 31],
                ['Aug', 31],
                ['Sep', 30],
                ['Oct', 31],
                ['Nov', 30],
                ['Dec', 31],
            ]

def print_weekdays():
    ret = ''
    for weekday in WEEKDAYS:
        ret += weekday + ' '
    print(ret)

def get_calendar(year, month):
    month_data = set_month_data(year)
    first_day_weekday = (datetime.date(year, month, 1).weekday() + 1) % 7 # month월 1일의 요일의 정수값 (0이면 일요일, 6이면 월요일)
    print("      {month} {year}".format(month = month_data[month-1][0], year = year))
    print_weekdays()
    result = ""
    i = 0
    date = 1
    while date <month_data[month-1][1]+1:
        if i < first_day_weekday:
            result += "   "
        else:
            if date < 10:
                result += " "
            result += str(date) + " "
            date += 1
        i += 1
        if i % 7 == 0:
            result += '\n'
    print(result)

get_calendar(2015, 5)
