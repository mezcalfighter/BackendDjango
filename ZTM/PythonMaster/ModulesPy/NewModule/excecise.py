import sys
import random

start = int(sys.argv[1])
stop = int(sys.argv[2])
random_num = random.randint(start,stop)
input_num = -1

while input_num != random_num:
    input_num = int(input(f"Ingrese un numero entre {start} y {stop}: "))
    if input_num == random_num:
        print("Numero encontrado!")
    else:
        print(f"El numero {input_num} no es, intente de nuevo")