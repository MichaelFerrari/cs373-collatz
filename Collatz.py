#!/usr/bin/env python3

# ---------------------------
# projects/collatz/Collatz.py
# Copyright (C) 2016
# Glenn P. Downing
# ---------------------------

# ------------
# collatz_read
# ------------


def collatz_read(string):
    """
    read two ints
    string tok string
    return a list of two ints, representing the beginning and end of a range, [i, j]
    """
    tok = string.split()
    return [int(tok[0]), int(tok[1])]

# ------------
# collatz_eval
# ------------


DICTION = {}  # A global cache diction


def collatz_eval(i, j):
    """
    i the beginning of the range, inclusive
    j the end       of the range, inclusive
    return the max cycle length of the range [i, j]
    """
    # We assert that i and j are int and in legal range
    assert i > 0
    assert i < 1000000
    assert isinstance(i, int)
    assert j > 0
    assert i < 1000000
    assert isinstance(j, int)
    if i > j:
        i, j = j, i
    max_cyclen = 0

    # We save the number with max cycle length
    num_max_cyclen = 837799
    DICTION[num_max_cyclen] = 525
    DICTION[1] = 1
    # We reduce the range of i to j
    if i < (j // 2 + 1):
        i = j // 2 + 1
    if i <= num_max_cyclen <= j:
        return 525

    # We loop through to find the number with the max cycle length
    for k in range(i, j + 1):
        cyclen = 1
        num = k

        if k in DICTION:
            cyclen = DICTION.get(k, None)
            k = 1
        while k != 1:
            cyclen += 1
            if k % 2 == 0:
                k //= 2
                assert isinstance(k, int)
                if k in DICTION:
                    cyclen += DICTION.get(k, None) - 1
                    k = 1
            else:
                k = 3 * k + 1
                assert isinstance(k, int)
                if k in DICTION:
                    cyclen += DICTION.get(k, None) - 1
                    k = 1
            if k == 1:
                DICTION[num] = cyclen

        # We replace the current max cycle length with a larger one, if it
        # exists
        if max_cyclen < cyclen:
            max_cyclen = cyclen
    return max_cyclen

# -------------
# collatz_print
# -------------


def collatz_print(writer, i, j, v_max):
    """
    print three ints
    writer a writer
    i the beginning of the range, inclusive
    j the end       of the range, inclusive
    v_max the max cycle length
    """
    writer.write(str(i) + " " + str(j) + " " + str(v_max) + "\n")

# -------------
# collatz_solve
# -------------


def collatz_solve(reader, writer):
    """
    reader a reader
    writer a writer
    """
    for string in reader:
        i, j = collatz_read(string)
        value = collatz_eval(i, j)
        collatz_print(writer, i, j, value)
