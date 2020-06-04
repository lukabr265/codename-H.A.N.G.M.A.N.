from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
class Render_controler():
    def __init__(self):
        self.counter = 0
        self.list_images = []

    def get_path(self,number):
        path = "img/wisielec"+str(number)+".jpg"
        return path

    def load_images(self):
        for i in range(10):
            picture = Image.open(self.get_path(i+1))
            self.list_images.append(picture)

    def show_next(self,paper):
        if self.counter >= 9:
            self.pic = ImageTk.PhotoImage(self.list_images[9].resize((380,420)))
            self.img_id = paper.create_image(600,200,image=self.pic)
            messagebox.showinfo("The end", "You lost :(\nTo play another round press the \'New game\' button")
            self.counter = 9
        else:
            self.pic = ImageTk.PhotoImage(self.list_images[self.counter].resize((380,420)))
            self.img_id = paper.create_image(600,200,image=self.pic)
            self.counter += 1            