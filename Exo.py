#1- Nan yon chenn karaktè, mete tout karaktè yo an miniskil.
teks1 = "MANJE MANGO NOU."
print(teks1)
print("Rezilta 1 : ", teks1.lower())


# 2-Nan yon chenn karaktè, koupe chenn nan tout kote ki gen espas. Epi afiche yon lis ki gen chak eleman yo. Ekzanp:
teks2 = "Challenge l'an nan Code9Class toujou rete solid"
print(teks2)
print("Rezilta 2 : ",teks2.split(" "))


# 3-Nan yon chenn karaktè, mete tout premye lèt chak mo an majiskil.
libele3 = "La terre est ronde pas comme une boule "
print(libele3)
print("Rezilta3 : ",libele3.title())


# 4-Nan yon chenn karaktè, rekipere premye lèt chak mo. Epi afiche yon nouvo chenn ak tout inisyal sa yo.
libele_4= "La famille est la plus petite cellule complète dans une société"
tab_let = []
for let in libele_4.split(" "):
    tab_let.append(let[:1])
print(libele_4)
print("Rezilta 4 : ",tab_let)


# 5-Ranplase tout karaktè "a" ki nan yon chenn pa "@"
chenn_a = "Aah ti papa ! ou pa ta monte pyebwa a ak sapat ou"
print(chenn_a)
print(chenn_a.replace("a","@"))


# 6-Mete yon chenn karaktè devan dèyè, answit mete l an majiskil.:
print("Lub se yon kotch solid")
ch = (" Lub se yon kotch solid")[::-1].upper()
print("Rezilta 6 : ", ch)


#7- Afiche endeks premye karaktè "a" ki nan yon chenn. Ekzanp:
# "Ayiti kapab avanse" 7
egzchenn = "Ayiti kapab avanse"
i=0
print(egzchenn )
egzchenn = egzchenn.replace(" ","")
for a in egzchenn:
    i+=1
    if (a == "a"):
        print("pozisyon Let 'a' a se :",i)
        break


# 8-Afiche total tout endeks karaktè "a" ki nan yon chenn (Kit se a majiskil oubyen miniskil). Ekzanp:
chenn_tot = "Ayiti kapab avanse sin mete men nan men"
i = somasyon = 0
print(chenn_tot)
for a in chenn_tot:

    if (a == "a" or a == "A"):
        somasyon+=i
    i += 1
print("Somme endeks 'a' ak 'A' nan chenn nan se ",somasyon)


# 9-Kreye yon lis ki gen endeks tout karaktè "a" ki nan yon chenn (Sèlman a miniskil). Ekzanp:
# "Ayiti kapab avanse" [7,9,12,14]
lis_index = []
chen_inisyal    ="map travay okay"
var="a"
j = 0
for k in chen_inisyal:
    if k ==var:
        lis_index.append(j)
    j= j+1
print(lis_index)

# 10- Retire tout espas ki nan yon chenn, epi kole chenn sa ak kantite karaktè li genyen (Pa kontwole espas yo).
chenn_kar="map kouri poum ka gen bel fom"
for k in chenn_kar:
    chenn_kar=chenn_kar.replace(" ","")

print(chenn_kar)
print(len(chenn_kar))
