# coding: utf-8
"""Check if fasta file and check if there is non nucleotid character"""
import sys
import os

ADN_LIST = ("A", "C", "G", "T")


def check_fasta_file(file):
    """Check if a file is a fasta File or not. If yez, it returns itself
    if it doesn't, return some string to say that is not Fasta File."""
    with open(file, "r", encoding="utf-8") as readed_file:
        if readed_file.readline(1) != ">":  # First char of a fasta file
            # Obviously, if the first line is not this one, this break the func...
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
    if len(sys.argv) <= 0:  # Check if there is other argument
        for arg in sys.argv:  # This is stupid but check all argument, including this script
            if os.path.isdir(arg):  # If it's directory
                # Takes path, dir, and files of the directory
                for path, dirs, files in os.walk(arg):
                    for names in files:  # for each names
                        # The path to send to the func before
                        RESULT = check_fasta_file(os.path.join(path, names))
                        if RESULT == os.path.join(path, names):
                            adn_read(RESULT)
                        else:
                            print(
                                f"{os.path.join(path,names)} is not a Fasta File")
            else:
                try:
                    os.path.isfile(arg)  # check if the file exist...
                    RESULT = check_fasta_file(arg)
                    if RESULT == arg:
                        adn_read(RESULT)
                    else:
                        print(f"{os.path.join(path,names)} is not a Fasta File")
                # Where is the file ? (In the Kitchen ?)
                except FileNotFoundError as error:
                    print(error)
    else:
        # Nice try but it's empty
        print("Veuillez renseigner un fichier ou un dossier !")
