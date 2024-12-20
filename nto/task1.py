import cv2
import os


def convert_to_gray(img):
    imggray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return imggray


def find_contours(img):
    ret, binthresh = cv2.threshold(img, 230, 255, 4)
    # cv2.imshow('binary_thrashhold', binthresh)  # показываем результат
    contours, hierarchy = cv2.findContours(
        binthresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key=cv2.contourArea, reverse=True)
    return contours


def draw_contours(img, contours):
    img = cv2.drawContours(img, contours, -1, (0, 255, 0), 4)
    cv2.imshow("image with contours", img)
    cv2.waitKey()
    return img


def predict(contours, img, count):
    print(f"image: {count}, glares area: {cv2.contourArea(contours[0])}, image size: {
          img.size}: ")


def main():
    dir = "/home/vlad/Documents/test-coding/nto/images"
    count = 1
    for path, folders, files in os.walk(dir):
        for file in files:
            img = cv2.imread(
                f"/home/vlad/Documents/test-coding/nto/images/{file}")
            gray_image = convert_to_gray(img)
            contours = find_contours(gray_image)
            predict(contours, gray_image, count)
            img_with_contours = draw_contours(img, contours)
            # cv2.imwrite(f"image {count} with contours", img_with_contours)
            count += 1


if __name__ == "__main__":
    main()
