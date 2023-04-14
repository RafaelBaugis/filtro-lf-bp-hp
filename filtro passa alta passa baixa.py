import tkinter as tk
import math
from scipy import constants

root = tk.Tk()

label = tk.Label(root, text="Insira a frequência de corte:")
label.pack()

entry = tk.Entry(root)
entry.pack()

label3 = tk.Label(root, text="Insira a impedância:")
label3.pack()

entry3 = tk.Entry(root)
entry3.pack()

pass_type_label = tk.Label(root, text="Selecione o tipo de filtro:")
pass_type_label.pack()

pass_type_var = tk.StringVar(value="Passa Alta")

pass_type_menu = tk.OptionMenu(root, pass_type_var, "Passa Alta", "Passa Baixa")
pass_type_menu.pack()

button = tk.Button(root, text="Calcular")
button.pack()

result_label = tk.Label(root)

def calculate():
    frequency_initial = float(entry.get())
    impedance = float(entry3.get())

    capacitance = 0
    inductance = 0

    # Cálculo da bobina e capacitor usando Scipy
    if pass_type_var.get() == "Passa Alta":
        capacitance = 1 / (2 * math.pi * frequency_initial * impedance)
        inductance = capacitance / (constants.pi ** 2 * frequency_initial ** 2)
    elif pass_type_var.get() == "Passa Baixa":
        inductance = impedance / (2 * math.pi * frequency_initial)
        capacitance = inductance / (constants.pi ** 2 * frequency_initial ** 2)

    inductance_str = "Indutância: {:.2f} mH".format(inductance*1000)
    capacitance_str = "Capacitância: {:.2f} uF".format(capacitance*1000000)

    result_label.config(text=inductance_str + "\n" + capacitance_str)

button.config(command=calculate)

result_label.pack()

root.mainloop()