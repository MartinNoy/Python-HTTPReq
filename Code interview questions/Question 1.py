import sys
"""
The Challenge

In this exercise, you're going to decompress a compressed string.
Your input is a compressed string of the format number[string] and the decompressed output form should be the string written number times. 
For example:
The input:   3[abc]4[ab]c
Would be output as:  abcabcabcababababc

Other rules

Number can have more than one digit. For example, 10[a] is allowed, and just means aaaaaaaaaa
One repetition can occur inside another. For example, 2[3[a]b] decompresses into aaabaaab
Characters allowed as input include digits, small English letters and brackets [ ].
Digits are only to represent amount of repetitions.
Letters are just letters.
Brackets are only part of syntax of writing repeated substring.
Input is always valid, so no need to check its validity.

Learning objectives

This question gives you the chance to practice with strings, recursion, algorithm, compilers, automata, and loops. 
It’s also an opportunity to work on coding with better efficiency.
"""

def decomp(text, start=0, times=1):
    
    for x in xrange(times):
        i = start
        while i < len(text) and text[i] != ']':
            if text[i].islower():
                yield text[i]
        else:
            sub_times = 0
            while text[i].isdigit():
                sub_times = sub_times * 10 + int(text[i])
                i += 1
            for item in decomp(text, i, sub_times):
                if isinstance(item, basestring):
                    yield item
                else:
                    i = item
            i += 1
    if start > 0:
        yield i
def decompress(text):
    for letter in decomp(text):
        sys.stdout.write(letter)
        sys.stdout.write('')
if __name__ == '__main__':
    decompress("3[Ho3[la]]")
