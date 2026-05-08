while True:
        user = input("Cual es tu nombre: ").lower()
        if user.isalpha():
            break
        else:
            print("solo puedes usar texto aqui... ")
        
while True:
    try:
        contra = int(input("crea una contraseña: "))
        break
    except ValueError:
        print("solo puedes escribir numeros aqui... ")

for i in range(3):
    while True:
        try:
    
            contraseña = int(input("introduce tu contraseña: "))
            break
        except ValueError:
            print("solo numeros bro... ")
    
    if contra == contraseña:
        print("BIENVENIDO: ", user)
        break
    else:
        print(f"contraseña incorrecta, intentos {2 - i}")
else:
    print("TE BLOQUEAMOS LA CUENTA")