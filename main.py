import cv2
import os
from pdf import create_pdf_from_image_folder
from selector import process_image


def run_on_image_paths_for(image_paths, output_image_path):
    count = 0
    fixed_image_paths = []

    for image_file_path in image_paths:
        count += 1
        dst = process_image(image_file_path)
        if dst is not None:
            cv2.imwrite('{}/{}.png'.format(output_image_path, str(count)), dst)
            fixed_image_paths.append(image_file_path)
        else:
            break
    print('FIXED', fixed_image_paths)
    return


def get_image_list(path):
    item_names = os.listdir(path)
    item_names.sort()
    print(path)
    print(item_names)
    image_paths = []
    for i in item_names:
        image_paths.append('{}/{}'.format(path, i))
    return image_paths


def main():
    path = 'C:/Users/Travie/Desktop/tb'
    output_image_path = 'fixed'
    image_paths = get_image_list(path)
    run_on_image_paths_for(image_paths, output_image_path)
    return


if __name__ == "__main__":
    main()
