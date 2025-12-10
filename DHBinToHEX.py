import os
import sqlite3

conn = sqlite3.connect("db copy.sqlite3")       # Alterar diretório para o banco de dados correto

cursor = conn.cursor()

salas = [str(i) for i in range(1, 21)]  # Lista de salas disponíveis (como strings)
dias = [str(j) for j in range (0,6)]  # 0=Segunda ... 5=Sábado
horario_fim = ["8:00:00", "9:00:00", "10:00:00", "11:00:00",
                  "12:00:00", "13:00:00", "14:00:00", "15:00:00",
                  "16:00:00", "17:00:00", "18:00:00", "19:00:00",
                  "19:20:00", "20:10:00", "21:00:00", "21:50:00"] # Horários de fim possíveis


def binToHex(bits):
    return hex(int(bits,2))[2:].upper()         # Converte string binária para hexadecimal

def salvar_arquivo(dia, sala, hex_str):         # Salva a string hexadecimal em um arquivo
    caminho = f"api/{dia}/{sala}/HorHex.txt"
    with open(caminho, "w") as f:
        f.write(hex_str)


for dia in dias:                                # Cria diretórios para cada dia e sala
    for sala in salas:
        os.makedirs(f"api/{dia}/{sala}/", exist_ok=True)


for sala in salas:                              # Gera os arquivos HorHex.txt para cada sala e dia
    for dia in dias:
        binario = ""
        for horaf in horario_fim:
            sql = F"""
            SELECT 
               count(*)
            FROM core_horarioturma LEFT JOIN core_sala ON core_horarioturma.sala_id = core_sala.id
            WHERE core_horarioturma.hora_fim IN ('{horaf}') AND core_horarioturma.dia_semana IN ('{dia}') AND core_sala.nome IN ('{sala}');
            """
            cursor.execute(sql)
            dados = cursor.fetchall()
            ocupado = dados[0][0] > 0  # Verifica se a sala está ocupada nesse horário

            if ocupado:
                binario += "1"
                print(f"Sala {sala} ocupada no dia {dia} às {horaf}")
            else:
                binario += "0"
        hexadecimal = binToHex(binario)
        salvar_arquivo(dia, sala, hexadecimal)

print("Arquivos HorHex.txt gerados com sucesso.", salas)
conn.close()