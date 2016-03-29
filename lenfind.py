#!/usr/bin/env python
import string, sys

charset = string.printable

def main():
    if len(sys.argv) < 2:
        print "Usage: python %s <hex data>" % (sys.argv[0])
        sys.exit(0)
    enc = [] # hex data will be stored in list of ints
    for char in sys.argv[1].decode("hex"):
        enc.append(ord(char))
    n_dict = {}
    min_n = -1
    min_total = -1
    for n in range(1, len(enc)):
        total = get_total(get_possible_values(enc, n))
        if total != 0:
            n_dict[n] = total
            if min_n == -1 and min_total == -1:
                min_n = n
                min_total = total
            else:
                if total < min_total:
                    min_n = n
                    min_total = total
    if min_n != -1 and min_total != -1:
        print "Best candidate: size=%d with %d possible values." % (min_n, min_total)
    else:
        print "No candidates found."

# Find possible values for each index of key size n for message enc
def get_possible_values(enc, n):
    possible = [] # store possible values for each index of key size n
    for i in range(n):
        i_possible = [] # store possible values for index i of key size n
        x = i
        while x < len(enc):
            x_possible = [] # store possible values for index x in message for index i of key size n
            for char in charset: # assume key is printable ASCII
                if chr(enc[x] ^ ord(char)) in charset:
                    x_possible.append(ord(char))
            if x == i: # no values in i_possible, skip checks
                i_possible.extend(x_possible)
            else:
                t_i_possible = [] # temp list, will overwrite i_possible after checks
                for value in i_possible:
                    if value in i_possible and value in x_possible: # make sure value doesn't only work for one index of message
                        t_i_possible.append(value)
                i_possible = t_i_possible
            x += n
        possible.append(i_possible)
    return possible

# Get total possibilites given list l holding values from get_possible(...)
def get_total(l):
    total = 1
    for sublist in l:
        total *= len(sublist)
    return total

if __name__ == "__main__":
    main()
