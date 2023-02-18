# Přiřazeni proměné
n= '0'
soubor = input()

# Slovník pro comp
comp_dict = {'0': '0101010', '1': '0111111', '-1': '0111010', 'D': '0001100', 'A': '0110000', 'M': '1110000', 
             '!D': '0001101', '!A': '0110001', '!M': '1110001', '-D': '0001111', '-A': '0110011', '-M': '1110011', 
             'D+1': '0011111', 'A+1': '0110111', 'M+1': '1110111', 'D-1': '0001110', 'A-1': '0110010', 
             'M-1': '1110010', 'D+A': '0000010', 'D+M': '1000010', 'D-A': '0010011', 'D-M': '1010011', 
             'A-D': '0000111', 'M-D': '1000111', 'D&A': '0000000', 'D&M': '1000000', 'D|A': '0010101', 
             'D|M': '1010101'}
# Slovník pro dest
dest_dict = {'': '000','M': '001', 'D': '010', 'MD': '011', 'A': '100', 'AM': '101', 'AD': '110', 'AMD': '111'}

# Slovník pro jump
jump_dict = {'': '000','JGT': '001', 'JEQ': '010', 'JGE': '011', 'JLT': '100', 'JNE': '101', 'JLE': '110', 'JMP': '111'}

def instrukce(c_inst):
    comp = ""
    dest = ""
    jump = ""
    if ";" in c_inst:
        comp,jump=c_inst.split(";")
    if "=" in c_inst:
        dest,comp=c_inst.split("=")
    comp = comp_dict.get(comp)
    dest = dest_dict.get(dest)
    jump = jump_dict.get(jump)
    return ('111'+comp+dest+jump)

# Otevření assem souboru

f2 = open('{}.hack'.format(soubor), 'w')
f1 = open('{}.asm'.format(soubor), 'r')
count = 0

while True:
    count += 1
    snumber = f1.readline().strip()
    
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

# Výběr jestli je načtená a nebo c instrukce + zapsání (\n) zapíše na novy rádek
    if c_inst == snumber:
        L=((f"{instrukce(c_inst)}\n"))
    if c_inst != snumber:
        L=("{}\n".format(n+a_inst))
    
    f2.writelines(L)

f1.close()
f2.close()