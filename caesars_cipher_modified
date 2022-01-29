# Caesar's cipher implementation with all ascii values
asciiValues = ''.join(chr(i) for i in range(128))

inputMessage = input("Input message: ")
inputKey = int(input("Input key (0-127): "))
inputMode = input("Input Mode (E/D): ")

def runCaesarsCipher(message, key, mode):
    outputMessage = ""

    for index, currentMessageChar in enumerate(inputMessage):
        if (currentMessageChar in asciiValues):
            currentMessageCharAsciiIndex = asciiValues.index(currentMessageChar)
            currentMessageCharUpdatedIndex = (currentMessageCharAsciiIndex + inputKey) % 127 if (inputMode == "D") else (currentMessageCharAsciiIndex - inputKey) % 127
            resultativeAsciiValue = asciiValues[currentMessageCharUpdatedIndex]
            outputMessage += resultativeAsciiValue

    return outputMessage

result = runCaesarsCipher(inputMessage, inputKey, inputMode)
