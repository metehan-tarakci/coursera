from itertools import product

k = 6
dna_list = [
"CAAACCTATGGCGTCTGCGGTGGCAAGGTCCGAAGCAGTCAC",
"AGCTCTACTCCTATGCTCCAAGATGTGTTTCGAAGCGGGCAG",
"GTTAAGCGAAGGGGTTAAAGTGGTGGTCCCCTATACACCTCT",
"GGCACCCTACGAGTACGGCACTTCCGAAGTATACTGGCCGCG",
"CTAAGTTAAAGTCGAAGGTTCACAGCACCGTTTCCGAAGCAT",
"TGCCTAGAGTAATAAATCGGACCACGAAGGTGTTACAATGAC",
"TAAATGCATTTTCGAAGTTAGGTATCCATGTCGTGGACCCCT",
"AAGAGATGATCACGGAATGATGTCCGAAGAGAGCACCTAAGG",
"GCACTGGTAGTGAAGAGTCATGGGACGTCGCAAGCACGAAGG",
"ACGAAACGAAGTCGACGATTCCCGACAACTGCGGGGATGGAA"
]

def hamming_distance(seq1, seq2):
    count = 0
    for i in range(len(seq1)):
        if seq1[i] != seq2[i]:
            count += 1
    return count

def all_kmers(k):
    kmers = set()
    for p in product('ACGT', repeat=k):
        kmers.add(''.join(p))
    return kmers

def min_distance_to_string(pattern, text):
    min_dist = len(pattern) + 1
    for i in range(len(text) - len(pattern) + 1):
        dist = hamming_distance(pattern, text[i:i+len(pattern)])
        if dist < min_dist:
            min_dist = dist
    return min_dist

def median_string(dna_list, k):
    best_pattern = None
    best_distance = None

    for kmer in all_kmers(k):
        total_distance = 0
        for dna in dna_list:
            total_distance += min_distance_to_string(kmer, dna)

        if best_distance is None or total_distance < best_distance:
            best_distance = total_distance
            best_pattern = kmer

    return best_pattern


print(median_string(dna_list, k))