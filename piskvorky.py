from random import randrange

def tah (pole):
    hodnota = input('Na jaké pole chceš hrát? ')
    try:
        hodnota=int(hodnota)
    except ValueError:
        print ('To nebylo cislo!')
        tah(pole)
    if hodnota > 0 and hodnota < 21:
        pozice = pole[hodnota]        
    else:
        tah(pole)
    while True:
        if 'x' == pozice or 'o' == pozice:
            (tah(pole))            
        else:
            zacatek = pole[:hodnota]
            konec = pole[hodnota + 1:]
            pole = zacatek + ('x') + konec
            print (pole)         
        if 'xxxx' not in pole:
            (tahp(pole))                 
        if 'xxxx' in pole:
            print ('Hráč vyhrál!')
            break            
    quit()        
        

def tahp (pole):
    cislo = randrange(1,21)            
    pozicep = pole[cislo]
    
    while True:
        if 'x' == pozicep or 'o' == pozicep:
            tahp(pole)
        else:
            zacatek = pole[:cislo]
            konec = pole[cislo + 1:]
            pole = zacatek + ('o') + konec
            print ('Počítač jede na pole: ',cislo)
            print (pole)
        if '-' not in pole:
            print('Konec hry!')
            break
        if 'oooo' not in pole:
            tah(pole)               
        if 'oooo' in pole:
            print ('Počítač vyhrál!')
            break
        
    quit()        

def piskvorky1d():
    pole = ('(--------------------)')
    print (pole)
    print ('Pravidla 1D piškovrek: \n1) Piš čísla od 1 do 20\n2) Kdo získá jako první 4 znaky vyhrává!')
    tah(pole)

piskvorky1d()




