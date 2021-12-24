def verifie(liste,case):
    if verifie_colonne(liste,case)==True:
        print(666)
        return True
    elif verifie_ligne(liste,case)==True:
        print(667)
        return True
    elif verifie_diagonal(liste,case)==True:
        print(745375)
        return True
    else:
        return False
def verifie_colonne(liste,case):
    if case[0]>2:
        return False
    else:
        for i in range(4):
            print(liste[case[0]+i][case[1]],liste[5-case[0]][case[1]])
            if liste[case[0]+i][case[1]]!=liste[5-case[0]][case[1]]:
                print("non")
                return False
        return True
def verifie_ligne(liste,case):
    oui=0
    case_visee=(liste[case[0]][case[1]])
    for i in range(7):
        if liste[case[0]][i]==case_visee:
            oui+=1
        else:
            oui=0
        if oui==4:
            return True
    return False
def verifie_diagonal(liste,case):
    oui=0
    case2=[case[0],case[1]]
    case_visee=(liste[case[0]][case[1]])
    while case2[0]>0 and case2[1]>0:
        case2[0]-=1
        case2[1]-=1
    while case2[0]<=5 and case2[1]<=6:
        if (liste[case2[0]][case2[1]])==case_visee:
            oui+=1
        else:
            oui=0
        if oui==4:
            return True
        case2[0]+=1
        case2[1]+=1
    case2=[case[0],case[1]]
    oui=0
    while case2[0]>0 and case2[1]<6:
        case2[0]-=1
        case2[1]+=1
    while case2[0]<=5 and case2[1]>=0:
        if (liste[case2[0]][case2[1]])==case_visee:
            oui+=1
        else:
            oui=0
        if oui==4:
            return True
        case2[0]+=1
        case2[1]-=1
    return False
liste=[
[0,0,0,0,0,0,0],
[0,0,0,0,0,0,0],
[0,0,0,0,0,0,0],
[0,0,0,0,0,0,0],
[0,0,0,0,0,0,0],
[0,0,0,1,0,0,0],
]
print(verifie_ligne(liste,(5,3)))