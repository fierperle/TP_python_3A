def strTolstInt(string: str, data: dict):
    #convert a sentence to a int list for the automate function tu use
    lstPonctuation = [",",":",";"]

    string = string.replace("."," .").replace("!"," !").replace("?"," ?").replace(","," , ").lower() #cleaning
    lstConv = string.split()

    index = 0
    while index < len(lstConv):
        word = lstConv[index]
        if word in lstPonctuation :
            lstConv.remove(word)
            index -= 1
        else:
            try:
                lstConv[index] = data[word]
            except Exception as e:
                raise "word is not in the data dictionnary"
        index +=1

    return lstConv


def automate(lstIn : list, statData : list) -> int:
    stat = 0
    for word in lstIn:
        stat = statData[stat][word]
    if stat not in [8,9]:
        stat = 8
    return stat
