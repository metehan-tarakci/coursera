def reverse_complement(DNAStr):
    table=str.maketrans("ATGC","TACG")
    newStr=DNAStr.translate(table)
    return (newStr[::-1])

print(reverse_complement("AAAACCCGGT"))