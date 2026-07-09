
def read_file(file):
    with open(file, "r") as f:
        first_line = f.readline().rstrip()
        args = first_line.split()
        pattern = args[0]
        dna_list = []
        for i in range(1, len(args)):
            dna_list.append(args[i])

    return pattern, dna_list

pattern, dna_list = read_file("week3_6.txt")

def hamming_distance(seq1, seq2):
    count = 0
    for i in range(len(seq1)):
        if seq1[i] != seq2[i]:
            count += 1
    return count

def median_string():
    count=0
    for dna in dna_list:
        kmers=[]
        for i in range(len(dna)-len(pattern)+1):
            kmers.append(dna[i:i+len(pattern)])
        freq_dict={}
        for kmer in kmers:
            freq_dict[kmer] = hamming_distance(kmer, pattern)
            print(freq_dict)
        count+=min(freq_dict.values())
    return count

print(median_string())