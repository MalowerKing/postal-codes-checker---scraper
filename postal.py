import pandas as pd

#Import Data
ulice = pd.read_csv(r"ULIC_Adresowy_2023-07-13.csv", sep=";")
miejscowosc = pd.read_csv(r"SIMC_Adresowy_2023-07-13.csv", sep=";")
kody = pd.read_csv(r"kody.csv", sep=";")
terc = pd.read_csv(r"TERC_Adresowy_2023-07-13.csv", sep=";")

#First try finding
def firstTry(name: str, nameU: str):

    def check(part,i):
        if part == check[i]:

    firstTry = kody[kody.MIEJSCOWOŚĆ == name]
    if len(firstTry) == 1: return firstTry["KOD POCZTOWY"]
    else:
        check = nameU.split()
        
        print(len(check))
        for lane in firstTry.ADRES.str.split():
            # print(part)
            count = 0
            for part in lane:
                
                    i +=
                # print(check[i])
                    if part == check[i]:
                        count += 1
            if count == len(check)-1: print
            # if count == len(check):
            #     return 1
            


def findingSettlment(settlement):

    def findPowWoj(name, i):
        woj_check = miejscowosc_analiza.iloc[i].WOJ
        pow_check = miejscowosc_analiza.iloc[i].POW

    powiaty = terc[terc.GMI.isnull() ]
    wojewodztwa = terc[terc.POW.isnull()& terc.NAZWA_DOD == 'województwo']

    for i in range(0, ):

        print(pow_check, woj_check)
        print("Powiat "+powiaty[(powiaty.POW == pow_check) & (powiaty.WOJ == woj_check)].NAZWA)

print(firstTry('Warszawa', 'ul. Bagno'))







