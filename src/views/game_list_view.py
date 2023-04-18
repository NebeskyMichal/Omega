from tkinter import *
import pyodbc


class GameListView():

    def __init__(self, data):
        window = Tk()
        window.geometry("600x400")
        window.title("Games Table")

        frame = Frame(window)
        frame.pack(fill=BOTH, expand=True)

        self.canvas = Canvas(frame)
        scrollbar = Scrollbar(frame, orient=VERTICAL, command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=scrollbar.set)

        table_frame = Frame(self.canvas)

        title_label = Label(table_frame, text="Title", font=("Arial", 14), padx=10, pady=10)
        title_label.grid(row=0, column=0, sticky=W)

        rating_label = Label(table_frame, text="Global Rating", font=("Arial", 14), padx=10, pady=10)
        rating_label.grid(row=0, column=1, sticky=W)

        for i, row in enumerate(data):
            title = row[0]
            rating = row[1]

            title_label = Label(table_frame, text=title, font=("Arial", 12), padx=10, pady=5)
            title_label.grid(row=i + 1, column=0, sticky=W)

            rating_label = Label(table_frame, text=str(rating), font=("Arial", 12), padx=10, pady=5)
            rating_label.grid(row=i + 1, column=1, sticky=W)

        self.canvas.create_window((0, 0), window=table_frame, anchor='nw')

        self.canvas.pack(side=LEFT, fill=BOTH, expand=True)
        scrollbar.pack(side=RIGHT, fill=Y)

        self.canvas.config(scrollregion=self.canvas.bbox('all'))
        self.canvas.bind('<Configure>', self.update_scroll_region)
        window.mainloop()

    def update_scroll_region(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox('all'))
