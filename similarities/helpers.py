from nltk.tokenize import sent_tokenize


def lines(a, b):
    """Return lines in both a and b"""

    return list(set(a.splitlines()) & set(b.splitlines()))


def sentences(a, b):
    """Return sentences in both a and b"""

    return list(set(sent_tokenize(a)) & set(sent_tokenize(b)))


def substrings(a, b, n):
    """Return substrings of length n in both a and b"""

    return list(set(substringHelper(a, n)) & set(substringHelper(b, n)))


def substringHelper(a, n):
    """Helper to take all of the substrings of length n"""

    result = []
    length = len(a)
    start = 0
    end = n
    while (end <= length):
        result.append(a[start:end])
        start += 1
        end += 1
    return result