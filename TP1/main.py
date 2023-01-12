"""Module providingFunction checking if it's correct fasta file"""
from re import search


def check_file(file):
    """Function checking file if it's correct fasta"""
    # Open file, and close the file at the end of the with
    with open(file, "r", encoding="utf-8") as main_file:
        for line in main_file.readlines():  # for each line of the file
            if line[0] != ">":  # if first character of the line is equal to ">"
                # if the character is not like the regex
                if search(r'[^ATGCatgc\n]', line) is not None:
                    # raise error
                    print("Error, one letter is not a nucleotide ! ")


check_file("fichier.fasta")  # Laucnh the function with the file asked.
