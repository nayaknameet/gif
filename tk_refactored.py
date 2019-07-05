import tkinter as tk
from tkinter import filedialog, BOTH, messagebox
from PIL import ImageTk, Image

class Application(tk.Frame):
    def __init__(self, master = None):
        super().__init__(master)
        self.master = master
        self.pack(fill=BOTH, expand=True)
        self.createwidgets()
        self.image_list = []

    def createwidgets(self):
        self.select = tk.Button(self, text = "Select", command = self.selectimages)
        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side = 'bottom')
        self.select.pack(side='bottom')

        self.gif = tk.Button(self, text = 'Create Gif', command = self.creategif)
        self.gif.pack(side = 'bottom')

    def selectimages(self):
        # open select image window and store the address to file path as a tuple
        file_path = filedialog.askopenfilenames()
        self.dynamicimages(file_path)

    def dynamicimages(self, args):
        for items in args:
            try:
                im = Image.open(items)
                self.image_list.append(im.copy())
                im.thumbnail((128, 128))
                img = ImageTk.PhotoImage(im)
                self.label = tk.Label(self, image=img)
                self.label.image = img
                self.label.pack()
            except:
                self.displayerror("Please select valid image")


    def creategif(self):
        try:
            self.image_list[0].save('new_image.gif',
                        save_all=True,
                        append_images=self.image_list[0:],
                        duration=100,
                        loop=0)
            self.displayinfo()

        except IndexError:
            self.displayerror("No image selected")

    def displayerror(self, error_msg):
        messagebox.showerror("Error", error_msg)

    def displayinfo(self):
        messagebox.showinfo("Gif", "Gif is create, please check your existing directory")

root = tk.Tk()

root.geometry('400x400')
app = Application(master = root)

app.mainloop()
