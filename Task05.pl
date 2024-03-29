# - Контекст
# Мы уже видели множество решений этой задачи в различных
# стилях. Пришло время решить её с помощью логической
# парадигмы.
# - Ваша задача
# Написать программу на языке Prolog для вычисления суммы
# элементов списка. На вход подаётся целочисленный массив.
# На выходе - сумма элементов массива.

sum_list([], 0).
sum_list([Head|Tail], Sum) :-
    sum_list(Tail, TailSum),
    Sum is Head + TailSum.

?- sum_list([1, 2, 3, 4, 5], X).
X = 15.