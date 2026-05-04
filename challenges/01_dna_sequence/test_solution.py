import pytest
from solution import (
    validate_dna,
    count_nucleotides,
    get_complement,
    get_reverse_complement,
    calculate_gc_content,
    find_motif
)


class TestValidateDNA:
    def test_valid_uppercase(self):
        assert validate_dna("ATGC") == True
        assert validate_dna("AAAA") == True
        assert validate_dna("TTTTGGGGCCCC") == True
    
    def test_valid_lowercase(self):
        assert validate_dna("atgc") == True
        assert validate_dna("aaaa") == True
    
    def test_valid_mixed_case(self):
        assert validate_dna("AtGc") == True
        assert validate_dna("aTgC") == True
    
    def test_invalid_characters(self):
        assert validate_dna("ATGX") == False
        assert validate_dna("ATGC123") == False
        assert validate_dna("ATGC ") == False
        assert validate_dna("ATGCN") == False
    
    def test_empty_sequence(self):
        assert validate_dna("") == True


class TestCountNucleotides:
    def test_equal_distribution(self):
        result = count_nucleotides("ATGC")
        assert result == {'A': 1, 'T': 1, 'G': 1, 'C': 1}
    
    def test_repeated_sequence(self):
        result = count_nucleotides("ATGCATGC")
        assert result == {'A': 2, 'T': 2, 'G': 2, 'C': 2}
    
    def test_single_nucleotide(self):
        result = count_nucleotides("AAAA")
        assert result == {'A': 4, 'T': 0, 'G': 0, 'C': 0}
    
    def test_lowercase(self):
        result = count_nucleotides("atgc")
        assert result == {'A': 1, 'T': 1, 'G': 1, 'C': 1}
    
    def test_empty_sequence(self):
        result = count_nucleotides("")
        assert result == {'A': 0, 'T': 0, 'G': 0, 'C': 0}


class TestGetComplement:
    def test_simple_complement(self):
        assert get_complement("ATGC") == "TACG"
        assert get_complement("AAAA") == "TTTT"
        assert get_complement("GGGG") == "CCCC"
    
    def test_longer_sequence(self):
        assert get_complement("ATGCATGC") == "TACGTACG"
    
    def test_lowercase(self):
        result = get_complement("atgc")
        assert result.upper() == "TACG"
    
    def test_empty_sequence(self):
        assert get_complement("") == ""


class TestGetReverseComplement:
    def test_simple_reverse_complement(self):
        assert get_reverse_complement("ATGC") == "GCAT"
        assert get_reverse_complement("AAAA") == "TTTT"
    
    def test_longer_sequence(self):
        assert get_reverse_complement("ATGCATGC") == "GCATGCAT"
    
    def test_palindrome(self):
        assert get_reverse_complement("GAATTC") == "GAATTC"
    
    def test_lowercase(self):
        result = get_reverse_complement("atgc")
        assert result.upper() == "GCAT"
    
    def test_empty_sequence(self):
        assert get_reverse_complement("") == ""


class TestCalculateGCContent:
    def test_fifty_percent(self):
        assert calculate_gc_content("ATGC") == 50.0
    
    def test_zero_percent(self):
        assert calculate_gc_content("AAATTT") == 0.0
    
    def test_hundred_percent(self):
        assert calculate_gc_content("GGGGCCCC") == 100.0
    
    def test_twenty_five_percent(self):
        assert calculate_gc_content("AAAG") == 25.0
    
    def test_lowercase(self):
        assert calculate_gc_content("atgc") == 50.0
    
    def test_empty_sequence(self):
        assert calculate_gc_content("") == 0.0


class TestFindMotif:
    def test_single_occurrence(self):
        assert find_motif("ATGCATGC", "GCA") == [2]
    
    def test_multiple_occurrences(self):
        assert find_motif("ATGATGATG", "ATG") == [0, 3, 6]
    
    def test_overlapping_occurrences(self):
        assert find_motif("AAAAA", "AA") == [0, 1, 2, 3]
    
    def test_no_occurrence(self):
        assert find_motif("ATGC", "TTT") == []
    
    def test_motif_at_end(self):
        assert find_motif("ATGCATG", "ATG") == [0, 4]
    
    def test_full_sequence_match(self):
        assert find_motif("ATGC", "ATGC") == [0]
    
    def test_lowercase(self):
        result = find_motif("atgatgatg", "atg")
        assert result == [0, 3, 6]
    
    def test_empty_sequence(self):
        assert find_motif("", "ATG") == []
    
    def test_empty_motif(self):
        assert find_motif("ATGC", "") == []


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
