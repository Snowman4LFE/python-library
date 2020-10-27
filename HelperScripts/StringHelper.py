# -----------------------------------------------------------
# Demonstrates how to write helper library files using python
#
# (C) 2020 Kyle B. Vo, Virginia, USA
# Virginia Commonwealth University
# Society of bioinformatics
# Email thinhvo1101@gmail.com
# Github https://github.com/votb92/
# -----------------------------------------------------------
"""
| Returning GC content of a string sequence
|
| Parameters:
|    seq (string): a string sequence
|
| Returns:
|    float: GC content
"""
def gcContent(seq):
    seq = seq.lower()
    count_gc = 0
    total_nucleotides = len(seq)
    for nucleotide in seq :
        if nucleotide == "g" or nucleotide == "c" or nucleotide == "s" :
            count_gc += 1
    return count_gc / total_nucleotides

"""
| Returning AT content of a string sequence
|
| Parameters:
|    seq (string): a string sequence
|
| Returns:
|    float: AT content
"""
def atContent(seq):
    seq = seq.lower()
    count_gc = 0
    total_nucleotides = len(seq)
    for nucleotide in seq:
        if nucleotide == "a" or nucleotide == "t" or nucleotide == "w" :
            count_gc += 1
    return count_gc / total_nucleotides

"""
| Returning a complementary of a given sequence
|
| Parameters:
|    seq (string): a string sequence
|
| Returns:
|    string: complementary sequence 
"""
def complimentary(seq):
    tempSeq = ""
    seq = seq.lower()
    for base in seq:
        if base == "g":
            tempSeq += "c"
        elif base == "c":
            tempSeq += "g"
        elif base == "a":
            tempSeq += "t"
        elif base == "c":
            tempSeq += "a"
        else:
            tempSeq += base
    tempSeq = tempSeq.upper()
    return tempSeq

"""
| Returning a reversed of a string
|
| Parameters:
|    aString (string): a string sequence
|
| Returns:
|    string: a reversed string
"""
def reserve(aString):
    aReserved = aString[::-1]
    return aReserved

"""
| Returning a reversed complement of a string
|
| Parameters:
|    aString (string): a string sequence
|
| Returns:
|    string: a reversed string
"""
def reverseCompliment(aString):
    temp = complimentary(reserve(aString))
    return temp

"""
| Returning a RNA sequence of a given DNA sequence string
|
| Parameters:
|    seq (string): a given DNA sequence string
|
| Returns:
|    string: a RNA sequence
"""
def DNAtoRNA(seq):
    tempSeq=""
    seq = seq.lower()
    for base in seq:
        if base == "t":
            tempSeq += "u"
        else:
            tempSeq += base
    tempSeq = tempSeq.upper()
    return tempSeq

"""
| Returning an DNA sequence of a given RNA sequence string
|
| Parameters:
|    seq (string): a given RNA sequence string
|
| Returns:
|    string: a DNA sequence
"""
def RNAtoDNA(seq):
    tempSeq=""
    seq = seq.lower()
    for base in seq:
        if base == "u":
            tempSeq += "t"
        else:
            tempSeq += base
    tempSeq = tempSeq.upper()
    return tempSeq

"""
| Returning a product of transcription given DNA sequence
|
| Parameters:
|    seq (string): a given DNA sequence string
|
| Returns:
|    string: a RNA product
"""
def transcribe(seq):
    tempSeq = ""
    seq = seq.lower()
    for base in seq:
        if base == "g":
            tempSeq += "c"
        elif base == "c":
            tempSeq += "g"
        elif base == "a":
            tempSeq += "u"
        elif base == "t":
            tempSeq += "a"
        else:
            tempSeq += base
    tempSeq = tempSeq.upper()
    return tempSeq

"""
| Returning a p-distance of 2 same length sequence
|
| Parameters:
|    seq1 (string): a given sequence string
|    seq2 (string): a given sequence string|
| Returns:
|    float: a p-distance number
"""
def p_distance(firstSeq, secondSeq):
    diff = 0
    length = len(firstSeq)
    for i in range(length):
        if (firstSeq[i] != secondSeq[i]):
            diff += 1
    return diff/float(length)


