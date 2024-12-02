def _KMP_search(text, pattern, start_index):
    if len(text) < len(pattern):
        return -1
    if start_index > len(text):
        return -1

    p = [0] * len(pattern)
    j = 0
    i = 1

    while i < len(pattern):
        if pattern[j] == pattern[i]:
            j += 1
            p[i] = j
            i += 1
        else:
            if j == 0:
                p[i] = 0
                i += 1
            else:
                j = p[j]
    
    j = 0
    i = start_index
    while i < len(text):
        if text[i] == pattern[j]:
            i += 1
            j += 1
            if j == len(pattern):
                return i - j
        else:
            if j > 0:
                j = p[j - 1]
            else:
                i += 1

    return -1

def search_all(text, pattern):
    start_index = 0
    all_indexes = []
    while True:
        index = _KMP_search(text, pattern, start_index)
        if index == -1:
            break
        all_indexes.append(index)
        start_index = index + 1
    return all_indexes

def find_shift(text, pattern):
    if len(text) < len(pattern):
        return -1
    p = text * 2
    return _KMP_search(p, pattern, 0)

# print(search_all("ababbababa", "aba"))

# print(find_shift("abcdz", "zabcd"))