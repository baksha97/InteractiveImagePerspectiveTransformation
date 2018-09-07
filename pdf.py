import glob
import os
from fpdf import FPDF #

#('Chapter12/*.png')
def create_pdf_from_image_folder(folder_dir_with_type, out_name):
    imagelist = sorted(glob.glob(folder_dir_with_type))
    imagelist.sort(key=os.path.getmtime)
    print(imagelist)
    pdf = FPDF()
    # imagelist is the list with all image filenames
    for image in imagelist:
        pdf.add_page()
        pdf.image(image,  w=190)
    pdf.output(out_name, "F")
    return True