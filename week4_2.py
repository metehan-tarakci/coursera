import random

def read_file(file):
    with open(file, "r") as f:
        first_line = f.readline().rstrip()
        args = first_line.split()
        k = args[0]
        t = args[1]
        N = args[2]

        dna_list = []
        for i in range(3, len(args)):
            dna_list.append(args[i])

    return int(k), int(t), int(N), dna_list


def build_profile(motifs, k):
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


def profile_randomly_generated_kmer(text, k, Alist, Clist, Glist, Tlist):
    kmers = []
    weights = []
    for i in range(len(text) - k + 1):
        kmer = text[i:i+k]
        kmers.append(kmer)
        weights.append(probability(kmer, Alist, Clist, Glist, Tlist, k))

    chosen = random.choices(kmers, weights=weights, k=1)
    return chosen[0]


def gibbs_sampler(dna_list, k, t, N):
    motifs = []
    for dna in dna_list:
        start = random.randint(0, len(dna) - k)
        motifs.append(dna[start:start+k])

    best_motifs = motifs

    for j in range(N):
        i = random.randint(0, t - 1)

        motifs_except_i = []
        for x in range(t):
            if x != i:
                motifs_except_i.append(motifs[x])

        Alist, Clist, Glist, Tlist = build_profile(motifs_except_i, k)
        motifs[i] = profile_randomly_generated_kmer(dna_list[i], k, Alist, Clist, Glist, Tlist)

        if score_motifs(motifs, k) < score_motifs(best_motifs, k):
            best_motifs = list(motifs)

    return best_motifs


def run_many_times(dna_list, k, t, N, starts=20):
    best_motifs = gibbs_sampler(dna_list, k, t, N)
    best_score = score_motifs(best_motifs, k)

    for _ in range(starts - 1):
        motifs = gibbs_sampler(dna_list, k, t, N)
        current_score = score_motifs(motifs, k)
        if current_score < best_score:
            best_score = current_score
            best_motifs = motifs

    return best_motifs


k, t, N, dna_list = read_file("week4_2.txt")
print(" ".join(run_many_times(dna_list, k, t, N)))