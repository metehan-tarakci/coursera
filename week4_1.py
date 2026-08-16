import random

def read_file(file):
    with open(file, "r") as f:
        first_line = f.readline().rstrip()
        args = first_line.split()
        k = args[0]
        t = args[1]

        dna_list = []
        for i in range(2, len(args)):
            dna_list.append(args[i])

    return int(k), int(t), dna_list


def build_profile(motifs, k):
    # start every count at 1 (pseudocount), not 0
    Alist = [1]*k
    Clist = [1]*k
    Glist = [1]*k
    Tlist = [1]*k

    for i in range(k):
        for motif in motifs:
            if motif[i] == "A":
                Alist[i] += 1
            elif motif[i] == "C":
                Clist[i] += 1
            elif motif[i] == "G":
                Glist[i] += 1
            elif motif[i] == "T":
                Tlist[i] += 1

    # total count per position is now len(motifs) + 4 (one extra per nucleotide)
    total = len(motifs) + 4
    for i in range(k):
        Alist[i] = Alist[i] / total
        Clist[i] = Clist[i] / total
        Glist[i] = Glist[i] / total
        Tlist[i] = Tlist[i] / total

    return Alist, Clist, Glist, Tlist


def probability(kmer, Alist, Clist, Glist, Tlist, k):
    product = 1
    for i in range(k):
        if kmer[i] == "A":
            product *= Alist[i]
        elif kmer[i] == "C":
            product *= Clist[i]
        elif kmer[i] == "G":
            product *= Glist[i]
        elif kmer[i] == "T":
            product *= Tlist[i]
    return product


def profile_most_probable_kmer(text, k, Alist, Clist, Glist, Tlist):
    best_kmer = text[0:k]
    best_probability = -1

    for i in range(len(text) - k + 1):
        kmer = text[i:i+k]
        prob = probability(kmer, Alist, Clist, Glist, Tlist, k)
        if prob > best_probability:
            best_probability = prob
            best_kmer = kmer

    return best_kmer


def score_motifs(motifs, k):
    consensus = ""
    for i in range(k):
        counts = {"A": 0, "C": 0, "G": 0, "T": 0}
        for motif in motifs:
            counts[motif[i]] += 1
        best_letter = max(counts, key=counts.get)
        consensus += best_letter

    total_score = 0
    for motif in motifs:
        for i in range(k):
            if motif[i] != consensus[i]:
                total_score += 1

    return total_score


def motifs_from_profile(dna_list, k, Alist, Clist, Glist, Tlist):
    motifs = []
    for dna in dna_list:
        motifs.append(profile_most_probable_kmer(dna, k, Alist, Clist, Glist, Tlist))
    return motifs


def randomized_motif_search(dna_list, k, t):
    motifs = []
    for dna in dna_list:
        start = random.randint(0, len(dna) - k)
        motifs.append(dna[start:start+k])

    best_motifs = motifs

    while True:
        Alist, Clist, Glist, Tlist = build_profile(motifs, k)
        motifs = motifs_from_profile(dna_list, k, Alist, Clist, Glist, Tlist)

        if score_motifs(motifs, k) < score_motifs(best_motifs, k):
            best_motifs = motifs
        else:
            return best_motifs


def run_many_times(dna_list, k, t, iterations=1000):
    best_motifs = randomized_motif_search(dna_list, k, t)
    best_score = score_motifs(best_motifs, k)

    for _ in range(iterations - 1):
        motifs = randomized_motif_search(dna_list, k, t)
        current_score = score_motifs(motifs, k)
        if current_score < best_score:
            best_score = current_score
            best_motifs = motifs

    return best_motifs


k, t, dna_list = read_file("week4_1.txt")
print(" ".join(run_many_times(dna_list, k, t)))