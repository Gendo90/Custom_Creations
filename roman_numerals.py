# map for each character to value
def getValMap():
    val_map = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    return val_map

# converts a roman numeral string to regular digits
def convertToDigits(s, val_map):
    arr = [a for a in s]

    total = 0
    last_val = 0

    while(len(arr) > 0):
        curr_val = val_map[arr.pop()]
        if(curr_val < last_val):
            total -= curr_val
        else:
            total += curr_val
            last_val = curr_val

    return total

# convert to minimized roman numeral
def minimizedRomanNumeral(n):
    result = ""

    # add thousands place
    result += "M"*(n // 1000)

    # add hundreds place
    n_hund = (n % 1000) // 100

    # make these conditionals a function when refactoring
    if(n_hund < 4):
        result += "C" * n_hund
    elif(n_hund == 4):
        result += "CD"
    elif(n_hund < 9):
        result += "D" + ("C" * (n_hund - 5))
    else:
        result += "CM"

    # add tens place
    n_tens = (n % 100) // 10

    if(n_tens < 4):
        result += "X" * n_tens
    elif(n_tens == 4):
        result += "XL"
    elif(n_tens < 9):
        result += "L" + ("X" * (n_tens - 5))
    else:
        result += "XC"

    # add ones place
    n_ones = n % 10

    if(n_ones < 4):
        result += "I" * n_ones
    elif(n_ones == 4):
        result += "IX"
    elif(n_ones < 9):
        result += "V" + ("I" * (n_ones - 5))
    else:
        result += "IX"

    return result