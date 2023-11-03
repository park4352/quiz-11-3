tree_height = int(input("크리스마스트리의 높이를 설정하세요: "))

def print_christmas_tree(height):
    for i in range(height):
        # 공백 출력
        for j in range(height - i - 1):
            print(" ", end="")

        # 별 출력
        for j in range(2 * i + 1):
            print("*", end="")

        # 줄 바꿈
        print()

print_christmas_tree(tree_height)
