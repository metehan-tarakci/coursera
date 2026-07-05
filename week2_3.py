pattern = "TGT"
genome = "CGTGACAGTGTATGGGCATCTTT"
d = 1

def hamming_distance(seq1,seq2):
    count=0
    for i in range(len(seq1)):
        if seq1[i]!=seq2[i]:
            count+=1
    return count

def approximate_pattern_positions():
    results = []
    for i in range(0, len(genome)-len(pattern)+1): 
        if hamming_distance(pattern, genome[i:i+len(pattern)]) <= d:
            results.append(i)
    return " ".join(map(str, results))

print(approximate_pattern_positions())