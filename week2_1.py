def skew_list(genome):
    
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

    return " ".join(map(str, oric_sites))

print(skew_list("CATTCCAGTACTTCATGATGGCGTGAAGA"))