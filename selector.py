import cv2
import numpy as np

from transformer import four_point_transform

current_points = []

def __select_point(event,x,y,flags,param):
    global current_points
    if event == cv2.EVENT_LBUTTONDOWN:
        current_points.append([x, y])

def __choose_points_for_image(image):
    global current_points
    # load the image, clone it, and setup the mouse callback function
    image = cv2.imread(image)
    clone = image.copy()
    cv2.namedWindow("image", cv2.WINDOW_NORMAL)
    imS = cv2.resize(image, (3024, 4032))
    cv2.setMouseCallback("image", __select_point)

    # keep looping until the 'q' key is pressed
    while len(current_points) < 4:
        # display the image and wait for a keypress
        cv2.imshow("image", imS)
        key = cv2.waitKey(1) & 0xFF

        # if the 'r' key is pressed, reset the cropping region
        if key == ord("r"):
            print("r pressed")
            current_points = []

        # if the 'c' key is pressed, break from the loop
        elif key == ord("c"):
            print("c pressed")
            return False
            break


    print(current_points)
    # close all open windows
    cv2.destroyAllWindows()


def process_image(image):
    global current_points
    if __choose_points_for_image(image) is False:
        print('canceled image')
        return None
    img = cv2.imread(image)
    selected_points = np.float32(current_points)
    current_points = []
    dst = four_point_transform(img, selected_points)
    return dst
