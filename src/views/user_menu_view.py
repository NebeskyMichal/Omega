from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


class UserMenuView:

    def __init__(self, gui,  username, email, password, rating_count, mean_score, reports_given):
        self.gui = gui

        self.username = username
        self.email = email
        self.password = password
        self.rating_count = rating_count
        self.mean_score = mean_score
        self.reports_given = reports_given

        if self.mean_score is None:
            self.mean_score = 0
        if self.rating_count is None:
            self.rating_count = 0
        if self.reports_given is None:
            self.report_given = 0

        self.ASSETS_PATH = Path(r"assets\user_menu_assets\frame0")
        self.window = Tk()
        self.window.geometry("700x450")
        self.window.configure(bg="#FFFFFF")
        self.canvas = Canvas(
            self.window,
            bg="#FFFFFF",
            height=450,
            width=700,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )

        self.canvas.place(x=0, y=0)
        self.generate_components()
        self.window.resizable(width=False, height=False)
        self.window.mainloop()

    def generate_components(self):
        self.canvas.create_rectangle(
            350.0,
            0.0,
            700.0,
            450.0,
            fill="#374194",
            outline="")

        self.button_image_1 = PhotoImage(
            file=Path(__file__).parent / self.ASSETS_PATH /("button_1.png"))
        self.button_1 = Button(
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.gui.open_game_review_form(self, self.username, self.email, self.password),
            relief="flat"
        )
        self.button_1.place(
            x=413.0,
            y=82.0,
            width=230.0,
            height=35.0
        )

        self.button_image_2 = PhotoImage(
            file=Path(__file__).parent / self.ASSETS_PATH /("button_2.png"))
        self.button_2 = Button(
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.gui.open_search_window(self, self.username, self.email, self.password, "user"),
            relief="flat"
        )
        self.button_2.place(
            x=413.0,
            y=149.0,
            width=230.0,
            height=35.0
        )
        #Availabile games
        self.button_image_3 = PhotoImage(
            file=Path(__file__).parent / self.ASSETS_PATH /("button_3.png"))
        self.button_3 = Button(
            image=self.button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.gui.open_game_list(),
            relief="flat"
        )
        self.button_3.place(
            x=413.0,
            y=214.0,
            width=230.0,
            height=35.0
        )

        self.button_image_4 = PhotoImage(
            file=Path(__file__).parent / self.ASSETS_PATH /("button_4.png"))
        self.button_4 = Button(
            image=self.button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.gui.move_to_password_change(self, self.username, self.email, self.password),
            relief="flat"
        )
        self.button_4.place(
            x=413.0,
            y=284.0,
            width=230.0,
            height=35.0
        )

        self.button_image_5 = PhotoImage(
            file=Path(__file__).parent / self.ASSETS_PATH /("button_5.png"))
        self.button_5 = Button(
            image=self.button_image_5,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.gui.return_to_login(self),
            relief="flat"
        )
        self.button_5.place(
            x=410.0,
            y=352.0,
            width=230.0,
            height=35.0
        )

        self.button_image_6 = PhotoImage(
            file=Path(__file__).parent / self.ASSETS_PATH / ("button_6.png"))
        self.button_6 = Button(
            image=self.button_image_6,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.gui.open_user_game_list(self.username),
            relief="flat"
        )
        self.button_6.place(
            x=96.0,
            y=235.0,
            width=159.0,
            height=35.0
        )

        self.canvas.create_text(
            98.0,
            13.0,
            anchor="nw",
            text=self.username,
            fill="#000000",
            font=("Inter", 32 * -1)
        )

        self.canvas.create_text(
            485.0,
            13.0,
            anchor="nw",
            text="Menu",
            fill="#FFFFFF",
            font=("Inter", 32 * -1)
        )

        self.image_image_1 = PhotoImage(
            file=Path(__file__).parent / self.ASSETS_PATH /("image_1.png"))
        self.image_1 = self.canvas.create_image(
            175.0,
            153.0,
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

    def destroy(self):
        self.window.destroy()
