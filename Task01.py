

# Задача №1
# Дан список целых чисел numbers. 
# Необходимо написать в императивном 
# стиле процедуру для сортировки числа в списке в порядке убывания. 
# Можно использовать любой алгоритм сортировки.

# Задача №2
# Написать точно такую же процедуру, но в декларативном стиле



def sort_list_imperativ(number: list) -> list:
    for i in range(len(number) - 1):
        for j in range(len(number) - 1 - i):
            if number[j] < number[j + 1]:
                number[j], number[j + 1] = number[j + 1], number[j]
    return number


def sort_list_declarativ(number: list) -> list:
    number = sorted(number, reverse=True)
    return number


if __name__ == "__main__":
    arr = [1, 7, 8, 67, 43]
    print(sort_list_imperativ(arr))
    print(sort_list_declarativ(arr))
