import os
import pyaes #biblioteca de criptografia

## ABRINDO O ARQUIVO CRIPTOGRAFADO

file_name = 'teste.txt.ransowaretroll'
file = open(file_name, 'rb')
file_data = file.read()
file.close()

## CHAVE DE DESCRIPTOGRAFIA

key = b'testeransomwares' 
aes = pyaes.AESModeOfOperationCTR(key)
decrypt_data = aes.decrypt(file_data)

## REMOVENDO O ARQUIVO CRIPTOGRAFADO

os.remove(file_name)

## CRIANDO UM NOVO ARQUIVO DESCRIPTOGRAFADO

new_file = 'teste.txt'
new_file = open(f'{new_file}','wb')
new_file.write(decrypt_data)
new_file.close

