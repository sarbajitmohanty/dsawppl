def patternSearch(txt, pattern) -> list[int]:
    pos = txt.find(pattern)
    res = []
    while pos >= 0:
        res.append(pos)
        pos = txt.find(pattern, pos + 1)
    return res
