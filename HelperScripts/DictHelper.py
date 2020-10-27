# -----------------------------------------------------------
# Demonstrates how to write helper library files using python
#
# (C) 2020 Kyle B. Vo, Virginia, USA
# Virginia Commonwealth University
# Society of bioinformatics
# Email thinhvo1101@gmail.com
# Github https://github.com/votb92/
# -----------------------------------------------------------
import StringHelper, IntHelper, ListHelper, TupleHelper
import matplotlib.pyplot as plt
"""
| reverse key and value in a dictionary
|
| Parameters:
|    a_dict (dict): a dictionary that need to be reversed
|
| Returns:
|    dict: a reversed dictionary
"""
def ReverseKeyValuePairs(a_dict: dict) -> dict :
    a_dict = dict((y, x) for x, y in a_dict.items())
    return a_dict

"""
| create a dictionary that hold each character of a string as key and the total number of that character as values
|
| Parameters:
|    seq (string): a string sequence
|
| Returns:
|    dict: a histogram dictionary
"""
def MakingHistogram(seq):
    aDict = {}
    for character in seq:
        aDict[character]= aDict.get(character,0)+1
    for k, v in aDict.items() :
        aDict[k] = v * 100 / len(seq)
    return aDict

"""
| visualizing histogram that was made in MakingHistogram function
|
| Parameters:
|    aDict (dict): a histogram dictionary
|
"""
def PrintHistogram(aDict):
    plt.bar(list(aDict.keys()), aDict.values(), color='g')
    plt.show()

"""
| a reference function that will print out a Dictionary of Amino acid mapping to their abbreviations
|
| Returns:
|    dict: an amino acid reference dictionary
"""
def PrintProteinTable():
    proteinDict = {'Alanine':'A',
                   'Arginine':'R',
                   'Asparagine':'N',
                   'Aspartic acid':'D',
                   'Cysteine':'C',
                   'Glutamic acid':'E',
                   'Glutamine':'Q',
                   'Glycine':'G',
                   'Histidine':'H',
                   'Hydroxyproline':'O',
                   'Isoleucine':'I',
                   'Leucine':'L',
                   'Lysine':'K',
                   'Methionine':'M',
                   'Phenylalanine':'F',
                   'Proline':'P',
                   'Pyroglutamatic':'U',
                   'Serine':'S',
                   'Threonine':'T',
                   'Tryptophan':'W',
                   'Tyrosine':'Y',
                   'Valine':'V'}
    print(proteinDict)
    return proteinDict

