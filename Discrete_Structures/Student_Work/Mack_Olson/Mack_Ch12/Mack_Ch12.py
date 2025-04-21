import customtkinter as ctk
from PIL import Image

# Define the NAND gate
def NAND(a, b):
    return not (a and b)

# Define the NOR gate
def NOR(a, b):
    return not (a or b)

# Using only NAND to create NOT, AND, OR
def NOT_using_NAND(a):
    return NAND(a, a)

def AND_using_NAND(a, b):
    return NOT_using_NAND(NAND(a, b))

def OR_using_NAND(a, b):
    return NAND(NOT_using_NAND(a), NOT_using_NAND(b))

# Using only NOR to create NOT, AND, OR
def NOT_using_NOR(a):
    return NOR(a, a)

def OR_using_NOR(a, b):
    return NOT_using_NOR(NOR(a, b))

def AND_using_NOR(a, b):
    return NOR(NOT_using_NOR(a), NOT_using_NOR(b))


class LogicGateApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("NAND and NOR Logic Gates")
        self.geometry("600x700")

        # Load images
        self.lit_bulb = ctk.CTkImage(Image.open("lit-bulb.png"), size=(30, 30))
        self.dim_bulb = ctk.CTkImage(Image.open("dim-bulb.png"), size=(30, 30))

        # Inputs
        self.label_a = ctk.CTkLabel(self, text="Input A:")
        self.label_a.pack(pady=5)
        self.switch_a = ctk.CTkSwitch(self, text="", command=self.update_outputs)
        self.switch_a.pack(pady=5)

        self.label_b = ctk.CTkLabel(self, text="Input B:")
        self.label_b.pack(pady=5)
        self.switch_b = ctk.CTkSwitch(self, text="", command=self.update_outputs)
        self.switch_b.pack(pady=5)

        # Frame to hold results
        self.results_frame = ctk.CTkScrollableFrame(self, width=500, height=500)
        self.results_frame.pack(pady=20)

        self.result_widgets = []
        self.update_outputs()

    def update_outputs(self):
        a = bool(self.switch_a.get())
        b = bool(self.switch_b.get())

        # Clear old results
        for widget in self.result_widgets:
            widget.destroy()
        self.result_widgets = []

        outputs = [
            ("NAND(a, b)", NAND(a, b)),
            ("NOR(a, b)", NOR(a, b)),
            ("NOT_using_NAND(a)", NOT_using_NAND(a)),
            ("AND_using_NAND(a, b)", AND_using_NAND(a, b)),
            ("OR_using_NAND(a, b)", OR_using_NAND(a, b)),
            ("NOT_using_NOR(a)", NOT_using_NOR(a)),
            ("AND_using_NOR(a, b)", AND_using_NOR(a, b)),
            ("OR_using_NOR(a, b)", OR_using_NOR(a, b)),
        ]

        for text, value in outputs:
            frame = ctk.CTkFrame(self.results_frame)
            frame.pack(pady=5, padx=10, fill="x")

            label = ctk.CTkLabel(frame, text=f"{text} = {value}", anchor="w")
            label.pack(side="left", padx=10)

            bulb = ctk.CTkLabel(frame, image=self.lit_bulb if value else self.dim_bulb, text="")
            bulb.pack(side="right", padx=10)

            self.result_widgets.append(frame)

if __name__ == "__main__":
    ctk.set_appearance_mode("System")
    app = LogicGateApp()
    app.mainloop()
