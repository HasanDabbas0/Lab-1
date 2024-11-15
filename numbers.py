# Открываем и читаем числа из файла
filename = 'sequence.txt'  # Путь к файлу на один уровень выше
numbers = []

try:
    with open(filename, 'r') as file:
        for line in file:
            try:
                number = float(line.strip())
                # Проверяем, что число в нужном диапазоне
                if (0 <= number <= 5) or (-5 <= number < 0):
                    numbers.append(number)
            except ValueError:
                print(f"Значение '{line.strip()}' не является допустимым числом.")
                
    # Проверяем, есть ли числа для отображения результатов
    if numbers:
        # Классифицируем числа
        positive = [num for num in numbers if num > 0]
        negative = [num for num in numbers if num < 0]
        zero = [num for num in numbers if num == 0]

        # Вычисляем процентные соотношения
        total = len(numbers)
        positive_percentage = (len(positive) / total) * 100
        negative_percentage = (len(negative) / total) * 100
        zero_percentage = (len(zero) / total) * 100

        # Выводим результаты
        print("Процентное соотношение чисел в нужном диапазоне:")
        print(f"Положительные: {positive_percentage:.2f}%")
        print(f"Отрицательные: {negative_percentage:.2f}%")
        print(f"Нулевые: {zero_percentage:.2f}%")
    else:
        print("В файле не найдено допустимых чисел в нужном диапазоне.")

except FileNotFoundError:
    print(f"Файл '{filename}' не найден.")
