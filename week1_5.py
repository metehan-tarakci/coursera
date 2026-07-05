from collections import Counter

DNAStr = "AAA"
k = 9
l = 500
t = 3

def find_most_frequent_kmers(seq, k, t):
    kmers=[]
    for i in range(len(seq) - k + 1):
        kmers.append(seq[i:i+k])
    kmer_frequencies = Counter(kmers)

    result = []
    for kmer, count in kmer_frequencies.items():
        if count >= t:
            result.append(kmer)
    return result

def clump_finder(k, l):
    clump_kmers = set()
    for i in range(len(DNAStr) - l + 1):
        possible_oric = DNAStr[i:i+l]
        clump_kmers.update(find_most_frequent_kmers(possible_oric, k, t))
    return " ".join(clump_kmers)

print(clump_finder(k, l))