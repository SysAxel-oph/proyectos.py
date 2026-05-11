import tkinter

ventana = tkinter.Tk()
ventana.title("registro: ")
ventana.geometry("900x900")
ventana.config(bg = "")

titulo = tkinter.Label(ventana, text = "antes de todo registrate: ")
a = tkinter.Label(ventana, text = "cual es tu nombre: ")
titulo.pack()
a.pack()

aviso = tkinter.Label(ventana, text = "")
aviso.pack()

nombre_tk = tkinter.Entry(ventana)
nombre_tk.pack()

contraseña_tk = tkinter.Entry(ventana, show = "*")
contraseña_tk.pack()

saldo = 0.0
a = ""

def registro():
    nombre = nombre_tk.get()
    clave = contraseña_tk.get()
    clave1 = "axel221"
    
    if nombre.isalpha():
        aviso.config(text = "")
        if clave == "":
             aviso.config(text = "esta vacio", fg = "orange")
        elif clave == clave1:
             aviso.config(text = "CORRECTO", fg = "green")
             cuenta()
        else:
             aviso.config(text = "la contraseña esta mal", fg = "red")
        

boton = tkinter.Button(ventana, text = "continue", command = registro)
boton.pack()

  
def cuenta():
    global saldo
    global x
    nombre_tk.get()
    
    global ventana1
    ventana1 = tkinter.Toplevel(ventana)
    ventana1.title("BANCO, CUENTA: ")
    ventana1.geometry("900x900")
    ventana1.config(bg = "")
    
    saludo = tkinter.Label(ventana1, text = "hola " + nombre_tk.get())
    x = tkinter.Label(ventana1, text = f"tu saldo es de: {saldo}")
    w = tkinter.Label(ventana1, text = "que quieres hacer hoy? ")
    o = tkinter.Label(ventana1, text = "seleciona: ")
    saludo.pack()
    x.pack()
    w.pack()
    o.pack()
    
    
    boton1 = tkinter.Button(ventana1, text = "1, para Deposito", command = Deposito)
    boton2 = tkinter.Button(ventana1, text = "2, para Retiro", command = retiro)
    #boton3 = tkinter.Button(ventana1, text = "3, para salir", command = ventana1.destroy())
    boton1.pack()
    boton2.pack()
    
def Deposito():
    global saldo
    global ventana2
    global D
    ventana2 = tkinter.Toplevel(ventana1)
    ventana2.title("BANCO, DEPOSITO: ")
    ventana2.geometry("900x900")
    ventana2.config(bg = "")
    
    p = tkinter.Label(ventana2, text = "Aqui eligue el monto que quieres Depositar: ")
    D = tkinter.Entry(ventana2)
    p.pack()
    D.pack()
    
    boton4 = tkinter.Button(ventana2, text = "okay", command = deposito1)
    boton4.pack()
    
def deposito1():
    global saldo
    dinero = D.get()
    u = float(dinero)
    saldo = saldo + u
    
    x.config(text = f"tu saldo ahora es de: {saldo}")
    ventana2.destroy()
    
def retiro():
    global saldo
    global ventana3
    global n
    ventana3 = tkinter.Toplevel(ventana1)
    ventana3.title("BANCO, Retiro: ")
    ventana3.geometry("900x900")
    ventana3.config(bg = "")
    
    p = tkinter.Label(ventana3, text = "Cuanto quieres Retirar hoy: ")
    n = tkinter.Entry(ventana3)
    b = tkinter.Label(ventana3, text = "")
    p.pack()
    n.pack()
    b.pack()
    
    boton5 = tkinter.Button(ventana3, text = "okay", command = retiro1)
    boton5.pack()
    
def retiro1():
    global saldo
    dinero = n.get()
    
    try:
        u = float(dinero)
    
        if u > saldo:
            b.config(ventana3, text = "te estas pasando de tu monto", fg = "red")
        elif u <= saldo:
            saldo = saldo - u
            x.config(text = f"{saldo}")
            ventana3.destroy()
    except ValueError:
        b.config(ventana3, text = "por favor, ingresa un numero valido", fg = "red")

  
ventana.mainloop()