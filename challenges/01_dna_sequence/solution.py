def validate_dna(sequence: str) -> bool:
    """
    Check if a DNA sequence is valid (contains only A, T, G, C).
    
    Args:
        sequence: DNA sequence string
        
    Returns:
        bool: True if valid, False otherwise
    """
     
    nucleotide = 'ATGC'
    is_valid = all(i in nucleotide for i in sequence.upper())
    return is_valid
   
    



def count_nucleotides(sequence: str) -> dict:
    """
    Count the occurrences of each nucleotide in the sequence.
    
    Args:
        sequence: DNA sequence string
        
    Returns:
        dict: Dictionary with counts for A, T, G, C
    """
     
    count_A = sequence.upper().count("A")
    count_T = sequence.upper().count("T")
    count_G = sequence.upper().count("G")
    count_C = sequence.upper().count("C")
    counts = {'A': count_A, "T": count_T, "G": count_G, "C": count_C}
    return counts






def get_complement(sequence: str) -> str:
    """
    Return the complementary DNA sequence.
    A <-> T, G <-> C
    
    Args:
        sequence: DNA sequence string
        
    Returns:
        str: Complementary DNA sequence
    """
    
    complement = ""
    for i in sequence:
        if i.upper() == "A":
            complement += "T"
        elif i.upper() == "T":
            complement += "A"
        elif i.upper() == "G":
            complement += "C"
        elif i.upper() == "C":
            complement += "G"
    return complement
    



def get_reverse_complement(sequence: str) -> str:
    """
    Return the reverse complement of the DNA sequence.
    
    Args:
        sequence: DNA sequence string
        
    Returns:
        str: Reverse complement DNA sequence
    """
     
    reverse_complement = ""
    for i in sequence:
        if i.upper() == "A":
            reverse_complement = "T" + reverse_complement
        elif i.upper() == "T":
            reverse_complement = "A" + reverse_complement
        elif i.upper() == "G":
            reverse_complement = "C" + reverse_complement
        elif i.upper() == "C":
            reverse_complement = "G" + reverse_complement
    return reverse_complement



def calculate_gc_content(sequence: str) -> float:
    """
    Calculate the GC content (percentage of G and C) in the sequence.
    
    Args:
        sequence: DNA sequence string
        
    Returns:
        float: GC content as a percentage (0-100)
    """

    gc_find = ""
    try:
        for i in sequence:
            if i == "g" or i == "G" or i == "c" or i == "C":
                gc_find += i
        gc_length = len(gc_find)
        sequence_length = len(sequence)
        percent_gc = 100 * gc_length/sequence_length
        return(percent_gc)
    except ZeroDivisionError:
        return 0.0
        


def find_motif(sequence: str, motif: str) -> list:
    """
    Find all starting positions of a motif in the DNA sequence.
    
    Args:
        sequence: DNA sequence string
        motif: Motif to search for
        
    Returns:
        list: List of starting positions (0-indexed)
    """

    positions = []
    motif_length = len(motif)
    for i in range(len(sequence)):
        if sequence[i: i + motif_length] == motif and motif != "":
            positions.append(i)
    return positions
