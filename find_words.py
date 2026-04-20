#! /usr/bin/env python3

import re

def main():
    import argparse

    # Create a command-line parser object
    parser = argparse.ArgumentParser()

input_file = 'example_input.txt'
word_root = 'nit'

def find_words_by_root(input_file, word_root):
    """
    Searches an input file for all occurrrences of words containing the root
    provided and returns a list of each word found and the line number that
    the word occurs on.

    Parameters
    ----------
    input_file : str
        A text file to be searched.
    word_root : str
        A string of the root to be searched for.

    Returns
    -------
    list
        A list with each word found and the line number associated
        with that word.

    Example
    --------
    >>> find_words_by_root('example_input.txt', 'nit')
    '1 nitrogen
    2 Nitrogenous
    3 nitrate
    3 nitrate
    4 nitrite
    7 Nitrogen
    8 nitrogen
    8 nitrogen'
    """
    root_pattern_str = r'[A-Za-z]*' + word_root + '+' + '[A-Za-z]*'
    root_pattern = re.compile(root_pattern_str, re.IGNORECASE)
    output_list = []

    with open(input_file, 'r') as in_stream:
            for line_num, line in enumerate(in_stream, 1):
                word_list = root_pattern.findall(line)
                if word_list:
                    line_word_list = [f"{line_num} {item}" for item in word_list]
                    output_list.extend(line_word_list)
            return output_list


def write_list(output_list, output_file):
    """
    Returns a file with each string from a list on a new line.

    Parameters
    ----------
    output_list : list
        List of strings to write to a file.
    output_file : str
        A file name to write the list to.

    Returns
    -------
    file
        A text file with each string from a list on a new line.
    """     
    with open(output_file, 'w') as out_stream:
        for item in output_list:
             out_stream.write(f'{item}\n')


if __name__ == '__main__':
    main()
    output_list = find_words_by_root(input_file, word_root)