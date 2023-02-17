dest= input
jump = input
if dest == True:
    if dest =='M':
        poloha=('001')
    else:
        poloha=('000') 
elif dest == False:
    poloha = ('000')

    # Skoky
if jump == True:
    if jump =='JGT':
        jump_=('001')
    else:
        jump_=('000')
elif jump == False:
    jump_=('000')
print (poloha)
print (jump_)