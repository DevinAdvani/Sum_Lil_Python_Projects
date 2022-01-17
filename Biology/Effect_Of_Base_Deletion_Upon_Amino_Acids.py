#https://en.wikipedia.org/wiki/DNA_and_RNA_codon_tables
#Standard_DNA_codon_table
CTAA = {
'GCT':'Ala  ',
'GCC':'Ala  ',
'GCA':'Ala  ',
'GCG':'Ala  ',

'CGT':'Arg  ',
'CGC':'Arg  ',
'CGA':'Arg  ',
'CGG':'Arg  ',
'AGA':'Arg  ',
'AGG':'Arg  ',

'AAT':'Asn  ',
'AAC':'Asn  ',

'GAT':'Asp  ',
'GAC':'Asp  ',

'AAT':'Asn/p', #Asn or Asp
'AAC':'Asn/p',
'GAT':'Asn/p',
'GAC':'Asn/p',

'TGT':'Cys  ',
'TGC':'Cys  ',

'CAA':'Gln  ',
'CAG':'Gln  ',

'GAA':'Glu  ',
'GAG':'Glu  ',

'CAA':'Gln/u', #Gln or Glu
'CAG':'Gln/u',
'GAA':'Gln/u',
'GAG':'Gln/u',

'GGT':'Gly  ',
'GGC':'Gly  ',
'GGA':'Gly  ',
'GGG':'Gly  ',

'CAT':'His  ',
'CAC':'His  ',

'ATG':'START', #START/Met

'ATT':'Ile  ',
'ATC':'Ile  ',
'ATA':'Ile  ',

'CTT':'Leu  ',
'CTC':'Leu  ',
'CTA':'Leu  ',
'CTG':'Leu  ',
'TTA':'Leu  ',
'TTG':'Leu  ',

'AAA':'Lys  ',
'AAG':'Lys  ',

'TTT':'Phe  ',
'TTC':'Phe  ',

'CCT':'Pro  ',
'CCC':'Pro  ',
'CCA':'Pro  ',
'CCG':'Pro  ',

'TCT':'Ser  ',
'TCC':'Ser  ',
'TCA':'Ser  ',
'TCG':'Ser  ',
'AGT':'Ser  ',
'AGC':'Ser  ',

'ACT':'Thr  ',
'ACC':'Thr  ',
'ACA':'Thr  ',
'ACG':'Thr  ',

'TGG':'Trp  ',

'TAT':'Tyr  ',
'TAC':'Tyr  ',

'GTT':'Val  ',
'GTC':'Val  ',
'GTA':'Val  ',
'GTG':'Val  ',

'TAA':'STOP ', #STOP
'TGA':'STOP ',
'TAG':'STOP ',






'AA':'AA',
'TA':'TA',
'CA':'CA',
'GA':'GA',

'AT':'AT',
'TT':'TT',
'CT':'CT',
'GT':'GT',

'AC':'AC',
'TC':'TC',
'CC':'CC',
'GC':'GC',

'AG':'AG',
'TG':'TG',
'CG':'CG',
'GG':'GG',






'A':'A',
'T':'T',
'C':'C',
'G':'G',
}

#Need to round down to a multiple of three for below definition
def rdt_three(z):
    return z - (z%3)

#DNA to Amino Acid
def DNAtAA(DNA):
    #Function doesn't work if not a perfect multiple of three, so need some changes
    if len(DNA) % 3 == 0:
        #Split into codons
        codons = []
        for i in range(0,len(DNA),3):
            codons.append(DNA[i:i+3])
        #Need to turn codons into amino acids
        for i in range(0,len(codons)):
            codons[i] = CTAA[codons[i]]
        return codons
    else:
        #Split into codons
        codons = []
        for i in range(0,rdt_three(len(DNA)),3):
            codons.append(DNA[i:i+3])
        codons.append(DNA[rdt_three(len(DNA)):(len(DNA))])
        #Need to turn codons into amino acids
        for i in range(0,len(codons)):
            codons[i] = CTAA[codons[i]]
        return codons



code = input("ENTER YOUR CODE ALL CAPS: ")
print(DNAtAA(code))
reference = ''
d_code = ''
for i in range(1,len(code)+1):
    reference += str(i)
if len(code) < 10:
    d_code = code
elif len(code) < 100:
    d_code += code[0:10]
    for i in range(10,len(code)):
       d_code += ' '
       d_code += code[i]
elif len(code) < 1000:
    d_code += code[0:10]
    for i in range(10,100):
        d_code += ' '
        d_code += code[i]
    for i in range (100, len(code)):
        d_code += '  '
        d_code += code[i]
print(reference)
print(d_code)
location = input("WHICH BASE NUMBER WOULD YOU LIKE TO DELETE: ")
n_code = code[0:int(location)-1] + code[int(location):len(code)]
print(f'''
ORIGINAL CODE:        {code}
NEW CODE:             {n_code}
ORIGINAL AMINO ACIDS: {DNAtAA(code)}
NEW AMINO ACIDS:      {DNAtAA(n_code)}''')

while True:
    var = 100
