import tkinter as tk  # python 3
from tkinter import font  as tkfont  # python 3
from huella_window import TakeHuella
from acerca_autor import AcercaDeAutor
from main_window import MainWindow
from ResultPage import ResultFrame


class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        # 1109 × 701
        container = tk.Frame(self, width=1109, height=701)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        # allowed screens
        for F in (MainWindow, AcercaDeAutor, TakeHuella, ResultFrame):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("MainWindow")
        # self.show_frame("TakeHuella")
        # self.show_frame("ResultFrame")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
