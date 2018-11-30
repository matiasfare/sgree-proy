#Pruebas Calculo entre fechas
from datetime import datetime, date, time, timedelta
import calendar

ahora = datetime.now()  # Obtiene fecha y hora actual
# print("Fecha y Hora:", ahora)  # Muestra fecha y hora
# print("Fecha y Hora UTC:",ahora.utcnow())  # Muestra fecha/hora UTC
# print("Día:",ahora.day)  # Muestra día
# print("Mes:",ahora.month)  # Muestra mes
# print("Año:",ahora.year)  # Muestra año
# print("Hora:", ahora.hour)  # Muestra hora
# print("Minutos:",ahora.minute)  # Muestra minuto
# print("Segundos:", ahora.second)  # Muestra segundo
# print("Microsegundos:",ahora.microsecond)  # Muestra microsegundo

# print("Horas:")
# hora1 = time(10, 5, 0)  # Asigna 10h 5m 0s
# print("\tHora1:", hora1)
# hora2 = time(23, 15, 0)  # Asigna 23h 15m 0s
# print("\tHora2:", hora2)

# # Compara horas
# print("\tHora1 < Hora2:", hora1 < hora2)  # True

def convertir_a_fecha(cadena_fecha):
    formato_fecha = "%Y-%m-%d"
    #Aqui se toma el string del usuario y se convierte a tipo Datetime con el formato especificado
    fecha= datetime.strptime(cadena_fecha, formato_fecha).date()
    return fecha


val = 5
print("Calcula Validez:")
print("Tiempo de Validez: ", val)
fecharec = '2018-11-26'
fecharec = convertir_a_fecha(fecharec)

fecha1 = fecharec  + timedelta(days=val) # Recibe fecha del recibo y añade tiempo de validez, resultando la fecha de vencimiento

print("\tFecha Vencimiento Recibo:", fecha1)

# Suma a la fecha actual 2 días
fecha2 = date.today()
print("\tFecha Actual:", fecha2)

# Compara fechas
print("\tEs valido el Recibo:", fecha1 >= fecha2)  # Da Falso si ya vencio y True y aun es valido




# class Cliente():
#     '''Clase para crear un Cliente'''
#     tipo = "cliente"
#     contactos = []
#     def __init__(self, documento, nombre, apellido, contacto):
#         self.nombre = nombre
#         self.apellido = apellido
#         self.documento = documento
#         self.contacto = contacto

# lista = []

# cliente1 = Cliente(5749,'Matias','Fare', '0981135750')
# cliente2 = Cliente(5748,'Anibal','Fare', '0981135750')

# lista.append(cliente1)
# lista.append(cliente2)

# #Si el objeto existe en la lista, imprime el ob y su posicion en la lista

# if cliente1 in lista:
#     print(cliente1)
#     indice = lista.index(cliente1)
#     print(indice)


# diccionarios = {
#     'clientes': {},
#     'recibos': {}
# }

# dbroot = {'dicc': diccionarios}

# cliente1 = Cliente(5749,'Matias','Fare', '0981135750')
# cliente2 = Cliente(5748,'Anibal','Fare', '0981135750')

# dic_actual = dbroot['dicc']

# dic_actual = dic_actual['clientes'] 

# dic_actual[cliente1.documento] = cliente1
# dic_actual[cliente2.documento] = cliente2

# dic_actual[cliente1.documento] = cliente1



# for clave in dic_actual:
#     obj = dic_actual[clave]
#     print(str(clave) + ":" + obj.nombre + ", " + obj.apellido)



# from tkinter import Tk, Label, Button, StringVar

# class MyFirstGUI:
#     LABEL_TEXT = [
#         "This is our first GUI!",
#         "Actually, this is our second GUI.",
#         "We made it more interesting...",
#         "...by making this label interactive.",
#         "Go on, click on it again.",
#     ]
#     def __init__(self, master):
#         self.master = master
#         master.title("A simple GUI")

#         self.label_index = 0
#         self.label_text = StringVar()
#         self.label_text.set(self.LABEL_TEXT[self.label_index])
#         self.label = Label(master, textvariable=self.label_text)
#         self.label.bind("<Button-1>", self.cycle_label_text)
#         self.label.pack()

#         self.greet_button = Button(master, text="Greet", command=self.greet)
#         self.greet_button.pack()

#         self.close_button = Button(master, text="Close", command=master.quit)
#         self.close_button.pack()

#     def greet(self):
#         print("Greetings!")

#     def cycle_label_text(self, event):
#         self.label_index += 1
#         self.label_index %= len(self.LABEL_TEXT) # wrap around
#         self.label_text.set(self.LABEL_TEXT[self.label_index])

