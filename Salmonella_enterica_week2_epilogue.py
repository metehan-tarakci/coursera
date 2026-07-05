from collections import Counter
from itertools import product

k = 9
d = 1
l = 500

def read_file(file):
    with open(file, "r") as f:
        for line in f:
            line = line.strip()
            if ">" in line:
                genome = "" 
            else:
                genome = genome + line
    return genome

genome = read_file("Salmonella_enterica.txt")

def skew_list():

    skew = [0]

    for i in range(len(genome)):

        if genome[i] == "G":
            skew.append(skew[i] + 1)

        elif genome[i] == "C":
            skew.append(skew[i] - 1)

        else:
            skew.append(skew[i])

    minimum_value = min(skew)

    oric_sites = []

    for position, element in enumerate(skew):

        if element == minimum_value:
            oric_sites.append(position)

    return oric_sites

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

def reverse_complement(DNAStr):        
    table=str.maketrans("ATGC","TACG")  
    newStr=DNAStr.translate(table)      
    return newStr[::-1]                 

def most_frequent(kmer_list):
    kmer_frequencies = Counter(kmer_list)
    highest_frequency = max(kmer_frequencies.values())
    max_list = []
    for key, value in kmer_frequencies.items():
        if value == highest_frequency:
            max_list.append(key)
    return max_list

def approximate_patterns():

    possible_oric_site = genome[skew_list()[0]:skew_list()[0]+l]
    results = []
    for kmer in all_kmers(k):
        count = 0
        for i in range(len(possible_oric_site) - k + 1):
            if hamming_distance(kmer, possible_oric_site[i:i+k]) <= d:
                count += 1
            if hamming_distance(reverse_complement(kmer), possible_oric_site[i:i+k]) <= d: 
                count += 1 
        if count > 0:
            for _ in range(count):
                results.append(kmer)
    return most_frequent(results)



print(f"Possible oric site starts: {skew_list()}")
print(" ".join(approximate_patterns()))
