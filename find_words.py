#! /usr/bin/env python3

import re


def find_words_by_root(input_file, output_file, word_root):
    """
    Searches an input file for all occurrrences of words containing the root
    provided and returns a file with a list of each word found and the line
    number associated with that word.

    Parameters
    ----------
    input_file : str
        A text file to be searched.
    output_file : str
        A file name to write the list of words found to.
    word_root : str
        A string of the root to be searched for.

    Returns
    -------
    file
        A file with a list of each word found and the line number associated
        with that word.

    Examples
    --------
    find_words_by_root(input_file.txt, output_file, 'nit')
    5 nitrogen
    7 Nitrogenous
    13 nitrate 
    15 nitrite
    21 Nitrogen
    30 nitrogen
    """
    root_pattern_str = r'[A-Za-z]*' + word_root + '+' + '[A-Za-z]*'
    root_pattern = re.compile(root_pattern_str)

    with open(input_file, 'r') as in_stream:
        with open(output_file, 'w') as out_stream:
            for line in in_stream:
                match_object = root_pattern.search(in_stream)

                            if match_object:
                                return match_object.group()
                            return ''

                line = line.strip()
                word_list = line.split()
                word_list.sort()
                for word in word_list:
                    out_stream.write(f'{word}\n')

    


