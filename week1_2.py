from collections import Counter

def find_most_frequent_kmers(sequence, k_len):

    kmers = []
    for i in range(len(sequence) - k_len + 1):
        kmers.append(sequence[i:i+k_len])

    kmer_frequencies = Counter(kmers)

    highest_frequency = max(kmer_frequencies.values())

  
    list=[]
    for key, value in kmer_frequencies.items():
        if value == highest_frequency:
            list.append(key)
    return list

print(find_most_frequent_kmers("TAAAGACTGCCGAGAGGCCAACACGAGTGCTAGAACGAGGGGCGTAAACGCGGGTCCGAT", 9))