from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
class Render_controler():
    def __init__(self):
        self.counter = 0 
        self.window = Tk()
        self.list_images = []
        self.paper = Canvas()

    def get_path(self,number): 
        path = "img/wisielec"+str(number)+".jpg"
        return path

    def load_images(self):
        for i in range(10):
            picture = Image.open(self.get_path(i+1))
            self.list_images.append(picture)

    def show_hangman(self):
        self.window.title("hangman")
        self.window.geometry("400x400")
        self.paper = Canvas(self.window,width=400,height=400)
        self.paper.pack()

    def show_next(self):
        self.pic = ImageTk.PhotoImage(self.list_images[self.counter])
        self.img_id = self.paper.create_image(200,200,image=self.pic)
        self.counter = self.counter + 1
        if self.counter == 10:
            messagebox.showinfo("The end", "You lost")
