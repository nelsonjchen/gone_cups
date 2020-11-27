import timeit

import cv2
from pyzbar.pyzbar import decode

camera = cv2.VideoCapture(0, cv2.CAP_DSHOW)
camera.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)

def show_points_on_img(img, points):
    img_show = img.copy()
    for point_pair_1, point_pair_2 in list(zip(points, points[1:])) + [(points[-1],points[0])]:
        point_pair_1 = (int(point_pair_1[0]), int(point_pair_1[1]))
        point_pair_2 = (int(point_pair_2[0]), int(point_pair_2[1]))
        cv2.line(img_show, point_pair_1, point_pair_2,  (255, 0, 0), 3)
    return img_show

while True:
    return_value, image = camera.read()
    start_time = timeit.default_timer()
    barcodes = decode(image)
    for barcode in barcodes:

        image = show_points_on_img(image, barcode.polygon)
    cv2.imshow('image', image)
    cv2.waitKey(1)

    if barcodes:
        print(barcodes)
