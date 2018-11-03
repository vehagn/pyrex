import re

# Check if string is a strictly positive number using regex matching
def is_strictly_positive_number(string):
    if re.match('^[+]?([1-9][0-9]*(?:[\.][0-9]*)?|0*\.0*[1-9][0-9]*)(?:[eE][+-]?[0-9]+)?$',string):
        return True
    else:
        return False

# Check if string is a strictly negative number using regex matching
def is_strictly_negative_number(string):
    if re.match('^[-]([1-9][0-9]*(?:[\.][0-9]*)?|0*\.0*[1-9][0-9]*)(?:[eE][+-]?[0-9]+)?$',string):
        return True
    else:
        return False

# Check if string is a non-zero number using regex matching
def is_nonzero_number(string):
    if re.match('^[+-]?([1-9][0-9]*(?:[\.][0-9]*)?|0*\.0*[1-9][0-9]*)(?:[eE][+-]?[0-9]+)?$',string):
        return True
    else:
        return False

# Check if string is a number using regex matching
def is_number(string):
    if re.match('^[+-]?([0-9]*(?:[\.][0-9]*)?|0*\.0*[1-9][0-9]*)(?:[eE][+-]?[0-9]+)?$',string):
        return True
    else:
        return False

# Get ratio from string
def rational_fraction_from_string(string):
    if re.match('^[1-9][0-9]*:[1-9][0-9]*$',string):
        n = float(string[0:string.find(':')])
        m = float(string[string.find(':')+1:])
        return n/m
    else:
        return None
