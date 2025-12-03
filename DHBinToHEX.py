import os
import random

salas = [1, 2, 3, 4,
         5, 6, 7, 8]

dias = ["Seg", "Ter", "Qua", "Qui", "Sex", "Sáb"]

horario_termino = ["8:00:00", "9:00:00", "10:00:00", "11:00:00",
                  "12:00:00", "13:00:00", "14:00:00", "15:00:00",
                  "16:00:00", "17:00:00", "18:00:00", "19:00:00",
                  "19:20:00", "20:10:00", "21:00:00", "21:50:00"]

def binToHex(bits):
    return hex(int(bits,2))[2:].upper()

def gerar_binario_mock():
    bits = [str(random.randint(0, 1)) for _ in range(16)]
    return "".join(bits)

def salvar_arquivo(dia, sala, hex_str):
    caminho = f"api/{dia}/{sala}/HorHex.txt"
    with open(caminho, "w") as f:
        f.write(hex_str)


for dia in dias:
    for sala in salas:
        os.makedirs(f"api/{dia}/{sala}/", exist_ok=True)
bits1 = gerar_binario_mock()
bits2 = "0000000011111111"        # Hex tem que ser F
print(bits1, bits2, binToHex(bits1), binToHex(bits2))

for sala in salas:
    for dia in dias:
        binario = gerar_binario_mock()   # depois isso vira SQL
        print(binario, sala, dia)
        hexadecimal = binToHex(binario)
        print(hexadecimal)
        salvar_arquivo(dia, sala, hexadecimal)