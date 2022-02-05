import math

inputMessage = input("Input message: ")
inputKey = int(input("Input key: "))
inputMode = input("Input Mode (E/D): ")

# Clamping key's length to not exceed half the length of input message
inputKey = max(1, min(inputKey, math.floor(len(inputMessage) / 2)))

# Transposition cipher splits plaintext in rows, ciphertext is read from collumns
# Example with plaintext hello world and key 3

# [h e l]      [0 1 2]
# [l o  ]      [3 4 5]
# [w o r]      [6 7 8]
# [l d  ]      [9 10 11]

# Noticable, that we can get each columns members by taking the base index and adding key size to it

def encryptTranspositionCipher(message, key):
    totalRows = math.ceil(len(message) / key)
    outputMessage = ""

    # Looping over each column
    for columnIndex in range(key):
        currentColumnElementIndex = columnIndex # holds the value of each column element
        iteration = 0

        # Getting each column rows value. Plaintext isn't split up evenly, "padding" has to be added
        while (iteration < totalRows):
            if (currentColumnElementIndex < len(message)):
                outputMessage += message[currentColumnElementIndex]
            else:
                outputMessage += " "

            currentColumnElementIndex += key
            iteration += 1

    return outputMessage

def decryptTranspositionCipher(message, key):
    totalRows = math.ceil(len(message) / key)
    outputMessage = ""

    for row in range(totalRows):
        currentRowElementIndex = row
        iterator = 0

        while (iterator < key and currentRowElementIndex < len(message)):
            outputMessage += message[currentRowElementIndex]

            currentRowElementIndex += totalRows
            iterator += 1

    return outputMessage

output = encryptTranspositionCipher(inputMessage, inputKey) if (inputMode == "E") else decryptTranspositionCipher(inputMessage, inputKey)
