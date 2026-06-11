def movimiento():
    global ubicacion
    ubicacion = "root"

def limpieza_de_la_terminal(encabezado, archivos, text):
    import time
    print(f"============================")
    print(f"  {encabezado}  ")
    print(f"============================")
    time.sleep(1.5)
    for i in range(0, 101, 1):
        print(f"{text} {archivos} {{{i}%}}")
        time.sleep(0.1)

def diseño():
    print("")
    print("====================")
    print("  Os.WWD//Terminal  ")
    print("====================")
    print("")

def ejecutar():
    global ubicacion
    
    while True:
        
        comando = input(f"Terminal//{ubicacion}//> ")
    
        comando = comando.strip().lower()
        
        if comando == "salir":
            print("Saliste de la terminal")
            break
        
        elif comando == "ayuda":
            print("1.// cd archivo  : mover a la carpeta")
            print("2.// cd..  : para ir para atras")
            print("3.// dir  : para ver todos tus archivos")
            print("4.// cls  : para limpiar pantalla")
            
        elif ubicacion == "root/archivo/Links" and comando == "dir":
             print("      // Dir:     Mia Kalifha.com")
             print("      //Dir:      xxx.com")
             print("")
             print("      //Bits:      Bits 123")
             
        elif ubicacion == "root/archivo/Carpeta de juegos" and comando == "dir":
             print("      // Dir:     Furri_Love")
             print("      //Dir:      FreFire")
             print("      //Dir:      Folnite")
             print("      //Dir:      Roblox")
             print("")
             print("      //Bits:      Bits 608")
            
        elif ubicacion == "root/archivo" and comando == "dir":
            print("      // Dir:     Links")
            print("      //Dir:      Carpeta de juegos")
            print("")
            print("      //Bits:      Bits 293")
            
        elif comando == "dir":
            print("      // Dir:     archivo")
            
        elif comando == "cls":
            a = 200
            contador = 0
            while contador < a:
                print("\n")
                contador += 1
                pass
            diseño()
            
        elif comando == "cd archivo":
            ubicacion = "root/archivo"
            print("te moviste a un archivo")
            
        elif comando == "cd links" and ubicacion == "root/archivo":
            ubicacion = "root/archivo/Links"
            
        elif comando == "cd carpeta de juegos" and ubicacion == "root/archivo":
            ubicacion = "root/archivo/Carpeta de juegos"
            
        elif ubicacion == "root/archivo/Carpeta de juegos" and comando == "cd..":
            ubicacion = "root/archivo"
            
        elif ubicacion == "root/archivo/Links" and comando == "cd..":
            ubicacion = "root/archivo"
            
        elif comando == "cd carpeta de juegos":
            print("no puedes saltarte pasos...")
            
        elif comando == "cd links":
            print("no puedes saltarte pasos...")
            
        elif ubicacion == "root" and comando == "cd..":
            print("Ya estas en el inicio. No puedes ir mas atras")
            
        elif comando == "cd..":
            ubicacion = "root"
            print("regresaste hacia atras")
            
        elif comando == "cd":
            print("te falta algo mas!!")
            
        elif comando == "":
            pass
        
        elif comando == "pip install anthony":
            limpieza_de_la_terminal("DESCARGANDO ANTHONY_PACK", "ANTHONY_PACK", "DESCARGANDO")
            diseño()
            pass
        
        elif comando == "pip install pornito":
            limpieza_de_la_terminal("DESINSTALANDO System32", "System32", "DESINSTALANDO LOS ARCHIVOS DE")
            return
        
        else:
            print(f"no existe este comando: {comando}")

movimiento()
diseño()
ejecutar()