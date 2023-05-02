import socket
import random
from time import sleep

HOST = '127.0.0.1' 
PORT = 5000


while (True):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Cria-se um socket IPV4 e TCP
    s.connect((HOST, PORT)) # Connecta-se ao servidor
    expoente = random.randint(1, 30)  # determina a quantidade de digitos

    # gera nuemro aleatorio com ate 30 digitos
    num = random.randint(10**(expoente-1), 10**expoente)
    numString = str(num) # Transforma em string

    s.sendall(numString.encode()) # Codifica e envia ao servidor
    data = s.recv(1024) # Guarda a resposta
    if not data:
        s.close()
        break
    print('Numero de digitos: ', expoente)
    print('Numero gerado: ', num)
    print('Mensagem ecoada:', data.decode())
    print('')
    s.close()
    sleep(10)
