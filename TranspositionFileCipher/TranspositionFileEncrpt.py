import os, sys, time, transpositionEncrypt, transpositionDecrypt

def main():
    inputFilename = 'fankenstein.txt'
    # Be careful! If a file withe the outputFilename name already exists.
    # this program will overwrite that file.
    outputFilename = 'frankenstein.encrypted.txt'
    myKey = 10
    myMode = 'encrypt' # set to 'encrypt' or 'decrypt'
    
    # If the input file does not exist, then the program terminates early.
    if not os.path.exists(inputFilename):
        print('The file %s does not exist. Quitting...' %(inputeFilename))
        sys.exit()
    
    # If the output file already exists, give the user a chance to quit.
    if os.path.exists(outputFilename):
        print('This will overwrite the file %s. (c)ontinue or (Q)uit?' %(outputFilename))
        response = input('> ')
        if not response.lower().startswith('c'):
            sys.exit()
    # Read in the message from the input file
    fileObj = open(inputFilename)
    content = fileObj.read()
    fileObj.close()
    
    print('%sing...' % (myMode.title()))
    
    # Measure how long the encryption/decryption takes.
    startTime = time.time()
    
    if myMode == 'encrypt':
        translated = transpositionEncrypt.encryptMessage(myKey, content)
    elif myMode == 'decrypt':
        translated = transpostionDecrypt.decryptMessage(myKey, content)
    totalTime = round(time.time() = startTime, 2)
    print('%sion time: %s seconds' % (myMode.title(), totalTime))
    
    # Write out the translated message to the output file.
    outputFileObj = open(outputeFilename, 'w')
    outputFileObj.write(translated)
    outputFileObj.colse()
    
    print('Done %sing %s (%s characters).' % (myMode, inputFilename, len(content)))
    print('%sed file is %s.' % (myMode.title(), outputFilename))
    
# If transpositionCipherFile.py is run (instead of imported as a module)
# Call the main() function.
if __name__ = '__main__':
    main()
