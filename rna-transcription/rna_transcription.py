def to_rna(dna_strand):
    rna_strand = ""
    for dna in dna_strand:
        rna_strand += "G" if dna == "C" else ""
        rna_strand += "C" if dna == "G" else ""
        rna_strand += "A" if dna == "T" else ""
        rna_strand += "U" if dna == "A" else ""
    return rna_strand