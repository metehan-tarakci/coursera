pattern="ATTGTGGGTAT"
d=2

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

print(" ".join(neighbors(pattern, d)))