
def calcImpot():
    incomes = int(input("Input your incomes : "))

    total = 0
    partitions = [[160336,0.45],[74545,0.41],[26070,0.30],[10225,0.11]]
    for splits in partitions:
        if incomes > splits[0]:
            total += (incomes - splits[0] - 1) * splits[1]
        incomes = splits[0]

    print(total)
