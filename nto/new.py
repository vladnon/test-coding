
import cv2
import numpy as np


def read_file(filepath):
    """Считывает черно-белое изображение."""
    img = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)
    if img is None:
        raise FileNotFoundError(f"Файл '{filepath}' не найден.")
    return img


def get_pixels_in_contour(img):
    """Находит все пиксели внутри каждой области, ограниченной контуром."""
    # Бинаризация изображения
    _, binary = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

    # Поиск контуров
    contours, _ = cv2.findContours(
        binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Список для хранения пикселей каждой фигуры
    all_pixels = []

    # Создаём пустую маску
    mask = np.zeros_like(binary)

    for contour in contours:
        # Очищаем маску для текущего контура
        mask[:] = 0

        # Рисуем контур на маске
        cv2.drawContours(mask, [contour], -1, color=(255, 255, 0),
                         thickness=-1)  # Закрашиваем область

        cv2.imshow("something", mask)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        # Получаем координаты всех пикселей внутри контура
        pixels = np.column_stack(np.where(mask == 255))  # Формат (y, x)
        all_pixels.append(pixels)

    return all_pixels


def main(filepath):
    """Главная функция."""
    image = read_file(filepath)
    all_pixels = get_pixels_in_contour(image)

    # Вывод информации о пикселях
    for i, pixels in enumerate(all_pixels):
        print(f"Контур {i + 1}: {len(pixels)} пикселей")
        print(pixels[:10])  # Вывод первых 10 пикселей


if __name__ == "__main__":
    main("input.png")
