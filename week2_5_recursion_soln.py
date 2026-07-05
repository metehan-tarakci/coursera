genome = "GGGGAATGGGGTCAAGGGGCGAAATTCAATCAAGGGGAATGGGGAATGGGGTCAATCAATCAAAATCGAAATCGAAATTCAAAATAATGGGGGGGGACATTCAATCAAAATACATTCAAACATACATTCAAACATACATTCAATCAACGAACATTCAACGAAATGGGGCGAGGGGGGGGACATACATCGATCAATCAAACATGGGGGGGGACATTCAAGGGGCGACGAGGGGCGACGATCAAGGGGGGGGGGGGACATTCAAAATGGGGACATTCAAAATCGAAATGGGGTCAAACATGGGGGGGGGGGGAATCGATCAAAATCGATCAAACAT"
k = 5
d = 3

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

def most_frequent_from_counts(counts):
    highest_frequency = max(counts.values())
    max_list = []
    for key, value in counts.items():
        if value == highest_frequency:
            max_list.append(key)
    return max_list

def approximate_patterns():
    counts = {}

    for i in range(len(genome) - k + 1):
        window = genome[i:i+k]

        for neighbor in neighbors(window, d):
            if neighbor in counts:
                counts[neighbor] += 1
            else:
                counts[neighbor] = 1

    return most_frequent_from_counts(counts)

print(" ".join(approximate_patterns()))