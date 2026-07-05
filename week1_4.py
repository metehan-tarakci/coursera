pattern= "AA"
genome = "AAACATAGGATCAAC"


for i in range(len(genome)-len(pattern)+1):
    if genome[i:i+len(pattern)] == pattern:
        print(i, end=" ")