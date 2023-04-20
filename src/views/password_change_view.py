from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


class PasswordChangeView:

    def __init__(self, gui, username, email, password):
        self.username = username
        self.password = password
        self.email = email
        self.gui = gui
        self.ASSETS_PATH = Path(r"assets\password_change\frame0")
        self.window = Tk()
        self.window.geometry("350x450")
        self.window.configure(bg="#384195")
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
        entry_bg_1 = self.canvas.create_image(
            174.5,
            116.5,
            image=self.entry_image_1
        )
        self.current_password = Text(
            bd=0,
            bg="#B4B6E7",
            fg="#000716",
            highlightthickness=0
        )
        self.current_password.place(
            x=49.0,
            y=98.0,
            width=251.0,
            height=35.0
        )

        self.entry_image_2 = PhotoImage(
            file=Path(__file__).parent / self.ASSETS_PATH / ("entry_2.png"))
        entry_bg_2 = self.canvas.create_image(
            174.5,
            184.5,
            image=self.entry_image_2
        )
        self.pass1 = Text(
            bd=0,
            bg="#B4B6E7",
            fg="#000716",
            highlightthickness=0
        )
        self.pass1.place(
            x=49.0,
            y=166.0,
            width=251.0,
            height=35.0
        )

        self.entry_image_3 = PhotoImage(
            file=Path(__file__).parent / self.ASSETS_PATH / ("entry_3.png"))
        self.entry_bg_3 = self.canvas.create_image(
            174.5,
            252.5,
            image=self.entry_image_3
        )
        self.pass2 = Text(
            bd=0,
            bg="#B4B6E7",
            fg="#000716",
            highlightthickness=0
        )
        self.pass2.place(
            x=49.0,
            y=234.0,
            width=251.0,
            height=35.0
        )

        self.canvas.create_text(
            41.0,
            76.0,
            anchor="nw",
            text="Old password",
            fill="#FFFFFF",
            font=("Inter", 18 * -1)
        )

        self.canvas.create_text(
            41.0,
            144.0,
            anchor="nw",
            text="New password",
            fill="#FFFFFF",
            font=("Inter", 18 * -1)
        )

        self.canvas.create_text(
            41.0,
            212.0,
            anchor="nw",
            text="New password again",
            fill="#FFFDFD",
            font=("Inter", 18 * -1)
        )

        self.canvas.create_text(
            41.0,
            17.0,
            anchor="nw",
            text="Password change",
            fill="#FFFFFF",
            font=("Inter", 32 * -1)
        )

        self.button_image_1 = PhotoImage(
            file=Path(__file__).parent / self.ASSETS_PATH / ("button_1.png"))
        self.button_1 = Button(
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.gui.change_password(self, self.username, self.email,
                                                     self.current_password.get("1.0", 'end-1c'),
                                                     self.pass1.get("1.0", 'end-1c'),
                                                     self.pass2.get("1.0", 'end-1c')),
            relief="flat"
        )
        self.button_1.place(
            x=60.0,
            y=291.0,
            width=230.0,
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
            x=112.0,
            y=346.0,
            width=129.0,
            height=35.0
        )

    def destroy(self):
        self.window.destroy()
