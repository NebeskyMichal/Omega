from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


class UserProfileView():

    def __init__(self, gui,  searched_username, rating_count, mean_score, reports_given, username, email, password):
        self.gui = gui

        self.searched_username = searched_username

        self.username = username
        self.email = email
        self.password = password

        self.rating_count = rating_count
        self.mean_score = mean_score
        self.reports_given = reports_given
        self.ASSETS_PATH = Path(r"assets\user_profile\frame0")
        self.window = Tk()
        self.window.geometry("350x450")
        self.window.configure(bg="#FFFFFF")
        self.canvas = Canvas(
            self.window,
            bg = "#FFFFFF",
            height = 450,
            width = 350,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        self.canvas.place(x=0, y=0)
        self.generate_components()
        self.window.resizable(width=False, height=False)
        self.window.mainloop()

    def generate_components(self):
        self.canvas.create_text(
            98.0,
            12.999999999999993,
            anchor="nw",
            text=self.searched_username,
            fill="#000000",
            font=("Inter", 32 * -1)
        )

        self.image_image_1 = PhotoImage(
            file=Path(__file__).parent / self.ASSETS_PATH /("image_1.png"))
        self.image_1 = self.canvas.create_image(
            175.0,
            143.0,
            image=self.image_image_1
        )

        self.canvas.create_text(
            45.0,
            282.0,
            anchor="nw",
            text="User statistics",
            fill="#000000",
            font=("Inter", 24 * -1)
        )

        self.canvas.create_rectangle(
            45.0,
            311.0,
            305.0,
            411.0,
            fill="#374194",
            outline="")

        self.canvas.create_text(
            49.0,
            322.0,
            anchor="nw",
            text="Games reviewed",
            fill="#FFFFFF",
            font=("Inter", 16 * -1)
        )

        self.canvas.create_text(
            49.0,
            352.0,
            anchor="nw",
            text="Mean score",
            fill="#FFFFFF",
            font=("Inter", 16 * -1)
        )

        self.canvas.create_text(
            253.0,
            352.0,
            anchor="nw",
            text=str(round(self.mean_score,2)),
            fill="#FFFFFF",
            font=("Inter", 16 * -1)
        )

        self.canvas.create_text(
            253.0,
            322.0,
            anchor="nw",
            text=self.rating_count,
            fill="#FFFFFF",
            font=("Inter", 16 * -1)
        )

        self.canvas.create_text(
            253.0,
            382.0,
            anchor="nw",
            text=self.reports_given,
            fill="#FFFFFF",
            font=("Inter", 16 * -1)
        )

        self.canvas.create_text(
            50.0,
            382.0,
            anchor="nw",
            text="Reports given",
            fill="#FFFFFF",
            font=("Inter", 16 * -1)
        )

        self.button_image_1 = PhotoImage(
            file=Path(__file__).parent / self.ASSETS_PATH /("button_1.png"))
        self.button_1 = Button(
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.gui.open_user_game_list(self.searched_username),
            relief="flat"
        )
        self.button_1.place(
            x=96.0,
            y=235.0,
            width=159.0,
            height=35.0
        )

        self.button_image_2 = PhotoImage(
            file=Path(__file__).parent / self.ASSETS_PATH /("button_2.png"))
        self.button_2 = Button(
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.gui.move_to_user_menu(self, self.username, self.email, self.password),
            relief="flat"
        )
        self.button_2.place(
            x=10.0,
            y=415.0,
            width=159.0,
            height=28.0
        )

        self.button_image_3 = PhotoImage(
            file=Path(__file__).parent / self.ASSETS_PATH /("button_3.png"))
        self.button_3 = Button(
            image=self.button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print(),
            relief="flat"
        )
        self.button_3.place(
            x=183.0,
            y=415.0,
            width=159.0,
            height=28.0
        )

    def destroy(self):
        self.window.destroy()
