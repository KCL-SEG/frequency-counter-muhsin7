"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    for key in items:
        try:
            if frequencies[key]:
                frequencies[key] += 1
        except KeyError:
            frequencies[key] = 1

    return frequencies
