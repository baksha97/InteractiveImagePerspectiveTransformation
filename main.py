import cv2
import os
from pdf import create_pdf_from_image_folder
from selector import process_image

count = -1


def run_on_image_paths_for(image_paths):
    global count, current_points
    for image_file_path in image_paths:
        count += 1
        dst = process_image(image_file_path)
        current_points = []
        cv2.imwrite('fixed/{}.png'.format(str(count)), dst)
    return


def main():
    path = 'C:/Users/Travie/Desktop/tb/'
    item_names = os.listdir(path)
    item_names.sort()
    print(path)
    print(item_names)
    image_paths = []
    for i in item_names:
        image_paths.append('{}{}'.format(path, i))
    run_on_image_paths_for(image_paths)
    return

if __name__ == "__main__":
    main()

