import tkinter
import sys
import os
import time
import hashlib

def seguridad():
    global lista_nombres, lista_claves, lista_saldo
    
    archivos = ["users.txt", "clave1.txt", "saldo.txt"]
    
    for arc in archivos:
        if not os.path.exists(arc):
            with open(arc, "w") as f:
                pass
            print(f"Configuracion: Se ha creado {arc} para el fucionamiento")
    
    with open("users.txt", 'r') as f:
        lista_nombres = [linea.strip() for linea in f.readlines()]
        
    with open("clave1.txt", 'r') as f:
        lista_claves = [linea.strip() for linea in f.readlines()]
        
    with open("saldo.txt", 'r') as f:
        lista_saldo = [linea.strip() for linea in f.readlines()]
        
def guardar_datos():
    global lista_saldo
    with open("saldo.txt", 'w') as f:
        for s in lista_saldo[posicion]:
            f.write(str(s) + "\n")

def diseño():
    global boton_creado
    global boton_continuar
    global ventana
    ventana = tkinter.Tk()
    ventana.resizable(0,0)
    ventana.title("registro: ")
    ventana.geometry("900x900")
    ventana.config(bg = "SystemButtonFace")
    boton_creado = False
    boton_continuar = None
    
    return ventana

def titulo1():
    global titulo
    global a
    global q
    titulo = tkinter.Label(ventana, text = "Antes de todo registrate: ", font = ("Arial", 20, "bold"))
    a = tkinter.Label(ventana, text = "Cual es tu nombre: ", font = ("Arial", 20, "bold"))
    q = tkinter.Label(ventana, text = "Introduce tu contraseña: ", font = ("Arial", 18, "bold"))
    titulo.pack()
    a.pack()

def aviso1():
    global aviso
    aviso = tkinter.Label(ventana, text = "")

def userName():
    global nombre_tk
    nombre_tk = tkinter.Entry(ventana, font = ("Arial", 20, "bold"))
    nombre_tk.pack(pady = 10)

def contra():
    global contraseña_tk
    contraseña_tk = tkinter.Entry(ventana, show = "*", font = ("Arial", 20, "bold"))
    q.pack()
    contraseña_tk.pack(pady = 10)
    aviso.pack()
    
def cifrar_datos(contraseña_limpia):
    contraseña_cifrada = hashlib.sha256(contraseña_limpia.encode('utf-8')).hexdigest()
    return contraseña_cifrada

def variable():
    global saldo
    saldo = 0.0

def registro():
    global boton_creado
    global saldo
    global posicion
    global nombre
    nombre = nombre_tk.get()
    clave = contraseña_tk.get()
    
    clave_encriptada = cifrar_datos(clave)
    
    if nombre in lista_nombres:
        posicion = lista_nombres.index(nombre)
    
        if nombre.isalpha():
            aviso.config(text = "")
            if clave == "":
                 aviso.config(text = "tienes vacios vacios", fg = "orange", font = ("Arial", 15))
            elif clave_encriptada == lista_claves[posicion]:
                 saldo = float(lista_saldo[posicion])
                 aviso.config(text = "BIENVENIDO", fg = "green", font = ("Arial", 15))
                 ventana.after(2000, cuenta)
                 aviso.config(text = "estan cargando los datos de la cuenta...", fg = "blue", font = ("Arial", 15))
            else:
                 aviso.config(text = "la contraseña esta mal", fg = "red", font = ("Arial", 15))
             
    else:
        with open("users.txt", 'a') as f:
            aviso.config(text = "nuevo usuario registrado", fg = "blue", font = ("Arial", 15))
            
            if nombre.strip() != "" and clave.strip() != "":
                with open("users.txt", 'a') as f:
                    f.write(nombre + "\n")
                with open("clave1.txt", 'a') as f:
                    f.write(clave_encriptada + "\n")
                with open("saldo.txt", 'a') as f:
                    
                    lista_nombres.append(nombre)
                    lista_claves.append(clave_encriptada)
                    lista_saldo.append("0.0")
                    guardar_datos()
                    cuenta()
            else:
                aviso.config(text = "no puedes dejar espacios vacios", fg = "red")

    if not boton_creado:
        boton_continuar = tkinter.Button(ventana, text = "continue", font = ("Arial", 11, "bold"), width = 14, height = 3, command = registro)
        boton_continuar.pack()
        boton_creado = True
  
