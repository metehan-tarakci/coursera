dna = ["ATAGTCTCTTATACCCGTGCAGTTG" ,"TCATAGTCCGTAACGATGGTCTCTT" ,"GATCGGCGAAGGGAAGAGAGCTATT" ,"GACTTAAAAAAAATTGTCACCTATT" ,"CAGTACACGAACCCGCTCTTGTCTC", "CTCGATAATACTGTTCTACCGGCAA"]
k = 5
d = 1

def hamming_distance(seq1, seq2):
    count = 0
    for i in range(len(seq1)):
        if seq1[i] != seq2[i]:
            count += 1
    return count

def neighbors(pattern, d):
    if d == 0:
        return {pattern}
    if len(pattern) == 1:
        return {"A", "C", "G", "T"}

    neighborhood = set()
    suffix = pattern[1:]
    first_symbol = pattern[0]

    suffix_neighbors = neighbors(suffix, d)

    for text in suffix_neighbors:
        if hamming_distance(suffix, text) < d:
            for x in "ACGT":
                neighborhood.add(x + text)
        else:
            neighborhood.add(first_symbol + text)

    return neighborhood

def appears_with_mismatches(pattern, text, d):
    for i in range(len(text) - len(pattern) + 1):
        if hamming_distance(pattern, text[i:i+len(pattern)]) <= d:
            return True
    return False

def motif_enumeration(dna, k, d):
    kmers = set()

    for sequence in dna:
        for i in range(len(sequence) - k + 1):
            kmer = sequence[i:i+k]

            for candidate in neighbors(kmer, d):
                found_in_all = True
                for other_sequence in dna:
                    if not appears_with_mismatches(candidate, other_sequence, d):
                        found_in_all = False
                        break
                if found_in_all:
                    kmers.add(candidate)

    return kmers

result = motif_enumeration(dna, k, d)
print(" ".join(result))