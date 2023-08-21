import random

############################################################################
def setup_word_dictionary():
    fileHandler = open("dictionary.txt", "r")

    # Get list of all lines in file
    listOfLines = fileHandler.readlines()

    # Close file
    fileHandler.close()

    word_arr = []

    for line in listOfLines:
        curr_word = line.strip()
        word_arr.append(curr_word)

    return word_arr

word_dictionary = setup_word_dictionary()

def get_random_word():
    size = len(word_dictionary)
    
    return word_dictionary[random.randint(0, size-1)]

# gives 2 random words as a name by default, more or fewer if the num_words parameter is set to a different integer
def generate_name(num_words=2):
    return " ".join([get_random_word().capitalize() for i in range(num_words)])
#############################################################################