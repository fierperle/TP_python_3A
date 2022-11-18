import functions_TP1 as TP1

"""selection de l"exercice"""
exercice = 3

if exercice == 1:
    print("--- Exercice 2 : Calendrier ---")
    TP1.inputDate()
    print("")

elif exercice == 2:
    print("--- Exercice 3 : les impots ---")
    TP1.calcImpot()
    print("")

elif exercice == 3:
    print("--- Exercice 4 : les matrices ---")
    A = [[1,0,0],[0,1,0],[0,0,1]]
    B = [[1,4,3],[2,4,0],[6,8,7]]

    C = TP1.matrixMultiplication(A,B)
    TP1.printMatrix(C)
