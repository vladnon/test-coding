import cv2
img = cv2.imread(
    '/home/vlad/Documents/test-coding/nto/images/2Fw7qN-WbX-osG-NIWAMU.jpg')
# cv2.imshow('Original image',img)
imggray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# перевод в оттенки серого
# и ещё алгоримт наложения маски, и плюс 2 алгоритма оптимизации.
ret, binthresh = cv2.threshold(imggray, 200, 255, 4)
cv2.imshow('binary_thrashhold', binthresh)  # показываем результат
contours, hierarchy = cv2.findContours(
    binthresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)  # нахождение контуров
cv2.drawContours(img, contours, -1, (0, 255, 0), 2)
img_with_contours = img.copy()
cv2.drawContours(img_with_contours, contours, -1, (0, 255, 0), 2)
cv2.imshow("image with countours", img_with_contours)


while True:
    cv2.imshow('Original image', img)
