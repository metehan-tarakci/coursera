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

def hamming_distance(seq1, seq2):
    count = 0
    for i in range(len(seq1)):
        if seq1[i] != seq2[i]:
            count += 1
    return count

def reverse_complement(DNAStr):        
    table = str.maketrans("ATGC", "TACG")  
    newStr = DNAStr.translate(table)      
    return newStr[::-1]

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
    start = skew_list()[0]
    possible_oric_site = genome[start:start+l]

    counts = {}

    for i in range(len(possible_oric_site) - k + 1):
        window = possible_oric_site[i:i+k]
        window_rc = reverse_complement(window)

        for neighbor in neighbors(window, d):
            if neighbor in counts:
                counts[neighbor] += 1
            else:
                counts[neighbor] = 1

        for neighbor in neighbors(window_rc, d):
            if neighbor in counts:
                counts[neighbor] += 1
            else:
                counts[neighbor] = 1

    return most_frequent_from_counts(counts)


print(f"Possible oric site starts: {skew_list()}")
print(" ".join(approximate_patterns()))