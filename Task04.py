## Корреляция

# - Контекст
# Корреляция - статистическая мера, используемая для оценки
# связи между двумя случайными величинами.
# - Ваша задача
# Написать скрипт для расчета корреляции Пирсона между
# двумя случайными величинами (двумя массивами). Можете
# использовать любую парадигму, но рекомендую использовать
# функциональную, т.к. в этом примере она значительно
# упростит вам жизнь.
# - Формула корреляции Пирсона:


import matplotlib.pyplot as plt
import pandas as pd
lst_x = [1, 2, 3, 4, 5, 6]
lst_y = [4, 5, 6, 7, 8, 9]


def pearson_correlation(x, y):
    n = len(x)
    sum_x = sum(x)
    sum_y = sum(y)
    sum_x_sq = sum(xi*xi for xi in x)
    sum_y_sq = sum(yi*yi for yi in y)
    psum = sum(xi*yi for xi, yi in zip(x, y))
    num = psum - (sum_x * sum_y/n)
    den = ((sum_x_sq - pow(sum_x, 2) / n) * (sum_y_sq - pow(sum_y, 2) / n)) ** 0.5
    if den == 0:
        return 0
    return num / den


if __name__ == '__main__':
    lst_x = [1, 2, 32, 4, 5, 6]
    lst_y = [4, 5, 6, 7, 85, 9]
    f = pearson_correlation(lst_x, lst_y)
    print(f)

    # df = pd.DataFrame(lst_x, lst_y)
    # plt.scatter(lst_x, lst_y, f)
    # plt.title(f'Correlation: {f:.2f}')
    # plt.xlabel('x')
    # plt.ylabel('y')
    # plt.show()