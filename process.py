import numpy as np
from PIL import Image

def change_and_save(gscimage, threshold, cond = 0):
    image = np.where(gscimage > threshold, 255, 0).astype(np.uint8)
    image = Image.fromarray(image)
    if cond == 1:
        image.save('output.png')
    image.show()
    
    