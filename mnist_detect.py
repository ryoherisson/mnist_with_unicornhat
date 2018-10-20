import time
import picamera
import numpy as np
import cv2
from twolayernet import TwoLayerNet
from PIL import Image


def mnist_detect():
    with picamera.PiCamera() as camera:
        camera.hflip = True
        camera.vflip = True
        camera.resolution = (750,750)
        camera.start_preview()
        time.sleep(5)
        camera.capture('picture.jpg', resize=(28,28))

    img_gray = cv2.imread('picture.jpg', cv2.IMREAD_GRAYSCALE)

    thresh = 100
    max_pixel = 255
    ret, img_dst = cv2.threshold(img_gray,
                                thresh,
                                max_pixel,
                                cv2.THRESH_BINARY)

    img_dst = img_dst / 255
    img_dst = img_dst.reshape(1, img_dst.size)

    print(img_dst[0])
    network = TwoLayerNet(input_size=784, hidden_size=50, output_size=10)
    network.load_params(file_name="params.pkl")
    y = network.predict(img_dst[0])
    y = np.argmax(y)
    print(y)

    return y

mnist_detect()
