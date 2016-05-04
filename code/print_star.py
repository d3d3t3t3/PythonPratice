def print_star1(count):
    """
    첫번째 별찍기 함수
    """
    for i in range(count):
        print("*" * (i+1))

def print_star2(count):
    """
    두번째 별찍기 함수
    """
    for i in range(count):
        print(" " * (count - i - 1) + "*" * (i + 1))

def print_star3(count):
    """
    세번째 별찍기 함수
    """
    for i in range(count):
        print("*" * (count-i))

def print_star4(count):
    """
    네번째 별찍기 함수
    """
    for i in range(count):
        print("" * i + "*" * (count - i))

print_star1(int(input("크기를 입력하세요 : ")))
print_star2(int(input("크기를 입력하세요 : ")))
print_star3(int(input("크기를 입력하세요 : ")))
print_star4(int(input("크기를 입력하세요 : ")))

# input.txt파일의 입력을 받아 print_star3 함수 실행
with open("./input.txt","r") as f:
    input_array = f.readlines()
for i in range(len(input_array)):
    print("<input이 {test_number}일 경우>".format(test_number=int(input_array[i])))
    print_star3(int(input_array[i]))
    print('\n')