# root = Tk()
# my_gui = MyFirstGUI(root)
# root.mainloop()

# #-------------------Actualizacion con validacion de datos---------------

# from tkinter import Tk, Label, Button, Entry, IntVar, END, W, E

# class Calculator:

#     def __init__(self, master):
#         self.master = master
#         master.title("Calculator")

#         self.total = 0
#         self.entered_number = 0

#         self.total_label_text = IntVar()
#         self.total_label_text.set(self.total)
#         self.total_label = Label(master, textvariable=self.total_label_text)

#         self.label = Label(master, text="Total:")

#         vcmd = master.register(self.validate) # we have to wrap the command
#         self.entry = Entry(master, validate="key", validatecommand=(vcmd, '%P'))

#         self.add_button = Button(master, text="+", command=lambda: self.update("add"))
#         self.subtract_button = Button(master, text="-", command=lambda: self.update("subtract"))
#         self.reset_button = Button(master, text="Reset", command=lambda: self.update("reset"))

#         # LAYOUT

#         self.label.grid(row=0, column=0, sticky=W)
#         self.total_label.grid(row=0, column=1, columnspan=2, sticky=E)

#         self.entry.grid(row=1, column=0, columnspan=3, sticky=W+E)

#         self.add_button.grid(row=2, column=0)
#         self.subtract_button.grid(row=2, column=1)
#         self.reset_button.grid(row=2, column=2, sticky=W+E)

#     def validate(self, new_text):
#         if not new_text: # the field is being cleared
#             self.entered_number = 0
#             return True

#         try:
#             self.entered_number = int(new_text)
#             return True
#         except ValueError:
#             return False

#     def update(self, method):
#         if method == "add":
#             self.total += self.entered_number
#         elif method == "subtract":
#             self.total -= self.entered_number
#         else: # reset
#             self.total = 0

#         self.total_label_text.set(self.total)
#         self.entry.delete(0, END)

# root = Tk()
# my_gui = Calculator(root)
# root.mainloop()



# import random
# from tkinter import Tk, Label, Button, Entry, StringVar, DISABLED, NORMAL, END, W, E

# class GuessingGame:
#     def __init__(self, master):
#         self.master = master
#         master.title("Guessing Game")

#         self.secret_number = random.randint(1, 100)
#         self.guess = None
#         self.num_guesses = 0

#         self.message = "Guess a number from 1 to 100"
#         self.label_text = StringVar()
#         self.label_text.set(self.message)
#         self.label = Label(master, textvariable=self.label_text)

#         vcmd = master.register(self.validate) # we have to wrap the command
#         self.entry = Entry(master, validate="key", validatecommand=(vcmd, '%P'))

#         self.guess_button = Button(master, text="Guess", command=self.guess_number)
#         self.reset_button = Button(master, text="Play again", command=self.reset, state=DISABLED)

#         self.label.grid(row=0, column=0, columnspan=2, sticky=W+E)
#         self.entry.grid(row=1, column=0, columnspan=2, sticky=W+E)
#         self.guess_button.grid(row=2, column=0)
#         self.reset_button.grid(row=2, column=1)

#     def validate(self, new_text):
#         if not new_text: # the field is being cleared
#             self.guess = None
#             return True

#         try:
#             guess = int(new_text)
#             if 1 <= guess <= 100:
#                 self.guess = guess
#                 return True
#             else:
#                 return False
#         except ValueError:
#             return False

#     def guess_number(self):
#         self.num_guesses += 1

#         if self.guess is None:
#             self.message = "Guess a number from 1 to 100"

#         elif self.guess == self.secret_number:
#             suffix = '' if self.num_guesses == 1 else 'es'
#             self.message = "Congratulations! You guessed the number after %d guess%s." % (self.num_guesses, suffix)
#             self.guess_button.configure(state=DISABLED)
#             self.reset_button.configure(state=NORMAL)

#         elif self.guess < self.secret_number:
#             self.message = "Too low! Guess again!"
#         else:
#             self.message = "Too high! Guess again!"

#         self.label_text.set(self.message)

#     def reset(self):
#         self.entry.delete(0, END)
#         self.secret_number = random.randint(1, 2)
#         self.guess = 0
#         self.num_guesses = 0

#         self.message = "Guess a number from 1 to 100"
#         self.label_text.set(self.message)

#         self.guess_button.configure(state=NORMAL)
#         self.reset_button.configure(state=DISABLED)

# root = Tk()
# my_gui = GuessingGame(root)
# root.mainloop()




