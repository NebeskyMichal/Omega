from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


class SearchView:

    def __init__(self, gui, username, email, password, option):
        self.gui = gui
        self.option = option
        self.username = username
        self.email = email
        self.password = password

        self.ASSETS_PATH = Path(r"assets\search\frame0")
        self.window = Tk()
        self.window.geometry("350x100")
        self.window.configure(bg="#FFFFFF")
        self.canvas = Canvas(
            self.window,
            bg="#FFFFFF",
            height=100,
            width=350,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )

        self.canvas.place(x=0, y=0)
        self.generate_components()
        self.window.resizable(width=False, height=False)
        self.window.mainloop()

    def generate_components(self):
        self.entry_image_1 = PhotoImage(
            file=Path(__file__).parent / self.ASSETS_PATH / ("entry_1.png"))
        entry_bg_1 = self.canvas.create_image(
            174.5,
            23.5,
            image=self.entry_image_1
        )
        self.searched_term = Text(
            bd=0,
            bg="#B4B6E7",
            fg="#000716",
            highlightthickness=0
        )
        self.searched_term.place(
            x=49.0,
            y=5.0,
            width=251.0,
            height=35.0
        )

        self.button_image_1 = PhotoImage(
            file=Path(__file__).parent / self.ASSETS_PATH / ("button_1.png"))
        self.button_1 = Button(
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.gui.open_user_profile(self, self.searched_term.get("1.0", 'end-1c'),
                                                       self.username, self.email, self.password),
            relief="flat"
        )
        self.button_1.place(
            x=182.0,
            y=50.0,
            width=126.0,
            height=35.0
        )

        self.button_image_2 = PhotoImage(
            file=Path(__file__).parent / self.ASSETS_PATH / ("button_2.png"))

        self.button_2 = Button(
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.gui.move_to_user_menu(self, self.username, self.email, self.password),
            relief="flat"
        )

        self.button_2.place(
            x=41.0,
            y=50.0,
            width=126.0,
            height=35.0
        )

    def destroy(self):
        self.window.destroy()
