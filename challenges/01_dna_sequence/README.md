# Challenge 01: DNA Sequence Manipulation 🧬

**Difficulty**: 🟢 Beginner  
**Topics**: String manipulation, Basic algorithms, Validation

## 📋 Description

DNA sequences are made up of four nucleotides: Adenine (A), Thymine (T), Guanine (G), and Cytosine (C). In this challenge, you'll implement several functions to manipulate and analyze DNA sequences.

## 🎯 Tasks

Implement the following functions in `solution.py`:

### 1. `validate_dna(sequence: str) -> bool`
Check if a DNA sequence is valid (contains only A, T, G, C characters, case-insensitive).

**Example:**
```python
validate_dna("ATGC")  # True
validate_dna("ATGX")  # False
validate_dna("atgc")  # True
```

### 2. `count_nucleotides(sequence: str) -> dict`
Count the occurrences of each nucleotide in the sequence.

**Example:**
```python
count_nucleotides("ATGCATGC")
# Returns: {'A': 2, 'T': 2, 'G': 2, 'C': 2}
```

### 3. `get_complement(sequence: str) -> str`
Return the complementary DNA sequence. The complement pairs are:
- A ↔ T
- G ↔ C

**Example:**
```python
get_complement("ATGC")  # Returns: "TACG"
```

### 4. `get_reverse_complement(sequence: str) -> str`
Return the reverse complement of the DNA sequence (complement + reverse).

**Example:**
```python
get_reverse_complement("ATGC")  # Returns: "GCAT"
```

### 5. `calculate_gc_content(sequence: str) -> float`
Calculate the GC content (percentage of G and C nucleotides) in the sequence.

**Example:**
```python
calculate_gc_content("ATGC")  # Returns: 50.0
calculate_gc_content("AAATTT")  # Returns: 0.0
```

### 6. `find_motif(sequence: str, motif: str) -> list`
Find all starting positions (0-indexed) of a motif in the DNA sequence.

**Example:**
```python
find_motif("ATGATGATG", "ATG")  # Returns: [0, 3, 6]
find_motif("AAAAA", "AA")  # Returns: [0, 1, 2, 3]
```

## 📝 Requirements

- All functions should handle both uppercase and lowercase input
- For invalid DNA sequences, `validate_dna` should return `False`
- Other functions can assume valid DNA input (but bonus points for validation!)
- Return types must match the specifications
- Empty sequences should be handled gracefully

## 🧪 Testing

Run the tests with:
```bash
pytest test_solution.py -v
```

## 💡 Hints

- Python's `str.upper()` or `str.lower()` can help with case-insensitivity
- Dictionary comprehension is useful for counting
- String slicing with `[::-1]` reverses a string
- The `str.count()` method can help with GC content
- Consider using a loop or regex for finding motifs

## 🎓 Learning Objectives

- String manipulation in Python
- Dictionary operations
- Input validation
- Algorithm implementation
- Edge case handling

## 🏆 Bonus Challenges

1. Optimize `find_motif` for overlapping patterns
2. Add a function to transcribe DNA to RNA (replace T with U)
3. Implement a function to find the longest repeated substring

Good luck! 🚀
