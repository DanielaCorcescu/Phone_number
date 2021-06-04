# Creati un app ce va cere numarul de telfon
# (numere arbice)
# si va printa pe ecran numarul cu caractere
# 1 , 2, 3
# unu , doi , trei
dictionar = {
    0: "zero",
    1: "unu",
    2: "doi",
    3: "trei",
    4: "patru",
    5: "cinci",
    6: "sase",
    7: "sapte",
    8: "opt",
    9: "noua"
}
numar = input("Introduce-ti numarul d-voastra de telefon -> ")
for cifra in str(numar):
 print(dictionar[int(cifra)])