#! /usr/bin/env python

def encoding(rna):
    base = ('U', 'C', 'A', 'G')                     
    amino_acids = 'FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG'

    codontable = {}
    for a in base:
        for b in base:
            for c in base:
                codontable[a+b+c] = 0      
            
    codondict = dict(zip(codontable, amino_acids))

    codonfrag = []
    for i in range(0, len(rna),3):
        codonfrag += [rna[i:i+3]]
    
    protein = ""
    for codon in codonfrag:
        protein += codondict[codon]
    return protein

protein = encoding("AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA")
print(protein)
    


        



