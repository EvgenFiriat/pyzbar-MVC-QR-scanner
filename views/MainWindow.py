from tkinter import *
import os

from PIL import Image, ImageTk


class MainWindow(Frame):
    def __init__(self, root):
        super().__init__(root)
        self.pack()
        self.root = root
        self.create_widgets()

    def create_widgets(self):
        self.image_uploaded = Image.open(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),  'src/default.png')).convert('RGB')
        self.img = ImageTk.PhotoImage(image = self.image_uploaded)
        self.image_label = Label(self, image = self.img)
        self.image_decompressed = Label(self, image = self.img)
        self.decompress_button = Button(self, text = 'Decompress', width =15, height = 2, bg = '#fff', font = 'ff-kava 10')
        self.openfile_button = Button(self, text = 'Open file', width = 15, height =2, bg = '#fff', font = 'ff-kava 10')
        self.image_label.grid(row = 0, column = 0, sticky = 'w')
        self.image_decompressed.grid(row = 0, column = 1, sticky = 'e')
        self.decompress_button.grid(row = 1, column = 0, sticky = 'we')
        self.openfile_button.grid(row=1, column=1, sticky='we')



if __name__ == '__main__':
     root = Tk()
     root.geometry("800x500+300+100")
     #root.resizable(False, False)
     root.title("JPEG - decompressor")
     app = MainWindow(root)
     root.mainloop()