def cuenta():
    global saldo
    global x
    nombre_tk.get()
    
    ventana.withdraw()
    
    global ventana1
    ventana1 = tkinter.Toplevel(ventana)
    ventana1.resizable(0,0)
    ventana1.title("BANCO, CUENTA: ")
    ventana1.geometry("900x900")
    ventana1.config(bg = "SystemButtonFace")
    
    t = tkinter.Label(ventana1, text = "BIENVENIDO, ESTAS DENTRO DE LA CUENTA.", font = ("Arial", 20, "bold"))
    saludo = tkinter.Label(ventana1, text = "hola " + nombre_tk.get(), font = ("Arial", 15, "bold"))
    x = tkinter.Label(ventana1, text = f"tu saldo es de: ${saldo:,.2f}", font = ("Arial", 18, "bold"), padx = 10)
    w = tkinter.Label(ventana1, text = "que quieres hacer hoy? ", font = ("Arial", 19, "bold"))
    o = tkinter.Label(ventana1, text = "seleciona: ", font = ("Arial", 20, "bold"))
    t.pack()
    saludo.pack()
    x.pack()
    w.pack()
    o.pack()
    
    boton1 = tkinter.Button(ventana1, text = "1, para Deposito", font = ("Arial", 11, "bold"), width = 14, height = 3, command = Deposito)
    boton2 = tkinter.Button(ventana1, text = "2, para Retiro", font = ("Arial", 11, "bold"), width = 14, heigh = 3, command = retiro)
    boton3 = tkinter.Button(ventana1, text = "4, para salir", font = ("Arial", 11, "bold"), width = 14, heigh = 3, command = salir)
    boton7 = tkinter.Button(ventana1, text = "3, para Trans", font = ("Arial", 11, "bold"), width = 14, heigh = 3, command = Transaccion)
    boton1.pack()
    boton2.pack()
    boton7.pack()
    boton3.pack()
    
def Deposito():
    global saldo
    global ventana2
    global D
    global bb
    ventana2 = tkinter.Toplevel(ventana1)
    ventana2.resizable(0,0)
    ventana2.title("BANCO, DEPOSITO: ")
    ventana2.geometry("900x900")
    ventana2.config(bg = "SystemButtonFace")
    
    p = tkinter.Label(ventana2, text = "Aqui eligue el monto que quieres Depositar: ", font = ("Arial", 20, "bold"))
    D = tkinter.Entry(ventana2, font = ("Arial", 20, "bold"))
    bb = tkinter.Label(ventana2, text = "", font = ("Arial", 15, "bold"))
    p.pack(pady = 10)
    D.pack(pady = 10)
    bb.pack(pady = 10)
    
    boton4 = tkinter.Button(ventana2, text = "okay", font = ("Arial", 11, "bold"), width = 14, heigh = 3, command = deposito1)
    boton8 = tkinter.Button(ventana2, text = "Regresar", font = ("Arial", 11, "bold"), width = 14, heigh = 3, command = ventana2.destroy)
    boton4.pack()
    boton8.pack()
    
def deposito1():
    global saldo   
    dinero = D.get()
    
    try:
        u = float(dinero)
        
        saldo = saldo + u
        lista_saldo[posicion] = str(saldo)
        guardar_datos()
        x.config(text = f"tu saldo es de: ${saldo:,.2f}")
        ventana2.destroy()
    except ValueError:
        bb.config(text = "por favor, ingresa un numero valido", fg = "orange")
    
def retiro():
    global saldo
    global ventana3
    global i
    global b
    ventana3 = tkinter.Toplevel(ventana1)
    ventana3.resizable(0,0)
    ventana3.title("BANCO, Retiro: ")
    ventana3.geometry("900x900")
    ventana3.config(bg = "SystemButtonFace")
    
    p = tkinter.Label(ventana3, text = "Cuanto quieres Retirar hoy: ", font = ("Arial", 20, "bold"))
    i = tkinter.Entry(ventana3, font = ("Arial", 20, "bold"))
    b = tkinter.Label(ventana3, text = "", font = ("Arial", 15, "bold"))
    p.pack()
    i.pack()
    b.pack(pady = 10)
    
    boton5 = tkinter.Button(ventana3, text = "okay", font = ("Arial", 11, "bold"), width = 14, heigh = 3, command = retiro1)
    boton9 = tkinter.Button(ventana3, text = "Regresar", font = ("Arial", 11, "bold"), width = 14, heigh = 3, command = ventana3.destroy)
    boton5.pack()
    boton9.pack()
    
