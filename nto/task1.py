import cv2
import os
# import numpy


def convert_to_gray(img):
    imggray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    print(f"gray_image_type: {type(imggray)}")
    return imggray


def find_contours(img):
    ret, binthresh = cv2.threshold(img, 200, 255, 4)
    cv2.imshow('binary_thrashhold', binthresh)  # показываем результат
    contours, hierarchy = cv2.findContours(
        binthresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    return contours


def draw_contours(img, contours):
    cv2.drawContours(img, contours, -1, (0, 255, 0), 2)
    while True:
        cv2.imshow('Original image', img)


def predict(contours, img):
    contours = sorted(contours, key=cv2.contourArea, reverse=True)
    count = 0
    print(f"glares area from image{count}, with {
          img.shape()[:-1]}: {cv2.contourArea(contours[0])}")


def main():
    dir = "/home/vlad/Documents/test-coding/nto/images"
    for path, folders, files in os.walk(dir):
        for file in files:
            img = cv2.imread(file)
            cv2.imshow("image", img)
            gray_image = convert_to_gray(img)
            contours = find_contours(gray_image)
            predict(contours, gray_image)


if __name__ == "__main__":
    main()
