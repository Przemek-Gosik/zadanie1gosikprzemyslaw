def wyrazciagu(n):
    if n==0:
        return 1
    elif n==1:
        return 3
    else:
        return (wyrazciagu(n-1)-wyrazciagu(n-2))+1
def wypelnienie(dlugosc,tab):
    i=0
    while i<dlugosc:
        tab[i]=wyrazciagu(i)
        i+=1
    return tab
def sortowanie(dlugosc,tab):
    i=0
    j=dlugosc-1
    while i<j:
        while tab[i]>0 and i<j:
            i+=1
        while tab[j]<=0 and i<j:
            j-=1
        if i<j:
            tab[i],tab[j]=tab[j],tab[i]
    return tab
n=-1
while n<0:
    n=int(input("Podaj nr wyrazu ciagu: "))
print("Wartosc wyrazu ciagu nr "+str(n)+" wynosi:"+str(wyrazciagu(n)))
dlugosc=0
while dlugosc<1:
    dlugosc=int(input("Podaj dlugosc tablicy"))
tab=[0]*dlugosc
tab=wypelnienie(dlugosc,tab)
print(tab)
tab=sortowanie(dlugosc,tab)
print(tab)
