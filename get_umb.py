import numpy as np
import matplotlib.pyplot as plt
from process import *

def show(hst, new):
    plt.bar(np.arange(256), hst, color='gray')
    plt.axvline(new, color='red', linestyle='--', linewidth=2, label=f'Umbral previo: {new:.2f}')
    plt.show()


def divide(gscimage, histogram, delta, limit = 50):
    threshold = np.mean(gscimage)
    count = 0
    while True:
        front = np.where(gscimage > threshold, gscimage, 0)
        back = np.where(gscimage <= threshold, gscimage, 0)
        meanF = np.mean(front[front>0])
        meanB = np.mean(back[back>0])
        newThreshold = (meanF + meanB) / 2

        change_and_save(gscimage, newThreshold)
        show(histogram, newThreshold)
        if abs(newThreshold - threshold) < delta or count >= limit:
            return newThreshold
        threshold = newThreshold
        count += 1
    