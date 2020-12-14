  
# Reverse Cipher

message = input("Enter Message to Encrypt or Decrypt: ")
translated = ''

i = len(message) - 1

while i >=0:
    translated += message[i]
    i -= 1

print(translated)
