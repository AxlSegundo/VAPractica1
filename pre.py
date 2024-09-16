import cv2
import numpy as np
import matplotlib.pyplot as plt

#Input image path here
image_paths = 'img/cancer.jpg'

def load_image_and_convert_grayscale():
    img = cv2.imread(image_paths)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    image_array = np.array(gray)

    return image_array

def create_histogram(image_array: np.array) -> np.array:
    h, w = image_array.shape
    histogram = np.zeros(256)

    for pixel in image_array.flatten():
        histogram[pixel] += 1

    return histogram


if __name__ == "__main__":
    image_array = load_image_and_convert_grayscale()
    histogram = create_histogram(image_array)
    #plot_histogram(histogram)