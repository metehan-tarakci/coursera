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


def build_laplace_profile(motifs, k):
    Alist = [0]*k
    Clist = [0]*k
    Glist = [0]*k
    Tlist = [0]*k

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
        Alist[i] = (Alist[i]+1)/len(motifs)
        Clist[i] = (Clist[i]+1)/len(motifs)
        Glist[i] = (Glist[i]+1)/len(motifs)
        Tlist[i] = (Tlist[i]+1)/len(motifs)

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


def greedy_motif_search(dna_list, k, t):
    best_motifs = []
    for x in range(t):
        best_motifs.append(dna_list[x][0:k])

    best_score = score_motifs(best_motifs, k)

    first_string = dna_list[0]
    for i in range(len(first_string) - k + 1):
        seed = first_string[i:i+k]
        motifs = [seed]

        for x in range(1, t):
            Alist, Clist, Glist, Tlist = build_laplace_profile(motifs, k)
            next_motif = profile_most_probable_kmer(dna_list[x], k, Alist, Clist, Glist, Tlist)
            motifs.append(next_motif)

        current_score = score_motifs(motifs, k)
        if current_score < best_score:
            best_score = current_score
            best_motifs = motifs

    return best_motifs


k, t, dna_list = read_file("week3_4.txt")
print(" ".join(greedy_motif_search(dna_list, k, t)))