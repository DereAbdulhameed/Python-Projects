"""
Example usage of DNA sequence functions.
Run this file to see how the functions work with sample data.
"""

from solution import (
    validate_dna,
    count_nucleotides,
    get_complement,
    get_reverse_complement,
    calculate_gc_content,
    find_motif
)


def run_examples():
    print("=" * 60)
    print("DNA SEQUENCE MANIPULATION - EXAMPLES")
    print("=" * 60)
    
    # Example DNA sequence
    dna = "ATGCGATACGCTTGA"
    
    print(f"\nOriginal DNA Sequence: {dna}")
    print("-" * 60)
    
    # 1. Validate DNA
    print("\n1. VALIDATE DNA")
    print(f"   Is '{dna}' valid? {validate_dna(dna)}")
    print(f"   Is 'ATGX' valid? {validate_dna('ATGX')}")
    
    # 2. Count Nucleotides
    print("\n2. COUNT NUCLEOTIDES")
    counts = count_nucleotides(dna)
    print(f"   Nucleotide counts: {counts}")
    
    # 3. Get Complement
    print("\n3. GET COMPLEMENT")
    complement = get_complement(dna)
    print(f"   Complement: {complement}")
    
    # 4. Get Reverse Complement
    print("\n4. GET REVERSE COMPLEMENT")
    rev_complement = get_reverse_complement(dna)
    print(f"   Reverse Complement: {rev_complement}")
    
    # 5. Calculate GC Content
    print("\n5. CALCULATE GC CONTENT")
    gc = calculate_gc_content(dna)
    print(f"   GC Content: {gc:.2f}%")
    
    # 6. Find Motif
    print("\n6. FIND MOTIF")
    motif = "ATG"
    positions = find_motif(dna, motif)
    print(f"   Motif '{motif}' found at positions: {positions}")
    
    print("\n" + "=" * 60)
    print("ADDITIONAL EXAMPLES")
    print("=" * 60)
    
    # More examples
    examples = [
        ("AAATTTGGGCCC", "AAA"),
        ("GCGCGCGC", "GCG"),
        ("ATATATATATAT", "AT"),
    ]
    
    for seq, mot in examples:
        print(f"\nSequence: {seq}")
        print(f"  GC Content: {calculate_gc_content(seq):.2f}%")
        print(f"  Motif '{mot}' at: {find_motif(seq, mot)}")
        print(f"  Complement: {get_complement(seq)}")
    
    print("\n" + "=" * 60)


if __name__ == "__main__":
    run_examples()
