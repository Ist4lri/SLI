# coding: utf-8
import sys
import os


def chek_fasta_file(file):
    with open(file, "r", encoding="utf-8") as readed_file:
        if readed_file.readline(1) != ">":
            if readed_file.readline(1) == "# coding: utf-8":
                return "script"
            return "pass"
        return file


ADN_LIST = ("A", "C", "G", "T")


def adn_read(fastafile):
    with open(fastafile, "r", encoding="utf-8") as readed_file:
        counter = 0
        header = ""
        for line in readed_file.readlines():
            counter += 1
            if line[0] == ">":
                header = line.strip()
            else:
                line = line.strip()
                line = line.upper()
                column_counter = 0
                for char in line:
                    column_counter += 1
                    if char not in ADN_LIST:
                        print(char + " It's not a nucl in line " + str(counter) +
                              " and column " + str(column_counter) + " for sequence "+header[1:])


if __name__ == "__main__":
    print(sys.argv)
    for arg in sys.argv[1:]:
        if os.path.isdir(arg):
            for path, dirs, files in os.walk(arg):
                for names in files:
                    print(chek_fasta_file(os.path.join(path, names)))
        else:
            print("FALSE")

        # try:
            # print(os.walk(arg))
        # except:
            # print("Not a directory, going to file mode...")


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