def retiro1():
    global saldo
    dinero = i.get()
    
    try:
        u = float(dinero)
    
        if u > saldo:
            b.config(text = "te estas pasando de tu monto", fg = "red")
        elif u <= saldo:
            saldo = saldo - u
            lista_saldo[posicion] = str(saldo)
            guardar_datos()
            x.config(text = f"tu saldo es de: ${saldo:,.2f}")
            ventana3.destroy()
    except ValueError:
        b.config(text = "por favor, ingresa un numero valido", fg = "orange")
    
def salir():
    
    ventana1.destroy()
    
    salir1 = sys.executable
    os.execl(salir1, salir1, *sys.argv)
    
def Transaccion():
    global ent_destino
    global ventana4
    global monto_destino
    global boton6
    global error
    ventana4 = tkinter.Toplevel(ventana1)
    ventana4.resizable(0,0)
    ventana4.title("BANCO, transaccion: ")
    ventana4.geometry("900x900")
    ventana4.config(bg = "SystemButtonFace")
    
    g = tkinter.Label(ventana4, text = "Cuanto quieres transferir: ", font = ("Arial", 25, "bold"))
    n = tkinter.Label(ventana4, text = "Ingresa el nombre de la persona: ", font = ("Arial", 18, "bold"))
    ke = tkinter.Label(ventana4, text = "Ingresa la cantidad que le quieres transferir: ", font = ("Arial", 20, "bold"))
    ent_destino = tkinter.Entry(ventana4, font = ("Arial", 20, "bold"))
    monto_destino = tkinter.Entry(ventana4, text = "", font = ("Arial", 20, "bold"))
    error = tkinter.Label(ventana4, text = "", font = ("Arial", 15, "bold"), bg = "SystemButtonFace")
    g.pack()
    n.pack()
    ent_destino.pack()
    ke.pack()
    monto_destino.pack()
    error.pack()
    
    boton6 = tkinter.Button(ventana4, text = "okey", font = ("Arial", 11, "bold"), width = 14, heigh = 3, command = transaccion1)
    boton10 = tkinter.Button(ventana4, text = "Regresar", font = ("Arial", 11, "bold"), width = 14, heigh = 3, command = ventana4.destroy)
    boton6.pack()
    boton10.pack()
    
def transaccion1():
    global error
    
    destino = ent_destino.get()
    cantidad = monto_destino.get()
    
    error.config(text = "")
    
    if destino == "":
        error.config(text = "Agrega al usuario ", fg = "orange")
        return
    
    if cantidad == "":
        error.config(text = "Ingresa el monto ", fg = "orange")
        return
    
    if destino == lista_nombres[posicion]:
        error.config(text = "No te puedes tranferir a ti mismo ", fg = "orange")
        return
    
    if not destino in lista_nombres:
        error.config(text = "No puedes pasar dinero a un usuario no existente ", fg = "orange")
        return
            
    pos_destino = lista_nombres.index(destino)
    
    try:
        monto_operacion = float(cantidad)
        
        mi_saldo_resta = float(lista_saldo[posicion]) - monto_operacion
        lista_saldo[posicion] = str(mi_saldo_resta)
        
        saldo_destino = float(lista_saldo[pos_destino]) + monto_operacion
        lista_saldo[pos_destino] = str(saldo_destino)
    except ValueError:
        error.config(text = "Solo numeros aqui ", fg = "red")
        return
    
    if monto_operacion > float(lista_saldo[posicion]):
            error.config(text = "No te puedes pasar de tu monto ", fg = "orange")
            return
        
    with open("saldo.txt", 'w') as f:
        for s in lista_saldo:
            f.write(s + "\n")
            
    global saldo
    saldo = mi_saldo_resta
    x.config(text = f"tu saldo es de: ${mi_saldo_resta:,.2f}")
    guardar_datos()
    ventana4.destroy()
                

seguridad()
ventana = diseño()
titulo1()
aviso1()
userName()
contra()
variable()
registro()
ventana.mainloop()