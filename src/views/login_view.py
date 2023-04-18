from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from controllers.gui_controller import GuiController


class LoginView:

    def __init__(self):
        self.gui = GuiController()
        self.ASSETS_PATH = Path(r"assets\login_assets\frame0")
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
            0.0,
            0.0,
            350.0,
            450.0,
            fill="#374194",
            outline="")

        self.canvas.create_text(
            39.0,
            35.0,
            anchor="nw",
            text="Welcome to GBDL",
            fill="#FFFFFF",
            font=("Inter", 32 * -1)
        )

        self.canvas.create_text(
            389.0,
            35.0,
            anchor="nw",
            text="Enter the details.",
            fill="#040000",
            font=("Inter", 32 * -1)
        )

        self.canvas.create_text(
            69.0,
            74.0,
            anchor="nw",
            text="Desktop app for tracking and \nreviewing your favorite games",
            fill="#FFFFFF",
            font=("Inter", 16 * -1)
        )

        self.image_image_1 = PhotoImage(
            file=Path(__file__).parent / self.ASSETS_PATH / (r"image_1.png"))
        self.canvas.create_image(
            174.00000762939453,
            224.0,
            image=self.image_image_1,
        )

        self.entry_image_1 = PhotoImage(
            file=Path(__file__).parent / self.ASSETS_PATH / ("entry_1.png"))
        entry_bg_1 = self.canvas.create_image(
            517.5,
            123.5,
            image=self.entry_image_1
        )
        self.username = Text(
            bd=0,
            bg="#B4B6E7",
            fg="#000716",
            highlightthickness=0
        )
        self.username.place(
            x=392.0,
            y=105.0,
            width=251.0,
            height=35.0
        )

        self.entry_image_2 = PhotoImage(
            file=Path(__file__).parent / self.ASSETS_PATH / ("entry_2.png"))
        entry_bg_2 = self.canvas.create_image(
            517.5,
            191.5,
            image=self.entry_image_2
        )
        self.email = Text(
            bd=0,
            bg="#B4B6E7",
            fg="#000716",
            highlightthickness=0
        )
        self.email.place(
            x=392.0,
            y=173.0,
            width=251.0,
            height=35.0
        )

        self.entry_image_3 = PhotoImage(
            file=Path(__file__).parent / self.ASSETS_PATH / ("entry_3.png"))
        entry_bg_3 = self.canvas.create_image(
            517.5,
            259.5,
            image=self.entry_image_3
        )
        self.password = Text(
            bd=0,
            bg="#B4B6E7",
            fg="#000716",
            highlightthickness=0
        )
        self.password.place(
            x=392.0,
            y=241.0,
            width=251.0,
            height=35.0
        )

        self.canvas.create_text(
            384.0,
            83.0,
            anchor="nw",
            text="Username",
            fill="#000000",
            font=("Inter", 18 * -1)
        )

        self.canvas.create_text(
            384.0,
            151.0,
            anchor="nw",
            text="E-Mail",
            fill="#000000",
            font=("Inter", 18 * -1)
        )

        self.canvas.create_text(
            384.0,
            219.0,
            anchor="nw",
            text="Password",
            fill="#000000",
            font=("Inter", 18 * -1)
        )

        self.button_image_1 = PhotoImage(
            file=Path(__file__).parent / self.ASSETS_PATH /("button_1.png"))
        self.button_1 = Button(
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.gui.open_registration(self),
            relief="flat"
        )
        self.button_1.place(
            x=428.0,
            y=357.0,
            width=180.0,
            height=37.0
        )

        self.button_image_2 = PhotoImage(
            file=Path(__file__).parent / self.ASSETS_PATH / ("button_2.png"))
        self.button_2 = Button(
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.gui.move_to_user_menu(self, self.username.get("1.0", 'end-1c'),
                                                       self.email.get("1.0", 'end-1c'),
                                                       self.password.get("1.0", 'end-1c')),
            relief="flat"
        )
        self.button_2.place(
            x=389.0,
            y=299.0,
            width=262.0,
            height=37.0
        )

    def destroy(self):
        self.window.destroy()
