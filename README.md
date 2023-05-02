# Trabalho Redes de Computadores

Universidade Federal do Ceará - UFC Campus Russas

********************Equipe:******************** 

João Vitor de Arruda Lima - *511061*

Francisco Mikael Monteiro Santiago - *475320*

# Aplicação Cliente-Servidor

A implementação foi em python, com o auxilio das bibliotecas:

- **socket:** que permite a construção da aplicação cliente-servidor, suportando conexões de rede.
- ****************random e string:**************** responsáveis pela aleatorização de números e strings.
- **************timer:************** possibilita o programa “dormir” como proposto no trabalho.

## Servidor

De início, ocorre a importação das bibliotecas e logo em seguida a definição de constantes que determinam o endereço e porta do servidor.

```python
HOST = 'localhost' # Endereço de IP do servidor
PORT = 5000 # porta que o servidor ficará ouvindo
```

Depois é criado um objeto de socket utilizando a biblioteca socket que leva dois parâmetros:

- **socket.AF_INET:** determina que o endereço do IP é um IPV4;
- **socket.SOCK_STREAM:** determina que o tipo de socket é um TCP

Definido o socket, associa-se o endereço IP e porta anteriormente definidos ao socket por meio da função **s.bind()**, para por fim começar a escutar as conexões de entrada através do **s.listen()**

```python
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Define o socket
s.bind((HOST, PORT)) # Associa o socket a um endereço IP e porta
s.listen() # Começa a escutar conexões de entrada
```

Agora começa o tratamento das conexões recebidas, como o servidor continuará rodando para mais de uma requisição/conexão, existe um laço While que só será parado quando não for mais necessário o servidor.

Para o tratamento, começamos aceitando a conexão do cliente pelo ********************s.accept()********************, e extraindo disso:

- **conn:** que representa a conexão que aconteceu;
- **************ender:************** que representa o endereço da máquina do cliente.

Se a conexão for estabelecida com sucesso, é extraído os dados enviados pelo cliente através da **********************************conn.recv(1024)**********************************, 1024 seria o tamanho do buffer.

```python
conn, ender = s.accept() # aceita a conexão
data = conn.recv(1024) # recebe os dados do cliente
```

A partir de então, o dado recebido é decodificado, transformado em inteiro, avaliado o número de digitos para então avaliar a condição:

- Se o número de digitos for maior do que 10, é gerado uma string aleatória de mesmo tamanho, que será enviada como resposta ao cliente.

```python
if numDigitos > 10:
    caracteres = string.ascii_lowercase + string.digits # Estabelece os caracteres
																												# possíveis na string aleatória
    # criar string aleatória
    stringAleatoria = ''.join(random.choice(caracteres)
                      for _ in range(numDigitos))
    resposta = stringAleatoria 
```

- Senão, verifica se o número é IMPAR ou PAR, enviando o respectivo resultado ao cliente.

Para enviar o resultado ao cliente, é usado conn.sendall(), passando como argumento o resultado codificado.

E então a conexão é fechada pelo método conn.close()

## Cliente

O cliente começa definindo as constantes HOST e PORT que guardarão respectivamente o endereço IP e a porta do servidor que receberá as requisições.

Como serão realizadas várias conexões uma após a outra, inicia-se um laço While que só será parado quando ocorrer um erro ao receber os dados de volta do servidor.

O cliente, assim como o servidor, começa criando um socket TCP/IP e conectando-se ao endereço do servidor, que foi endereçado pelas constantes HOST e PORT, por meio do método ************************s.connect().************************

```python
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Cria-se um socket IPV4 e TCP
s.connect((HOST, PORT)) # Connecta-se ao servidor
```

Em seguida, para aleatorizar de forma a conseguir diferentes resultados no final, aleatoriza-se, por meio do método **randint()** um número aleatório entre 1 e 30, que determinará o número de casas que o próximo número gerado pode ter e armazenado na variável ******************expoente.******************

Após isso, gera-se um novo número que estará no intervalo de 10 elevado ao expoente anterior à 10 elevado ao expoente conquistado anteriormente.

Esse número é transformado em string para que possa ser codificado e enviado ao servidor.

```python
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
expoente = random.randint(1, 30)  # determina a quantidade de digitos

# gera número aleatorio
num = random.randint(10**(expoente-1), 10**expoente)
numString = str(num) # Transforma em string

s.sendall(numString.encode()) # Codifica e envia ao servidor
```

Com isso, é armazenado a resposta do servidor na variável **********data********** através do método s.recv(1024), onde 1024 é o tamanho do buffer.

Então, é imprimido na tela o número de digitos do número enviado ao servidor, o número enviado e a resposta recebida.

```python
data = s.recv(1024) # Guarda a resposta

print('Numero de digitos: ', expoente)
print('Numero gerado: ', num)
print('Mensagem ecoada:', data.decode())
```