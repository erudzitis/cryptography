import math

inputMessage = input("Input message: ")
inputKey = input("Input key: ").lower()
inputMode = input("Input Mode (E/D): ")

# Clamping key's length to not exceed half the length of input message
if len(inputKey) > math.floor(len(inputMessage) / 2):
    inputKey = inputKey[:math.floor(len(inputMessage) / 2)]

# Transposition cipher splits plaintext in rows, ciphertext is read from collumns
# Example with plaintext hello world and key 3

# [h e l]      [0 1 2]
# [l o  ]      [3 4 5]
# [w o r]      [6 7 8]
# [l d  ]      [9 10 11]

# Noticable, that we can get each columns members by taking the base index and adding key size to it
# In this modified version, encryption column order depends on the alphabetical order of the letters in the key

# Letters in they key MUST be unique

def encryptTranspositionCipher(message, key):
    keyLength = len(key)
    totalRows = math.ceil(len(message) / keyLength)
    outputMessage = ""

    # Getting column iteration order based on key's character alphabetical ordering
    columnDictionary = {}

    # Creating initial key, value pair (initial column index, numerical value of the letter)
    for i in range(keyLength):
        columnDictionary[i] = ord(key[i]) - 96

    # Sorting dictionary by numerical letter values and retrieving only the keys as a list
    sortedColumnDictionary = list(dict(sorted(columnDictionary.items(), key=lambda item: item[1])))

    # Looping over each column
    for columnIndex in range(len(sortedColumnDictionary)):
        currentColumnElementIndex = sortedColumnDictionary[columnIndex] # holds the value of each column element
        iteration = 0

        # Getting each column rows value. Plaintext isn't split up evenly, "padding" has to be added
        while (iteration < totalRows):
            if (currentColumnElementIndex < len(message)):
                outputMessage += message[currentColumnElementIndex]
            else:
                outputMessage += " "

            currentColumnElementIndex += keyLength
            iteration += 1

    return outputMessage

def decryptTranspositionCipher(message, key):
    keyLength = len(key)
    totalRows = math.ceil(len(message) / keyLength)
    outputMessage = ""

    # Getting column iteration order based on key's character alphabetical ordering
    columnDictionary = {}

    # Creating initial key, value pair (initial column index, numerical value of the letter)
    for i in range(keyLength):
        columnDictionary[i] = ord(key[i]) - 96

    # Sorting dictionary by numerical letter values and retrieving only the keys as a list
    initialSortedColumnDictionary = list(dict(sorted(columnDictionary.items(), key=lambda item: item[1])))

    # Converting (for encryption used) list back to dictionary, this time encryption columns are values.
    targetRowDictionary = {i : initialSortedColumnDictionary[i] for i in range(0, len(initialSortedColumnDictionary))}
    # Sorting dictionary by values, retrieving the keys as sorted rows for decryption
    targetRowDictionarySorted = list(dict(sorted(targetRowDictionary.items(), key=lambda item: item[1])))

    for row in range(totalRows):
        currentRowElementIndex = row
        iterator = 0

        while (iterator < keyLength and currentRowElementIndex < len(message)):
            currentRowElementIndex = row + (totalRows * targetRowDictionarySorted[iterator])
            outputMessage += message[currentRowElementIndex]

            iterator += 1


    return outputMessage
