import re

def is_strictly_positive_number(string):
# Check is a string can be evaluated as a stricly positve number on the form 10.0, +1.0e+2, etc.
    if re.match('^[+]?([1-9][0-9]*(?:[\.][0-9]*)?|0*\.0*[1-9][0-9]*)(?:[eE][+-]?[0-9]+)?$',string):
        return True
    else:
        return False

def is_strictly_negative_number(string):
# Check is a string can be evaluated as a stricly negative number on the form -10.0, -1.0e+2, etc.
    if re.match('^[-]([1-9][0-9]*(?:[\.][0-9]*)?|0*\.0*[1-9][0-9]*)(?:[eE][+-]?[0-9]+)?$',string):
        return True
    else:
        return False

def is_nonzero_number(string):
# Check is a string can be evaluated as a non-zero number on the form 10.0, 1.0e+2, etc.
    if re.match('^[+-]?([1-9][0-9]*(?:[\.][0-9]*)?|0*\.0*[1-9][0-9]*)(?:[eE][+-]?[0-9]+)?$',string):
        return True
    else:
        return False

def is_number(string):
# Check is a string can be evaluated as a number on the form 10.0, -1.0e+2, etc.
    if re.match('^[+-]?([0-9]*(?:[\.][0-9]*)?|0*\.0*[1-9][0-9]*)(?:[eE][+-]?[0-9]+)?$',string):
        return True
    else:
        return False

def rational_fraction_from_string(string):
# Get rational fraction from sting of type n:m or n/m
    if re.match('^[1-9][0-9]*[:/][1-9][0-9]*$',string):
        n = float(string[0:string.find(':')])
        m = float(string[string.find(':')+1:])
        return n/m
    else:
        return None
