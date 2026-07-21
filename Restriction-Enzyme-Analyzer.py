def find_restriction_sites(sequence):
    enzymes = {
        "EcoRI": "GAATTC",
        "BamHI": "GGATCC",
        "HindIII": "AAGCTT",
        "PstI": "CTGCAG"
    }

    sequence = sequence.upper()

    print("\nRestriction Sites Found:")

    for enzyme, site in enzymes.items():
        position = sequence.find(site)

        while position != -1:
            print(f"{enzyme} site found at position {position + 1}")
            position = sequence.find(site, position + 1)


dna_sequence = input("Enter DNA sequence: ")
find_restriction_sites(dna_sequence)