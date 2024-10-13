# -*- coding: utf-8 -*-
"""
Файл служит для определения точности вашего алгоритма

Для получения оценки точности, запустите файл на исполнение
"""

import cv2
import pandas as pd

import eval as submission


def main():
    csv_file = "annotations.csv"
    data = pd.read_csv(csv_file, sep=';')
    data = data.sample(frac=1)

    correct = 0
    for row in data.itertuples():
        _, image_filename, answer = row

        image = cv2.imread(image_filename)

        user_answer = submission.predict_illumination(image)
        if user_answer == answer:
            correct += 1

    total_object = len(data.index)
    print(f"Из {total_object} предсказаний верны {correct}")

    score = correct / total_object
    print(f"Точность: {score:.2f}")


if __name__ == '__main__':
    main()