from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


class GameReviewView:

    def __init__(self, gui, username, email, password):
        self.gui = gui

        self.username = username
        self.email = email
        self.password = password

        self.ASSETS_PATH = Path(r"assets\game_review\frame0")
        self.window = Tk()
        self.window.geometry("350x225")
        self.window.configure(bg="#FFFFFF")
        self.canvas = Canvas(
            self.window,
            bg="#FFFFFF",
            height=225,
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
        self.entry_bg_1 = self.canvas.create_image(
            237.5,
            76.0,
            image=self.entry_image_1
        )
        self.game_to_review = Text(
            bd=0,
            bg="#B4B6E7",
            fg="#000716",
            highlightthickness=0
        )
        self.game_to_review.place(
            x=171.0,
            y=64.0,
            width=133.0,
            height=22.0
        )

        self.entry_image_2 = PhotoImage(
            file=Path(__file__).parent / self.ASSETS_PATH / ("entry_2.png"))
        self.entry_bg_2 = self.canvas.create_image(
            174.5,
            146.0,
            image=self.entry_image_2
        )
        self.rating = Text(
            bd=0,
            bg="#B4B6E7",
            fg="#000716",
            highlightthickness=0
        )
        self.rating.place(
            x=45.0,
            y=110.0,
            width=259.0,
            height=70.0
        )

        self.canvas.create_text(
            37.0,
            66.0,
            anchor="nw",
            text="Rating (1-10)",
            fill="#000000",
            font=("Inter", 16 * -1)
        )

        self.entry_image_3 = PhotoImage(
            file=Path(__file__).parent / self.ASSETS_PATH / ("entry_3.png"))
        self.entry_bg_3 = self.canvas.create_image(
            237.5,
            30.0,
            image=self.entry_image_3
        )
        self.review = Text(
            bd=0,
            bg="#B4B6E7",
            fg="#000716",
            highlightthickness=0
        )
        self.review.place(
            x=171.0,
            y=18.0,
            width=133.0,
            height=22.0
        )

        self.canvas.create_text(
            37.0,
            20.0,
            anchor="nw",
            text="Game to review",
            fill="#000000",
            font=("Inter", 16 * -1)
        )

        self.canvas.create_text(
            37.0,
            88.0,
            anchor="nw",
            text="Review",
            fill="#000000",
            font=("Inter", 16 * -1)
        )

        self.button_image_1 = PhotoImage(
            file=Path(__file__).parent / self.ASSETS_PATH / ("button_1.png"))
        self.button_1 = Button(
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.gui.send_review(self.username, self.email,
                                                 self.review.get("1.0", 'end-1c'),
                                                 self.game_to_review.get("1.0", 'end-1c')
                                                 , self.rating.get("1.0", 'end-1c')
                                                 ),
            relief="flat"
        )
        self.button_1.place(
            x=202.0,
            y=187.0,
            width=110.0,
            height=21.0
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
            x=37.0,
            y=187.0,
            width=110.0,
            height=21.0
        )

    def destroy(self):
        self.window.destroy()
