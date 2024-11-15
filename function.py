# Диапазон значений x и y
max_y = 10
max_x = 10

# Построение сетки
for y in range(max_y, -1, -1):
    line = ""
    for x in range(max_x + 1):
        # Если точка соответствует уравнению y = x + 1
        if y == x + 1:
            line += "* "
        # Рисуем оси
        elif y == 0 and x > 0:
            line += "- "
        elif x == 0 and y > 0:
            line += "| "
        # Пустые ячейки
        else:
            line += "  "
    print(line)
