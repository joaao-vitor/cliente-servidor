import socket
import random
import string

HOST = 'localhost' # Endereço de IP do servidor
PORT = 5000 # porta que o servidor ficará ouvindo

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Define o socket
s.bind((HOST, PORT)) # Associa o socket a um endereço IP e porta
s.listen() # Começa a escutar conexões de entrada

print('Aguardando conexão de um cliente')

while (True):
    conn, ender = s.accept() # aceita a conexão
    print('Conectado em ', ender) 

    data = conn.recv(1024) # recebe os dados do cliente
    num = int(data.decode())
    numDigitos = len(data.decode())

    resposta = ''
    if numDigitos > 10:
        caracteres = string.ascii_lowercase + string.digits# Estabelece os caracteres possíveis na string aleatória

        # criar string aleatória
        stringAleatoria = ''.join(random.choice(caracteres)
                                  for _ in range(numDigitos))
        resposta = stringAleatoria
    else:
        if num % 2 == 0:
            resposta = 'PAR'
        else:
            resposta = 'IMPAR'
    
    print('Número recebido:', num)
    print('Quantidade de dígitos:', numDigitos)
    print('Resposta a ser enviada:', resposta)
    print('')
    conn.sendall(resposta.encode()) # Envia a resposta codificada
    conn.close()
