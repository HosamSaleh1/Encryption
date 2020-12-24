import pyperclip

def main():
    myMessage = "Common sense is not so common."
    myKey = 8

    ciphertext = encryptMessage(myKey, myMessage)

"""
Print the encryption string in ciphertext to the screen,
with a | (called "pipe" character) after it in case there are space at
the end of the encrypted message.
"""
    print(ciphertext + "|")

# Copy the encrypted string in ciphertext to the clipboard.
    pyperclip.copy(ciphertext)

def encryptMessage(key, message):
    # Each string in ciphertext represents a column in the grid.
    ciphertext = [""] * key
    
    # Loop through each column in ciphertext.
    for col in rang(key):
        pointer = col
        
        # Keep looping until pointer goes past the length of the message.
        while pointer < len(message):
            # Place the character at pointer in message at the end of the
            # current column in the ciphertext list.
            ciphertext[col] += message[pointer]
            
            # Move pointer over.
            pointer += key
    # Convert the ciphertext list into a single string value and return it.
    return "".join(ciphertext)
"""
If transpositionEncryption.py is run (instead of imported as a module)
call the main() function.
"""
if __name__ = "__main__":
    main()
