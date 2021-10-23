import sys
import math


def get_coef(index, prompt):
    '''
    Читаем коэффициент из командной строки или вводим с клавиатуры
    Args:
        index (int): Номер параметра в командной строке
        prompt (str): Приглашение для ввода коэффицента
    Returns:
        float: Коэффициент квадратного уравнения

    '''

    try:
        # Пробуем прочитать коэффициент из командной строки
        coef_str = sys.argv[index]
        if index == 1:
            1 / float(sys.argv[1])

    except ZeroDivisionError:
        print('Коэффициент А не должен быть равен нулю, иначе это будет не биквадратное уравнение')
        print(prompt)
        coef_str = input()
        #coef = float(coef_str)

        # Пытаемся перевести строку в действительное число
    try:
        coef = float(coef_str)

    except (ValueError, TypeError):
        print('Введены некорректные данные!')
        print(prompt)
        coef_str = input()
        coef = float(coef_str)

    # coef = float(coef_str)
    return coef


def get_roots(a, b, c):
    '''
    Вычисление корней биквадратного уравнения
    Args:
        a (float): коэффициент А
        b (float): коэффициент B
        c (float): коэффициент C
    Returns:
        list[float]: Список корней
    '''
    result = []
    D = b * b - 4 * a * c

    if D == 0.0:
        root1 = math.sqrt(-b / (2.0 * a))
        if root1 == 0:
            result.append(abs(root1))
        else:
            root2 = -root1
            result.append(root1)
            result.append(root1)
    elif D > 0.0:
        sqD = math.sqrt(D)
        if ((-b + sqD) / (2.0 * a)) >= 0:
            root3 = round(math.sqrt((-b + sqD) / (2.0 * a)), 2)
            if root3 == 0:
                result.append(abs(root3))
            else:
                root4 = -root3
                result.append(root3)
                result.append(root4)
        if ((-b - sqD) / (2.0 * a)) >= 0:
            root5 = round(math.sqrt((-b - sqD) / (2.0 * a)), 2)
            if root5 == 0:
                result.append(abs(root5))
            else:
                root6 = -root5
                result.append(root5)
                result.append(root6)

    return result


def main():
    '''
    Основная функция
    '''

    a = get_coef(1, 'Введите коэффициент А:')
    b = get_coef(2, 'Введите коэффициент B:')
    c = get_coef(3, 'Введите коэффициент C:')

    # Вычисление корней
    roots = get_roots(a, b, c)

    # Вывод корней
    len_roots = len(roots)

    if len_roots == 0:
        print('Нет корней')
    elif len_roots == 1:
        print('Один корень: {}'.format(roots[0]))
    elif len_roots == 2:
        print('Два корня: {}, {}'.format(roots[0], roots[1]))
    elif len_roots == 3:
        print('Три корня: {}, {}, {}'.format(roots[0], roots[1], roots[2]))
    elif len_roots == 4:
        print('Четыре корня: {}, {}, {}, {}'.format(roots[0], roots[1], roots[2], roots[3]))


# Если сценарий запущен из командной строки
if __name__ == "__main__":
    main()

# Пример запуска
# python3 main.py 1 0 -4
