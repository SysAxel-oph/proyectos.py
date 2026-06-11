import random

jugar = 'si'
numero_secreto = 0

numero_secreto = random.randint(1, 200)
respuesta = 0
while jugar != 'no':
    try:
        respuesta = int(input("Adivina el numero secreto Pixel!: "))
        
        if respuesta < numero_secreto:
            print("Esta muy bajo pixel, subele mas")
        elif respuesta > numero_secreto:
            print("Esta muy alto pixel, bajale mas")
        else:
            print("Ganaste pixel, felicidades!")
            jugar = input("Quieres darle otra vez pixeleados?('si'/'no'): ").lower()
        
    except ValueError:
        print("solo numeros aqui pequeña ")
        
        jugar = input("Quieres darle otra vez pixeleados?('si'/'no'): ").lower()