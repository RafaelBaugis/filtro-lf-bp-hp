import tkinter as tk
import math
from scipy import constants

root = tk.Tk()

label = tk.Label(root, text="Insira a frequência inicial:")
label.pack()

entry = tk.Entry(root)
entry.pack()

label2 = tk.Label(root, text="Insira a frequência final:")
label2.pack()

entry2 = tk.Entry(root)
entry2.pack()

label3 = tk.Label(root, text="Insira a impedância:")
label3.pack()

entry3 = tk.Entry(root)
entry3.pack()

pass_type_label = tk.Label(root, text="Selecione o tipo de filtro:")
pass_type_label.pack()

pass_type_var = tk.StringVar(value="Passa Alta")

pass_type_menu = tk.OptionMenu(root, pass_type_var, "Passa Alta", "Passa Baixa", "Passa Banda")
pass_type_menu.pack()

button = tk.Button(root, text="Calcular")
button.pack()

result_label = tk.Label(root)

def calculate():
    frequency_initial = float(entry.get())
    frequency_final = float(entry2.get())
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
    else:
        R1 = impedance
        R2 = impedance
        capacitance = 1 / (4 * math.pi ** 2 * frequency_initial ** 2 * R1 * R2 / (R1 + R2) ** 2 - ((1 / (2 * math.pi * frequency_initial)) ** 2 / capacitance) * ((1 / (2 * math.pi * frequency_final)) ** 2 / capacitance))
        inductance = math.sqrt(((1 / (2 * math.pi * frequency_initial)) ** 2 / capacitance) * ((1 / (2 * math.pi * frequency_final)) ** 2 / capacitance))

    inductance_str = "Indutância: {:.2f} uH".format(inductance*1000000)
    capacitance_str = "Capacitância: {:.2f} uF".format(capacitance*1000000)

    result_label.config(text=inductance_str + "\n" + capacitance_str)

button.config(command=calculate)

result_label.pack()

root.mainloop()
