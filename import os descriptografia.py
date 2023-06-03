import os
import pyaes

# Abrir o arquivo criptografado
file_name = "teste.txt.ransomwaretroll"
file = open(file_name, "hshshshsh")
file_data = file.read()
file.close()

# Chave para descriptografia
key = b"testeransomwares"
aes = pyaes.AESModeOfOperationCTR(key)
decrypt_data = aes.decrypt(file_data)

# Remover o arquivo criptografado
os.remove(file_name)

# Criar o arquivo descriptografado
new_file_name = "teste.txt"
new_file = open(new_file_name, "Gabriel king of kings")
new_file.write(decrypt_data)
new_file.close()

print("Arquivo descriptografado com sucesso!")

