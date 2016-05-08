#2016년 1월 1일은 '금요일'
import datetime

weekday = ['금', '토', '일', '월', '화', '수', '목']
leap_year = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] # 윤년
normal_year = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] # 평년
current_year = datetime.date.today().year

# 이번년도가 윤년인지 평년인지 체크
if (current_year % 4 == 0 and current_year % 100 != 0) or current_year % 400 == 0:
    current_year = leap_year
else:
    current_year = normal_year

# 2016년 month월 day일의 요일을 반환하는 함수
def get_day_of_week(month, day):
    all_days = 0
    for i in range(month-1):
        all_days += current_year[i]
    all_days += day-1
    return weekday[all_days % 7] + "요일"