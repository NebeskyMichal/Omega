from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


class RegistrationView:
    def __init__(self, gui_controller):
        self.ASSETS_PATH = Path(r"assets\registration_assets\frame0")
        self.window = Tk()
        self.window.geometry("350x450")
        self.window.configure(bg="#384195")
        self.gui = gui_controller
        self.canvas = Canvas(
            self.window,
            bg="#384195",
            height=450,
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
            174.5,
            104.5,
            image=self.entry_image_1
        )
        self.username = Text(
            bd=0,
            bg="#B4B6E7",
            fg="#000716",
            highlightthickness=0
        )
        self.username.place(
            x=49.0,
            y=86.0,
            width=251.0,
            height=35.0
        )

        self.entry_image_2 = PhotoImage(
            file=Path(__file__).parent / self.ASSETS_PATH / ("entry_2.png"))
        self.entry_bg_2 = self.canvas.create_image(
            174.5,
            172.5,
            image=self.entry_image_2
        )
        self.email = Text(
            bd=0,
            bg="#B4B6E7",
            fg="#000716",
            highlightthickness=0
        )
        self.email.place(
            x=49.0,
            y=154.0,
            width=251.0,
            height=35.0
        )

        self.entry_image_3 = PhotoImage(
            file=Path(__file__).parent / self.ASSETS_PATH / ("entry_3.png"))
        self.entry_bg_3 = self.canvas.create_image(
            174.5,
            240.5,
            image=self.entry_image_3
        )
        self.password = Text(
            bd=0,
            bg="#B4B6E7",
            fg="#000716",
            highlightthickness=0
        )
        self.password.place(
            x=49.0,
            y=222.0,
            width=251.0,
            height=35.0
        )

        self.canvas.create_text(
            41.0,
            64.0,
            anchor="nw",
            text="Username",
            fill="#FFFFFF",
            font=("Inter", 18 * -1)
        )

        self.canvas.create_text(
            41.0,
            132.0,
            anchor="nw",
            text="E-Mail",
            fill="#FFFFFF",
            font=("Inter", 18 * -1)
        )

        self.canvas.create_text(
            41.0,
            200.0,
            anchor="nw",
            text="Password",
            fill="#FFFDFD",
            font=("Inter", 18 * -1)
        )

        self.entry_image_4 = PhotoImage(
            file=Path(__file__).parent / self.ASSETS_PATH / ("entry_4.png"))
        self.entry_bg_4 = self.canvas.create_image(
            174.5,
            308.5,
            image=self.entry_image_4
        )
        self.password_check = Text(
            bd=0,
            bg="#B4B6E7",
            fg="#000716",
            highlightthickness=0
        )
        self.password_check.place(
            x=49.0,
            y=290.0,
            width=251.0,
            height=35.0
        )

        self.canvas.create_text(
            41.0,
            268.0,
            anchor="nw",
            text="Repeat password",
            fill="#FFFFFF",
            font=("Inter", 18 * -1)
        )

        self.canvas.create_text(
            84.0,
            13.0,
            anchor="nw",
            text="Registration",
            fill="#FFFFFF",
            font=("Inter", 32 * -1)
        )

        self.button_image_1 = PhotoImage(
            file=Path(__file__).parent / self.ASSETS_PATH / ("button_1.png"))
        self.button_1 = Button(
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.gui.register_user(self,
                                                   self.username.get("1.0", 'end-1c'),
                                                   self.email.get("1.0", 'end-1c'),
                                                   self.password.get("1.0", 'end-1c'),
                                                   self.password_check.get("1.0", 'end-1c')),
            relief="flat"
        )
        self.button_1.place(
            x=60.0,
            y=358.0,
            width=230.0,
            height=35.0
        )

        self.button_image_2 = PhotoImage(
            file=Path(__file__).parent / self.ASSETS_PATH / ("button_2.png"))
        self.button_2 = Button(
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.gui.return_to_login(self),
            relief="flat"
        )
        self.button_2.place(
            x=115.0,
            y=402.0,
            width=129.0,
            height=35.0
        )

    def destroy(self):
        self.window.destroy()
