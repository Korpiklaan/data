# Přiřazeni proměné
snumber = input()
c_inst = ''
a_inst = ''
comp = ''
dest = ''
jump = ''

# A instukce
if '@' in snumber:
    a_inst = int(snumber[1:])
    print(000,bin(a_inst)[2:],sep='')

# C instukce
if '@' not in snumber:
    c_inst = snumber

# instrukce
if c_inst == snumber:
    if '0' in c_inst:
        comp = ('0101010')
    if '1' in c_inst:
        comp = ('0111111')
    if '-1' in c_inst:
        comp = ('0111010')
    if 'D' in c_inst and not 'D=' in c_inst:
        comp = ('0001100')    
    if 'A' in c_inst and not 'A=' in c_inst:
        comp = ('0110000')
    if 'M' in c_inst and not 'M=' in c_inst:
        comp = ('1110000')
    if '!D' in c_inst:
        comp = ('0001101')
    if '!A' in c_inst:
        comp = ('0110001')
    if '!M' in c_inst:
        comp = ('1110001')
    if '-D' in c_inst:
        comp = ('0001111')
    if '-A' in c_inst:
        comp = ('0110011')
    if '-M' in c_inst:
        comp = ('1110011')
    if 'D+1' in c_inst:
        comp = ('1011111')
    if 'A+1' in c_inst:
        comp = ('0110111')
    if 'M+1' in c_inst:
        comp = ('1110111')
    if 'D-1' in c_inst:
        comp = ('0001110')
    if 'A-1' in c_inst:
        comp = ('0110010')
    if 'M-1' in c_inst:
        comp = ('1110010')
    if 'D+A' in c_inst:
        comp = ('0000010')
    if 'D+M' in c_inst:
        comp = ('1000010')
    if 'D-A' in c_inst:
        comp = ('0010011')
    if 'D-M' in c_inst:
        comp = ('1010011')
    if 'A-D' in c_inst:
        comp = ('0000111')
    if 'M-D' in c_inst:
        comp = ('1000111')
    if 'D&A' in c_inst:
        comp = ('0000000')
    if 'D&M' in c_inst:
        comp = ('1000000')    
    if 'D|A' in c_inst:
        comp = ('0010101')
    if 'D|M' in c_inst:
        comp = ('1010101')

    # Destinace
    if 'M=' in c_inst:
        dest = ('001')
    elif 'D=' in c_inst:
        dest = ('010')
    elif 'MD=' in c_inst:
        dest = ('011')
    elif 'A=' in c_inst:
        dest = ('100')
    elif 'AM=' in c_inst:
        dest = ('101')
    elif 'AD=' in c_inst:
        dest = ('110')
    elif 'AMD=' in c_inst:
        dest = ('111')

    else:
        dest = ('000')

    # Jump
    if 'JGT' in c_inst:
        jump=('001')
    elif 'JEQ' in c_inst:
        jump=('010')
    elif 'JGE' in c_inst:
        jump=('011')
    elif 'JLT' in c_inst:
        jump=('100')
    elif 'JNE' in c_inst:
        jump=('101')
    elif 'JLE' in c_inst:
        jump=('110')
    elif 'JMP' in c_inst:
        jump=('111')
    else:
        jump=('000')

    print(111,comp,dest,jump,sep='')

