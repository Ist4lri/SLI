# coding: utf-8
"""System and arg module."""
import sys
import os

ADN_LIST = ("A", "C", "G", "T")


def chek_fasta_file(file):
    """Check if a file is a fasta File or not. If yez, it returns itself
    if it doesn't, return some string to say that is not Fasta File."""
    with open(file, "r", encoding="utf-8") as readed_file:
        if readed_file.readline(1) != ">":
            if readed_file.readline(1) == "# coding: utf-8":
                return "script"
            return "pass"
        return file


def adn_read(fasta_file):
    """Detecting all non nucleotid in a fasta file, with the line and column position."""
    with open(fasta_file, "r", encoding="utf-8") as readed_file:
        line_of_file = 0
        name_sequence = ""
        for line in readed_file.readlines():
            line_of_file += 1
            if line[0] == ">":
                name_sequence = line.strip()
            else:
                line = line.strip()
                line = line.upper()
                column_of_file = 0
                for char in line:
                    column_of_file += 1
                    if char not in ADN_LIST:
                        print("\nOn "+fasta_file +
                              ", sequence named : "+name_sequence)
                        print("At line "+str(line_of_file) +
                              " and column "+str(column_of_file)+" :")
                        print("There is a non-nucleotide character : "+char+"\n")


if __name__ == "__main__":
    if sys.argv[-1] != sys.argv[0]:
        for arg in sys.argv:
            if os.path.isdir(arg):
                for path, dirs, files in os.walk(arg):
                    for names in files:
                        RESULT = chek_fasta_file(os.path.join(path, names))
                        if RESULT == os.path.join(path, names):
                            adn_read(RESULT)
                        else:
                            print("Not a Fasta File, going to the next file !")
            else:
                try:
                    os.path.isfile(arg)
                    RESULT = chek_fasta_file(arg)
                    if RESULT == arg:
                        adn_read(RESULT)
                    else:
                        print("Not a Fasta File, going to the next file !")
                except FileNotFoundError as error:
                    print(error)
    else:
        print("Veuillez renseigner un fichier ou un dossier !")


# def pierre_louis():  # C'EST PIERRE-LOÏC #
#     with open("a.fasta", "r") as mainFile:
#         if mainFile.readline()[0] == ">":
#             for line in mainFile.readlines():
#                 for char in line:
#                     if char != "A" or char != "C" or char != "G" or char != "T":
#                         print("Error this is not a nucleotide !")
#                         break
#         else:
#             print("This is not a fasta file !")
