#!/usr/bin/env python3

# ---------------------------
# projects/collatz/Collatz.py
# Copyright (C) 2016
# Glenn P. Downing
# ---------------------------

# ------------
# collatz_read
# ------------

import sys

def collatz_read(s):
    """
    read two ints
    s a string
    return a list of two ints, representing the beginning and end of a range, [i, j]
    """
    a = s.split()
    return [int(a[0]), int(a[1])]

# ------------
# collatz_eval
# ------------

cache = {}  # A global cache dictionary
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
    global cache
    
    # We save the number with max cycle length 
    num_max_cyclen = 837799
    cache[num_max_cyclen] = 525
    cache[1] = 1

    # We reduce the range of i to j
    if i < (j // 2 + 1):
        i = j // 2 + 1
    if i <= num_max_cyclen <= j:
        return 525

    # We loop through to find out the cycle length for each number 
    # and find the number with the max cycle length
    for k in range(i, j+1):
        cyclen = 1
        n = k
        if k in cache:
            cyclen = cache.get(k, None)
            k = 1
        while k != 1:
            cyclen += 1
            if k % 2 == 0:
                k //= 2
                assert isinstance(k, int)
                if k in cache:
                    cyclen += cache.get(k, None) - 1
                    k = 1
            else:
                k = 3 * k + 1
                assert isinstance(k, int)
                if k in cache:
                    cyclen += cache.get(k, None) - 1
                    k = 1
            if k == 1:
                cache[n] = cyclen
        
        # We replace the current max cycle length with a larger one, 
        # if it exists
        if max_cyclen < cyclen:
            max_cyclen = cyclen
    return max_cyclen

# -------------
# collatz_print
# -------------


def collatz_print(w, i, j, v):
    """
    print three ints
    w a writer
    i the beginning of the range, inclusive
    j the end       of the range, inclusive
    v the max cycle length
    """
    w.write(str(i) + " " + str(j) + " " + str(v) + "\n")

# -------------
# collatz_solve
# -------------


def collatz_solve(r, w):
    """
    r a reader
    w a writer
    """
    for s in r:
        if not s.strip():
            break
        i, j = collatz_read(s)
        v = collatz_eval(i, j)
        collatz_print(w, i, j, v)



# ----
# main
# ----

if __name__ == "__main__":
    collatz_solve(sys.stdin, sys.stdout)
