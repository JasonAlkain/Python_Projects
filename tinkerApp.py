import tkinter as tk


class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()


# create the application
_app = App()

#
# here are method calls to the window manager class
#

appSize = width, height = int(1920/2), int(1080/2)

_app.master.title("My Do-Nothing Application")
_app.master.minsize(width, height)
_app.master.maxsize(width, height)

# start the program
_app.mainloop()
