"""Entertaining Argparser"""
from argparse import ArgumentParser
from argparse import FileType
from argparse import ArgumentTypeError

PROGRAM_DESCRIPTION = '''For learning argparser'''


def create_parser():
    """create parser with all argument in parse"""
    parser = ArgumentParser(add_help=True, description=PROGRAM_DESCRIPTION)
    parser.add_argument('-i', '--inputfile',
                        help="Path of InputFile",
                        default=None,
                        metavar="fasta file",
                        type=FileType('r'),
                        required=True,
                        nargs='+')
    parser.add_argument('-nb', '--nbmaxlenght',
                        help="Maximum Lenght retained",
                        default=0,
                        metavar="Whole number",
                        type=int,
                        required=False,
                        nargs=1)
    return parser


def execute(files, nb_max):
    """execute the main core of the program"""
    list_of_file = []
    for file in files:
        result = {}
        for line in file:
            if line[0] == ">":
                name_line = line[1:-1]
                result[name_line] = 1
            else:
                for char in line:
                    if char != "\n":
                        result[name_line] += 1
        list_of_file.append(result)
    for element in list_of_file:
        for key, value in element.items():
            if value > nb_max:
                print('Sequence named :', key, ', lenght :', value)


def main():
    """main function that create list of args, and check if it's ok."""
    parser = create_parser()
    args = parser.parse_args()
    try:
        execute(args.inputfile, args.nbmaxlenght[0])
    except ArgumentTypeError as error:
        print(error)


if __name__ == "__main__":
    main()
