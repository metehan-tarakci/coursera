from collections import Counter
from itertools import product

genome = "GGGGAATGGGGTCAAGGGGCGAAATTCAATCAAGGGGAATGGGGAATGGGGTCAATCAATCAAAATCGAAATCGAAATTCAAAATAATGGGGGGGGACATTCAATCAAAATACATTCAAACATACATTCAAACATACATTCAATCAACGAACATTCAACGAAATGGGGCGAGGGGGGGGACATACATCGATCAATCAAACATGGGGGGGGACATTCAAGGGGCGACGAGGGGCGACGATCAAGGGGGGGGGGGGACATTCAAAATGGGGACATTCAAAATCGAAATGGGGTCAAACATGGGGGGGGGGGGAATCGATCAAAATCGATCAAACAT"
k = 5
d = 3

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
        if count > 0:
            for _ in range(count):
                results.append(kmer)
    return most_frequent(results)

print(" ".join(approximate_patterns()))

""" 
#counter olmadan dict ile

from itertools import product

genome = "ACGTTGCATGTCGCATGATGCATGAGAGCT"
k = 4
d = 1

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

def most_frequent_from_counts(counts):
    highest_frequency = max(counts.values())
    max_list = []
    for key, value in counts.items():
        if value == highest_frequency:
            max_list.append(key)
    return max_list

def approximate_patterns():
    counts = {}
    for kmer in all_kmers(k):
        count = 0
        for i in range(len(genome) - k + 1):
            if hamming_distance(kmer, genome[i:i+k]) <= d:
                count += 1
        counts[kmer] = count

    return most_frequent_from_counts(counts)

print(approximate_patterns())

"""