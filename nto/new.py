
import cv2
import numpy as np


def find_line_equations(image_path):
    # Загрузка изображения
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if image is None:
        raise FileNotFoundError(f"Изображение '{image_path}' не найдено.")

    # Бинаризация
    _, binary = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)

    # Поиск контуров
    contours, _ = cv2.findContours(
        binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

    # Находим линии (аппроксимация)
    lines = []
    for contour in contours:
        if len(contour) >= 2:
            # Аппроксимируем контур как прямую
            [vx, vy, x0, y0] = cv2.fitLine(contour, cv2.DIST_L2, 0, 0.01, 0.01)
            slope = vy / vx
            intercept = y0 - slope * x0
            # Уравнение вида y = slope * x + intercept
            lines.append((slope[0], intercept[0]))

    print(lines)

    return lines, binary


def find_intersections(lines, image_shape):
    height, width = image_shape
    intersections = []

    for i in range(len(lines)):
        for j in range(i + 1, len(lines)):
            # Уравнения двух прямых: y = m1 * x + b1, y = m2 * x + b2
            m1, b1 = lines[i]
            m2, b2 = lines[j]

            # Если прямые параллельны, пропускаем
            if abs(m1 - m2) < 1e-6:
                continue

            # Найдём точку пересечения
            x = (b2 - b1) / (m1 - m2)
            y = m1 * x + b1

            # Проверяем, находится ли точка в пределах изображения
            if 0 <= x < width and 0 <= y < height:
                intersections.append((int(round(x)), int(round(y))))

    print(intersections)

    return intersections


def count_white_intersections(intersections, binary):
    count = 0
    for x, y in intersections:
        if binary[y, x] == 255:  # Белый пиксель
            count += 1
    return count


if __name__ == "__main__":
    image_path = "./input.png"
    try:
        # Шаг 1: Найдём уравнения прямых
        lines, binary = find_line_equations(image_path)

        # Шаг 2: Найдём точки пересечения
        intersections = find_intersections(lines, binary.shape)

        # Шаг 3: Подсчитаем только белые пересечения
        result = count_white_intersections(intersections, binary)
        print(result)
    except Exception as e:
        print(f"Ошибка: {e}")
