# -----------------------------------------------------------
# Demonstrates how to write helper library files using python
#
# (C) 2020 Kyle B. Vo, Virginia, USA
# Virginia Commonwealth University
# Society of bioinformatics
# Email thinhvo1101@gmail.com
# Github https://github.com/votb92/
# -----------------------------------------------------------

import DictHelper, StringHelper, IntHelper, ListHelper, TupleHelper

throwaway_1 = {"key1": 4,
               "key2": 3,
               "key3": 2,
               "key4": 1}
throwaway_2 = [{"key2": 323},
               {"key1": 34},
               {"key3": 52},
               {"key4": 41}]

DNA_seq = "AGTCTAGCWACGACGTCCAGCTCGACCWAGCAGSCGATAG"
ProteinSeq = "LLKHMLCMKAGKAMGMMCGLGAMLGMLKKCCHMAGCCKHKKCGMMMHMAKLHAGHHCGHCACGCHKLGMALLAGALACLKMGLHLLKALACKLHGACHGH"
DNA_sequence = "AGTCTAGC"
#Create variables
test_1 = DictHelper.ReverseKeyValuePairs(throwaway_1)
test_2 = ListHelper.SortListOfDictsByKey(throwaway_2)
test_3 = ListHelper.SortListOfDictsByValue(throwaway_2)
###########################################################
#########               EXAMPLE1                 ##########
###########################################################
print("DEMONSTRATING REVERSE KEY VALUE IN A DICTIONARY")
print(throwaway_1)
print(test_1)
print("\n\n")
###########################################################
#########               EXAMPLE2                 ##########
###########################################################
print("DEMONSTRATING SORTING A LIST OF DICTIONARIES BY THEIR VALUES")
print(test_2)
print(test_3)
print("\n\n")
###########################################################
#########               EXAMPLE3                 ##########
###########################################################
print("GC AND AT CONTENT OF A SEQUENCE: ")
print("\nThe sequence is: ", DNA_seq)
gcContent = StringHelper.gcContent(DNA_seq)
atContent = StringHelper.atContent(DNA_seq)
print("GC content is:",gcContent ,"\n", "AT content is: " , atContent)
print("\n\n")
###########################################################
#########               EXAMPLE4                 ##########
###########################################################
print("A DICTIONARY THAT TOTAL THE COUNTS OF NUCLEOTIDE SYMBOLS :","\n")
aDict = DictHelper.MakingHistogram(DNA_seq)
DictHelper.PrintHistogram(aDict)
print(aDict)
aProDict = DictHelper.MakingHistogram(ProteinSeq)
DictHelper.PrintHistogram(aProDict)
print(aProDict)
print("\n\n")

a_new_dict = DictHelper.PrintProteinTable()
print(DictHelper.ReverseKeyValuePairs(a_new_dict))
print("\n\n")
###########################################################
#########               EXAMPLE5                 ##########
###########################################################
print("P-DISTANCE EXAMPLE:")
Seq1 = "ATTGATTATGGGCGCGGATCGAGTCT"
Seq2 = "ATTGATTATGGGCCGGATATTTATCT"
print(Seq1 + "\n" + Seq2 +"\n")
print(StringHelper.p_distance(Seq1,Seq2))
###########################################################
#########               EXAMPLE6                 ##########
###########################################################
print("DEMONSTRATING HOW TO REVERSE STRING: ")
aString = "Hello World"
print(aString)
print(StringHelper.reserve(aString))
print("\n\n")
###########################################################
#########               EXAMPLE7                 ##########
###########################################################
print("DEMONSTRATING HOW TO MANIPULATE SEQUENCE: ")
print(DNA_sequence)
print(StringHelper.DNAtoRNA(DNA_sequence))
print(StringHelper.complimentary(DNA_sequence))
print(StringHelper.reserve(DNA_sequence))
print(StringHelper.reverseCompliment(DNA_sequence))
print(StringHelper.transcribe(DNA_sequence))
print("\n\n")
###########################################################
#########               EXAMPLE8                 ##########
###########################################################
print("INTEGER FUNCTIONS:")
aNumber = 2
print(IntHelper.isEven(aNumber))
print(IntHelper.isOdd(aNumber))
print(IntHelper.lastDigit(343452))

