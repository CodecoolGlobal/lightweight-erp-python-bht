""" Common module
implement commonly used functions here
"""

import random


def generate_random(table):
    """
    Generates random and unique string. Used for id/key generation:
         - at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letter
         - it must be unique in the table (first value in every row is the id)

    Args:
        table (list): Data table to work on. First columns containing the keys.

    Returns:
        string: Random and unique string
    """

    generated = ''
    # your code

    passphrase_min_length = 2
    nums = '0123456789'
    letters = 'abcdefghijklmnopqrstuvwxyz'
    special_chars = "~!@#$%^&*()}{][+-_=/\\:\"'|,.?><"
    # must_contain [letters, letters, special_chars, nums]

    ID_num = [(random.choice(nums)) for x in range(0, passphrase_min_length)]
    ID_letters_upper = [(random.choice(letters.upper())) for x in range(0, passphrase_min_length)]
    ID_letters_lower = [(random.choice(letters)) for x in range(0, passphrase_min_length)]
    ID_special_chars = [(random.choice(special_chars)) for x in range(0, passphrase_min_length)]

    ID = ID_num + ID_letters_upper + ID_letters_lower + ID_special_chars
    generated = ''.join(ID)
    for line in table:
        if generated == line[0]:
            generated()
        else:
            return generated
