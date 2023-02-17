# Přiřazeni proměné
c_inst = ''
a_inst = ''
comp = ''
dest = ''
jump = ''
a='111'
n= '0'
soubor = input()
# Otevření assem souboru

f2 = open('{}.hack'.format(soubor), 'w')
f1 = open('{}.asm'.format(soubor), 'r')
count = 0

while True:
    count += 1
    snumber = f1.readline()
    if not snumber:
        break

    # A instukce
    if '@' in snumber:
        if '@' in snumber:
            a_inst = (snumber[1:])
        if '@R' in snumber:
            a_inst = (snumber[2:])
        if '@KBD' in snumber:
            a_inst = ('24576')
        if '@SCREEN' in snumber:
            a_inst = ('16384')
        if '@SP' in snumber:
            a_inst = ('0')
        if '@LCL' in snumber:
            a_inst = ('1')
        if '@ARG' in snumber:
            a_inst = ('2')
        if '@THIS' in snumber:
            a_inst = ('3')
        if '@THAT' in snumber:
            a_inst = ('4')
        a_inst = int(a_inst)
        a_inst= bin(a_inst+(1<<15))[3:]

    # C instukce
    elif '0' in snumber or '1' in snumber or 'A' in snumber or 'D' in snumber or 'M' in snumber or 'JGT' in snumber or 'JEQ' in snumber or 'JGE' in snumber or 'JLT' in snumber or 'JNE' in snumber or 'JLE' in snumber or 'JMP' in snumber:
        c_inst = snumber

# Comp instrukce
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
    if 'M' in c_inst and not 'M=' in c_inst and not 'JMP' in c_inst:
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
        comp = ('0011111')
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
    if 'D=' in c_inst:
        dest = ('010')
    if 'MD=' in c_inst:
        dest = ('011')
    if 'A=' in c_inst:
        dest = ('100')
    if 'AM=' in c_inst:
        dest = ('101')
    if 'AD=' in c_inst:
        dest = ('110')
    if 'AMD=' in c_inst:
        dest = ('111')
    if 'M=' not in c_inst and 'D=' not in c_inst and 'MD=' not in c_inst and 'A=' not in c_inst and 'AM' not in c_inst and 'AD' not in c_inst and 'AMD' not in c_inst:
        dest = ('000')


    # Jump
    if 'JGT' in c_inst:
        jump=('001')
    if 'JEQ' in c_inst:
        jump=('010')
    if 'JGE' in c_inst:
        jump=('011')
    if 'JLT' in c_inst:
        jump=('100')
    if 'JNE' in c_inst:
        jump=('101')
    if 'JLE' in c_inst:
        jump=('110')
    if 'JMP' in c_inst: 
        jump=('111')
    if 'JGT' not in c_inst and 'JEQ' not in c_inst and 'JGE' not in c_inst and 'JLT' not in c_inst and 'JNE' not in c_inst and 'JLE' not in c_inst and 'JMP' not in c_inst:
        jump=('000')

# Výběr jestli je načtená a nebo c instrukce + zapsání (\n) zapíše na novy rádek
    if c_inst == snumber:
        L=("{}\n".format(a+comp+dest+jump))
    if c_inst != snumber:
        L=("{}\n".format(n+a_inst))
    
    f2.writelines(L)
    
f1.close()
f2.close()