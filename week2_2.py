dnaStr="CTTGAAGTGGACCTCTAGTTCCTCTACAAAGAACAGGTTGACCTGTCGCGAAG"
mutatedStr="ATGCCTTACCTAGATGCAATGACGGACGTATTCCTTTTGCCTCAACGGCTCCT"

original_seqs= []
mutated_seqs=[]

for i in range(len(dnaStr)):
    if dnaStr[i] != mutatedStr[i]:
        original_seqs.append(f"{dnaStr[i]}")
        mutated_seqs.append(f"{mutatedStr[i]}, sequence no: {i+1}")

for x, y in zip(original_seqs, mutated_seqs):
    print("Original:", x, "Mutated:", y)

print(len(mutated_seqs))
