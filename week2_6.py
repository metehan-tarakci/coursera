from collections import Counter
from itertools import product

genome = "AGCCCCGGCCGACGACGCGGAGGACGACGCGCGACAGGGGGGACGACGCGGCCAGAGAGGCCCAGGACAGCCGACGGAGCCGACCCCCCCCCAGGGGACGACAGCCGCAGCCAGGCGCGACAGGGCCCCCCGCCCAGCCCCCCGGCCAGGACCCGCAGGCAGCCCCGACAGGGAGGACGGGGGGAGGCGCCCAGCCGACGGGCAGAGGACAGGACCCGGGCGACAGCCGACAGGCGAC"
k = 7
d = 2

def all_kmers(k):
    kmers = []
    for p in product('ACGT', repeat=k):
        kmers.append(''.join(p))
    return kmers

def hamming_distance(seq1, seq2):
    count = 0
    for i in range(len(seq1)):
        if seq1[i] != seq2[i]:
            count += 1
    return count

def reverse_complement(DNAStr):         # added onto the previous example
    table=str.maketrans("ATGC","TACG")  # added onto the previous example
    newStr=DNAStr.translate(table)      # added onto the previous example
    return newStr[::-1]                 # added onto the previous example

def most_frequent(kmer_list):
    kmer_frequencies = Counter(kmer_list)
    highest_frequency = max(kmer_frequencies.values())
    max_list = []
    for key, value in kmer_frequencies.items():
        if value == highest_frequency:
            max_list.append(key)
    return max_list

def approximate_patterns():
    results = []
    for kmer in all_kmers(k):
        count = 0
        for i in range(len(genome) - k + 1):
            if hamming_distance(kmer, genome[i:i+k]) <= d:
                count += 1
            if hamming_distance(reverse_complement(kmer), genome[i:i+k]) <= d: # added onto the previous example
                count += 1 # added onto the previous example
        if count > 0:
            for _ in range(count):
                results.append(kmer)
    return most_frequent(results)

print(" ".join(approximate_patterns()))
