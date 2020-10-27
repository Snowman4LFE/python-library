# -----------------------------------------------------------
# Demonstrates how to write helper library files using python
#
# (C) 2020 Kyle B. Vo, Virginia, USA
# Virginia Commonwealth University
# Society of bioinformatics
# Email thinhvo1101@gmail.com
# Github https://github.com/votb92/
# -----------------------------------------------------------
import DictHelper, StringHelper, IntHelper, TupleHelper
"""
| Sort a list of dictionaries by keys
|
| Parameters:
|    a_list (dict): a list that has multiple dicts need to be sorted
|
| Returns:
|    list: a sorted list of dictionaries in list form
"""
def SortListOfDictsByKey(a_list: list()) -> list :
    temp = list(map(dict, sorted(list(i.items()) for i in a_list)))
    return temp

"""
| Sort a list of dictionaries by values
|
| Parameters:
|    a_list (dict): a list that has multiple dicts need to be sorted
|
| Returns:
|    list: a sorted list of dictionaries in list form
"""
def SortListOfDictsByValue(a_list: list()) -> list :
    temp1 = []
    temp2 = []
    for i in a_list:
        i = DictHelper.ReverseKeyValuePairs(i)
        temp1.append(i)
    temp1 = SortListOfDictsByKey(temp1)
    for i in temp1:
        i = DictHelper.ReverseKeyValuePairs(i)
        temp2.append(i)
    return temp2
