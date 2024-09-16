from pre import *
from get_umb import *
from process import *

def main():
    #To change image path, refer to pre.py file
    image_array = load_image_and_convert_grayscale()
    histogram = create_histogram(image_array)
    umbral = divide(image_array, histogram, 1)
    change_and_save(image_array, umbral, 1)



if __name__ == "__main__":
    main()