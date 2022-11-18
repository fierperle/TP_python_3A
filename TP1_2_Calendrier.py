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
