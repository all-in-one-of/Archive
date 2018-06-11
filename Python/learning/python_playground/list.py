
def histogram(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1;
        else:
            d[c] += 1
    return d

d = histogram('test')

def sortWords(*args):
    t = []
    for word in args:
        t.append((len(word), word))

    t.sort(reverse=True)

    result = []
    for length, word in t:
        result.append(word)

    return result

print sortWords("asdf", "tests", "b", "awesome")
