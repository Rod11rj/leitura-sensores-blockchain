import hashlib
import datetime as date
import csv


lista_password = []
usuarios = ['CIAA']
senhas = [2023]


usuario = str(input("Informe seu usuario: ")).upper()


class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()


    def calculate_hash(self):
        sha = hashlib.sha256()
        sha.update(str(self.index).encode('utf-8')+
                   str(self.timestamp).encode('utf-8')+
                   str(self.data).encode('utf-8')+
                   str(self.previous_hash).encode('utf-8'))
        return sha.hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block (0, date.datetime.now(), 'Genesis Block: [data-hora , temperatura]', '0')

    def add_block(self, new_block):
        new_block.previous_hash = self.chain[-1].hash
        new_block.hash = new_block.calculate_hash()
        self.chain.append(new_block)

    def is_valid(self):
        for i in range (1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain [i-1]

            if current_block.hash != current_block.calculate_hash():
                return False
            if current_block.previous_hash != previous_block.calculate_hash():
                return False

        return True

    def imprimir_blocos(self):
        for bloco in self.chain:
            print(f"Bloco: {bloco.index}")
            print(f"Timestamp: {bloco.timestamp}")
            print(f"Dados: {bloco.data}")
            print(f"Hash anterior: {bloco.previous_hash}")
            print(f"Hash: {bloco.hash}")
            print("\n")

for i in range (0, len(usuarios)):
        if usuario == usuarios[i]:
            senha = int(input('Informe sua senha: '))
            if senha == senhas[i]:
                print('Acesso liberado')
                print('=====================')

                my_blockchain_sensor = Blockchain()

                with open("data.csv", "r")  as f:
                    reader = csv.reader(f, delimiter=",")

                    index = 1
                    for row in reader:
                        # Criando um novo bloco
                        data = row[0]

                        new_block = Block(index, date.datetime.now(), row, my_blockchain_sensor.chain[-1].calculate_hash())

                        # Adicionando o novo bloco à blockchain
                        my_blockchain_sensor.add_block(new_block)
                        index += 1

                print(f'blockchain valida? {str(my_blockchain_sensor.is_valid())}\n')

                my_blockchain_sensor.imprimir_blocos()

            else:
                print('Acesso negado')
