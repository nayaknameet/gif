import tkinter as tk
from tkinter import filedialog, BOTH





class Application(tk.Frame):
    def __init__(self, master = None):
        print(tk.Frame, master)
        super().__init__(master)
        self.master = master
        self.pack(fill=BOTH, expand=True)
        self.create_widgets()

    def create_widgets(self):
        self.select = tk.Button(self, text = "Select", command = self.select_images)
        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side = 'bottom')
        self.select.pack(side='bottom')

    def select_images(self):
        # open select image window and store the address to file path as a tuple
        file_path = filedialog.askopenfilenames()
        self.DynamicImages(file_path)

    def DynamicImages(self, *args):
        pass



root = tk.Tk()

root.geometry('400x400')
app = Application(master = root)



app.mainloop()
