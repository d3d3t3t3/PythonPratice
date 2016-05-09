# 출력함수
def print_move(from_tower, to_tower, n):
    print("{from_tower} 에서 {to_tower} 로 {n} 번째 원판을 옮깁니다.".format(
            from_tower = from_tower,
            to_tower = to_tower,
            n = n,
        ))

# form_tower에 있는 height개의 원판을 to_tower로 옮기는 함수
def get_tower_of_hanoi_solution(height, from_tower, to_tower, helper_tower):
    if height == 1:
        print_move(from_tower, to_tower, height) # from_tower에 있는 원판 1개를 to_tower로 옮긴다.
    else:
        get_tower_of_hanoi_solution(height-1, from_tower, helper_tower, to_tower) # from_tower에 있는 height-1 개 원판을 helper_tower로 일단 옮긴다.
        print_move(from_tower, to_tower, height) # form_tower에 있는 height 번째 원판을 to_tower로 옮긴다.
        get_tower_of_hanoi_solution(height-1, helper_tower,to_tower,from_tower) # 아까 helper_tower에 놓았던 height-1 개 원판을 to_tower의 height 번째 원판 위에 옮긴다.

get_tower_of_hanoi_solution(3, "A", "B", "C")