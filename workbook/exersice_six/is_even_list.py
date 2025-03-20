def is_even_list(list: list[int]) -> int:
    count = 0
    for i in list:
        if i % 2 != 0:
            count += 1
    return count


if __name__ == "__main__":
    print(is_even_list([1, 2, 3, 4, 5, 6]))