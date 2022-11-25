import functions_TP2 as TP2

""" ---------------- CONST ---------------------"""
dictionnary = {
"le" : 0, "la" : 0,
"petite" : 1, "petit" : 1, "joli" : 1, "grosse" : 1, "bleu" : 1, "verte" : 1, "blanc" : 1,
"chat" : 2, "souris" : 2,
"mange" : 3, "dort" : 3,"joue" : 3,
"julie" : 4,"jean" : 4, "martin" : 4,
 "." : 5, "!" : 5, "?" : 5}
lstTest = [
    "le joli chat joue.",
    "le ,joli chat ; joue.",
    "la grosse souris verte mange le joli petite chat blanc.",
    "la grosse souris verte mange jean.",
    "Jean joue.",
    "Jean mange Martin.",
    "Jean mange le chat.",
    "la verte souris grosse petit mange le bleu verte chat petite.",
    ".",
    "",
    "le joli chat joue",
    "le joli chat dort.",
    "la souris mange le chat.",
    "souris mange chat"
]
lstExpected = [9,9,9,9,9,9,9,9,8,8,8,9,9,8]
lstStats = [
    [ 1, 8, 8, 8, 4, 8 ],
    [ 8, 1, 2, 8, 8, 8 ],
    [ 8, 2, 8, 3, 8, 8 ],
    [ 5, 8, 8, 8, 7, 9 ],
    [ 8, 8, 8, 3, 8, 8 ],
    [ 8, 5, 6, 8, 8, 8 ],
    [ 8, 6, 8, 8, 8, 9 ],
    [ 8, 8, 8, 8, 8, 9 ],
    [ 8, 8, 8, 8, 8, 8 ]
]

""" ---------------- CODE ---------------------"""
for index,sentence in enumerate(lstTest):
    print("--------------------")
    print(index,": ",sentence)
    lstInt = TP2.strTolstInt(sentence,dictionnary)
    print("lstInt: ",lstInt)
    out = TP2.automate(lstInt,lstStats)
    comp = "unexpected"
    if out == lstExpected[index]:
        comp = "ok"
    print("Out:",out, comp)
