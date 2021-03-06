import cv2
import os
from tkinter import Tk, TOP, BOTH, X, LEFT, Button, Listbox, END, BOTTOM
from tkinter.ttk import Frame, Label, Entry
from selector import process_image
from pdf import create_pdf_from_image_folder


class PerspectiveTransformerGUI(Frame):

    def __init__(self):
        super().__init__()
        self.master.title("Perspective Transformer")
        self.pack(fill=BOTH, expand=True)

        frame1 = Frame(self)
        frame1.pack(fill=X)

        lbl1 = Label(frame1, text="INPUT", width=15)
        lbl1.pack(side=LEFT, padx=5, pady=5)

        self.input_entry = Entry(frame1)
        self.input_entry.pack(fill=X, padx=5, expand=True)

        frame2 = Frame(self)
        frame2.pack(fill=X)

        lbl2 = Label(frame2, text="OUTPUT", width=15)
        lbl2.pack(side=LEFT, padx=5, pady=5)

        self.output_entry = Entry(frame2)
        self.output_entry.pack(fill=X, padx=5, expand=True)

        start_button = Button(self, text="START", width=25, padx=5, pady=5, command= self.run_on_image_paths)
        start_button.pack(side=TOP)

        pdf_button = Button(self, text="MAKE A PDF FROM FIXED", width=25, padx=5, pady=5, command=self.create_pdf)
        pdf_button.pack(side=BOTTOM)

        frame3 = Frame(self)
        frame3.pack(fill=BOTH, expand=True)

        lb3 = Label(frame3, text="[C Key => Finish early] \n FIXED ITEMS/Dialog", width=50)
        lb3.pack(side=TOP, padx=5, pady=5)

        self.listbox = Listbox(frame3)
        self.listbox.pack(fill=BOTH)

    def create_pdf(self):
        # ('Chapter12/*.png')
        output_path = self.output_entry.get()
        completed = create_pdf_from_image_folder('{}/*.png'.format(output_path), 'output.pdf')
        completed_string = 'COMPLETED: {}'.format(completed)
        print(completed_string)
        self.listbox.insert(END, completed_string)
        return

    def get_image_list(self):
        path = self.input_entry.get()
        item_names = os.listdir(path)
        item_names.sort()
        print(path)
        print(item_names)
        image_paths = []
        for i in item_names:
            image_paths.append('{}/{}'.format(path, i))
        return image_paths

    def run_on_image_paths(self):
        count = 0
        fixed_image_paths = []

        for image_file_path in self.get_image_list():
            count += 1
            dst = process_image(image_file_path)
            if dst is not None:
                cv2.imwrite('{}/{}.png'.format(self.output_entry.get(), str(count)), dst)
                fixed_image_paths.append(image_file_path)
            else:
                break
        self.listbox.insert(END, *fixed_image_paths)
        return


def main():
    root = Tk()
    root.geometry("300x300+600+300")
    app = PerspectiveTransformerGUI()
    root.mainloop()


if __name__ == '__main__':
    main()
