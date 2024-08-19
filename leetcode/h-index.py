def hIndex(citations=[3, 0, 6, 1, 5]):
    sortedCitations = sorted(citations, reverse=True)
    i = -1
    h = 0
    while (i := i + 1) < len(sortedCitations):
        if not sortedCitations[i] > h: break
        h += 1
    return h
print(hIndex())
