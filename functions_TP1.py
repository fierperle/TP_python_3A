""" TP1 de dévelopement en python du 18/11/2022 """
# la partie 1 n'est qu'un préambule
"""
partie 2 : la validité des dates
"""
# fonction pour l'année bisextile
def is_leap_year(year: int):
    return ((year % 100 != 0) and (year %4 ==0)) or (year % 400 == 0)

# fonction qui donne le nombre de jours dans un mois
def count_days( year :int, month :int):
    if (0 <= month <= 12):
        if (month in [1,3,5,7,8,10,12]):
            return 31
        elif(month == 2):
            return 29 if (is_leap_year(year)) else 28
        else:
            return 30
    else:
        return 0

#fonction devérification de validité de la date
def is_date_valide(year :int, month :int, day :int):
    return (day <= count_days(year, month))

#fonction d'entrée de date par input + vérification
def inputDate():
    isok = False
    while not isok:
        userInput = input("Input a date : (format Day/Month/Year ")
        LstParam = userInput.split("/")
        if (len(LstParam) == 3):
            okParam = 0
            for index,val in enumerate(LstParam) :
                LstParam[index] = val.strip()
                try:
                    LstParam[index] = int(val)
                    okParam += 1
                except:
                    print(LstParam[index],"is not a numbers")
                    break
            if okParam == 3:
                isok = True

    if (is_date_valide(LstParam[2],LstParam[1],LstParam[0])):
        print(f"The date {LstParam[0]}/{LstParam[1]}/{LstParam[2]} is valide")
    else:
        print("Invalide Date")

"""
partie 3 : les impots
"""
def calcImpot():
    incomes = int(input("Input your incomes : "))

    total = 0
    partitions = [[160336,0.45],[74545,0.41],[26070,0.30],[10225,0.11]]
    for splits in partitions:
        if incomes > splits[0]:
            total += (incomes - splits[0] - 1) * splits[1]
        incomes = splits[0]

    print(total)

"""
partie 4 : produit de matrices
"""
#format : liste de ligne
def matrixMultiplication(matA,matB):
    if len(matA[0]) == len(matB):
        #taille de la matrice de sortie
        height = len(matA)
        width = len(matB[0])
        #pour les calcues
        calcSize = len(matB)

        finalMatrix = []
        for i in range(height):
            lstLigne =[]
            for j in range(width):
                a_ij = 0
                for k in range (calcSize):
                    a_ij += matA[i][k] * matB[k][j]

                lstLigne.append(a_ij)
            finalMatrix.append(lstLigne)
        return finalMatrix

def printMatrix(matrix):
    print("Matrix : ")
    for line in matrix:
        strLine = "|"
        for val in line:
            strLine += str(val)+" "
        strLine = strLine[:-1] + "|"
        print(strLine)

"""
partie 5 : les Tours de Hanoï
"""
#les tours sont des listes (le dernier est en haut)
def move(towerFrom, towerTo):
    print("move")
    print("  origine",towerFrom,towerTo)
    towerTo.append(towerFrom[-1])
    towerFrom.pop()
    print("  end",towerFrom,towerTo)

#targeted tower : 2
def solveHanoi(tower1,tower2,tower3):
    pass
    if len(tower1) > 1:
        tower1,tower2,tower3 = solveHanoi(tower1[:-1],tower3,tower2)
    move(tower1,tower2)
    """
    tower1,tower2,tower3 = solveHanoi(tower1,tower3,tower2)
    """

    return(tower1,tower2,tower3)
    # /!\ does not work /!\
