import math

inputFile = open("input.txt","r")
inputFileLines = inputFile.read()

outputFile = open("output.txt", "w")

inputKey = input("Input key: ").lower()
inputMode = input("Input Mode (E/D): ")

default_letters = "abcdefghijklmnopqrstuvwxyz{}()[]1234567890*=-+,@"
default_letters_indexes = dict([(value[1],value[0]) for value in enumerate(default_letters)])

default_letter_substitution = {
    0: "}w8hyk,+5dt2c-pj6aixv]nbq31(*u4m79e)@lro[f{zs0=g",
    1: "1oervz-s{4w)tkj*(=2an}@[3m0h+9qlyiufcgp67d58,bx]",
    2: "2,-gnx7a{+]@3mw5ocvf1}(usqhzy6[9)bl4t=8pek*rdji0",
    3: "=(j1x4tlp+8qvo0g2kn5}r7e]c*aib,@h[y3z-6md9{wufs)",
    4: "u]j95r0)dpbk+-x8ca}w6q=3(i@tv*yn7s4{m[zfle,go2h1",
    5: "*cuxwv(snmtpdya1o+78g45q3)6f,ekhbrl2z-@{0]}=j[i9",
    6: "yw,q1u[]bpzt5(a}3940f@nhex=)ijd8vrk62g-mol7s+c{*",
    7: "xndzgr[h}-wlk5v3o9ejq06*ft,u1=24+p]8i)(ya7bcm{s@",
    8: "h,g]78lye95z*omx{dfn}tv2-)+aw6qc4[jipk10(@=r3bsu",
    9: "il*5p4}{hj]qfbny+wsraeg-0,7vxz3[dk(1m9=82ut6)o@c",
    10: "+-1{[mo*k0te5rpah432dqyw),cbunl9xgzv@(]78s}6jfi=",
    11: ")2]=alwxkj,35b1upe@o+y(n07v{zqdtgi9}-4cf6rmh*s8[",
    12: "+r5)ahm8j*tolqw64ce}7=zk9nixsu31b[f@](-{0gyvd2p,",
    13: "c}(5pqv*t2iw9fysz=e-m6l0x4,r]1k{o[hb)7dnag3u8+j@",
    14: "{3[]4n86sbu,evlqwf@yt+(r}1)azcd=7jm9*okgix50ph2-",
    15: "t47b3hn+i2{c0k95mu1gwxzqe@y-r]jp=,(dsal[)f}86v*o",
    16: "tu4=rmz83i+}2hypvqd1naew6k-c(ox90]7[g,f@s5lb{*j)",
    17: "8y9xv0f4*rbd([ot}]pizem1+{g,s6j2a)lq-=3w@cu7nkh5",
    18: "6b*(1n9t-frj+luvam=3[]pq)c7h,@g52wzoy4d8k{ix}e0s",
    19: "1}chjvt2epo6q+[8sriu]kbm4w90gnz)@(7=,*-{f3ld5xay"
}

def encryptJ(message, key):
    message = message.replace(" ", "@")
    sortedColumnDictionary = key.split()
    keyLength = len(sortedColumnDictionary)
    totalRows = math.ceil(len(message) / keyLength)
    outputMessage = ""

    # Looping over each column
    for columnIndex in range(len(sortedColumnDictionary)):
        currentColumnElementIndex = int(sortedColumnDictionary[columnIndex]) # holds the value of each column element
        iteration = 0

        # Getting each column rows value. Plaintext isn't split up evenly, "padding" has to be added
        while (iteration < totalRows):
            if (currentColumnElementIndex < len(message)):

                if (message[currentColumnElementIndex] in default_letters):
                    currentChar = message[currentColumnElementIndex]
                    currentCharIndex = default_letters_indexes[currentChar]
                    updatedChar = default_letter_substitution[iteration % 20][currentCharIndex]

                    outputMessage += updatedChar

                else:
                    outputMessage += message[currentColumnElementIndex]

            else:
                outputMessage += " "

            currentColumnElementIndex += keyLength
            iteration += 1

    outputFile.write(outputMessage)

def decryptMessage(key, message):
    numOfColumns = int(math.ceil(len(message) / float(key)))
    numOfRows = key

    numOfShadedBoxes = (numOfColumns * numOfRows) - len(message)

    plaintext = [''] * numOfColumns

    column = 0
    row = 0

    for symbol in message:
        if (symbol in default_letters):
            currentSymbolIndex = default_letter_substitution[column % 20].find(symbol)
            updatedSymbol = default_letters[currentSymbolIndex]

            plaintext[column] += updatedSymbol
        else:
            plaintext[column] += symbol

        column += 1

        if (column == numOfColumns) or (column == numOfColumns - 1 and row >= numOfRows - numOfShadedBoxes):
            column = 0
            row += 1

    outputFile.write(''.join(plaintext).replace("@", " "))


#encryptJ(inputFileLines, "1 2 3 4")
#decryptMessage(4, inputFileLines)

inputFile.close()
outputFile.close()
