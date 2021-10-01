'''
Lecture 30-09-2021
'''
# seq1 = 'asdasdasfasfasfasfhfhwoqwkd'
# seq2 = 'asdasdasfasfasfagjaslgjasld'
# subseq = 'ad'
# subseq = 'daaqw'
# subseq = 'aswq'

# A 'abc'
# B 'adc'

# 'ac' -> 2

#Input: seq1 seq2
#Goal: max_subseq_len(seq1, seq2)
'''
A = 'abcde'
''    -> '' (1)
'a'   -> '', 'a' (2)
'ab'  -> '', 'a', 'b', 'ab' (4)
'abc' -> '', 'a', 'b', 'ab', 'c', 'ac', 'bc', 'abc' (8)

2^N
'''

def find_subseq(seq):
    subseqs = ['']
    for c in seq:
        new_subseqs = []
        for s in subseqs:
            new_subseqs.append(s + c)
        subseqs += new_subseqs
    return subseqs

def intersect(seq1, seq2):
    common = []
    seq1 = set(seq1)
    for s in seq2:
        if s in seq1:
            common.append(s)
    return common

def find_max_len(seqs):
    return max([len(s) for s in seqs])
'''
Full iteration
o**n
'''
def max_subseq_len_bt(seq1, seq2):
    subseq1 = find_subseq(seq1)
    subseq2 = find_subseq(seq2)
    common = intersect(subseq1, subseq2)
    return find_max_len(common)

#seq1 = 'bbcdas'
#seq2 = 'dc'


'''
Recursion
Too long
'''
'''
if seq1[0] == seq2[0]:
    max_subseq_len = 1 + max_subseq_len(seq1[1:], seq2[1:])
else:
    max_subseq_len = max(max_subseq_len(seq1, seq2[1:]), max_subseq_len(seq1[1:], seq2))
'''


'''
Using cache in recursion
Dynamic programming top down

Create dictionary of dictionaries
val - global variable
Key - string, subsec
Value - max_subseq_len_rec
'''
from collections import defaultdict

cache = defaultdict(lambda: defaultdict(int))


def max_subseq_len_rec(seq1, seq2):
    if not seq1 or not seq2:
        return 0

    val = cache.get(seq1, {}).get(seq2, None)
    if val is not None:
        return val

    if seq1[0] == seq2[0]:
        val = 1 + max_subseq_len_rec(seq1[1:], seq2[1:])
    else:
        val = max(max_subseq_len_rec(seq1, seq2[1:]), max_subseq_len_rec(seq1[1:], seq2))
    cache[seq1][seq2] = val
    cache[seq2][seq1] = val

    return val

#A = 'dasdasdaskjdhjasld'
#B = 'jdljdlasjldjaskld'

'''
Make random and lang strings
'''
import string
import random

LEN = 5000

A = ''.join([random.choice(string.ascii_letters) for _ in range(LEN)])
B = ''.join([random.choice(string.ascii_letters) for _ in range(LEN)])

'''
Dynamic programming Upwards
Fill the cache
dp - necessary variable
'''
def max_subseq_len_dp(seq1, seq2):
   '''2-dimensional matrix'''
    dp = [[None for _ in range(len(seq2) + 1)] for _ in range(len(seq1) + 1)]
'''Fill the left edge of the matrix with zeros'''
    for i in range(len(seq1) + 1):
        dp[i][0] = 0

    for j in range(len(seq2) + 1):
        dp[0][j] = 0

    for i in range(1, len(seq1) + 1):
        for j in range(1, len(seq2) + 1):
            if seq1[i - 1] == seq2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[len(seq1)][len(seq2)]

# print(max_subseq_len_bt(A, B))
# print(max_subseq_len_rec(A, B))
print(max_subseq_len_dp(A, B))