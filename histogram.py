import cv2

import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("shrek.png")

img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow("Original", img)
cv2.waitKey(-1)

arr = np.array(img)


def histogram(array):
    intensities = np.zeros(shape=(256,))

    for i in range(array.shape[0]):
        for j in range(array.shape[1]):
            intensities[array[i][j]] += 1

    return intensities


def h_histogram(array, lim):
    intensities = np.zeros(shape=(256,))

    for i in range(array.shape[0]):
        for j in range(array.shape[1]):
            if array[i][j] < lim:
                intensities[array[i][j]] += 1

    return intensities

def normalized_histogram(array):
    intensities = np.zeros(shape=(256,))
    size = array.size

    for i in range(array.shape[0]):
        for j in range(array.shape[1]):
            intensities[array[i][j]] += 1

    intensities = [i / size for i in intensities]

    return intensities


hist = histogram(arr)
hist2 = h_histogram(arr, 200)
hist3 = normalized_histogram(arr)
# plt.bar(range(256), hist2, color=[(v / 255, v / 255, v / 255) for v in range(256)], width=1.0)
# plt.bar(range(256), hist, color=[(v / 255, v / 255, v / 255) for v in range(256)], width=1.0)
plt.bar(range(256), hist3, color=[(v / 255, v / 255, v / 255) for v in range(256)], width=1.0)
plt.title("Intensity Histogram with Color")
plt.xlabel("Intensity Value (0-255)")
plt.ylabel("Pixel Count")
plt.show()